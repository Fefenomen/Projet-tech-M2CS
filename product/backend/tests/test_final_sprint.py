import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.core.database import SessionLocal, engine, initialize_database, Base
from app.models.alert import Alert
from app.models.audit_log import AuditLog
from app.telemetry.service import events_store, heartbeats
from app.traffic.service import captures_store


client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_test_db():
    Base.metadata.drop_all(bind=engine)
    initialize_database()
    heartbeats.clear()
    events_store.clear()
    captures_store.clear()
    yield
    Base.metadata.drop_all(bind=engine)


def get_token(username: str = "admin", password: str = "admin123") -> str:
    response = client.post(
        "/api/v1/auth/login",
        json={"username": username, "password": password},
    )
    if response.status_code == 200:
        return response.json()["access_token"]
    return ""


# --- US-02.8: Audit log on login ---

def test_audit_log_on_login_success():
    token = get_token()
    db = SessionLocal()
    try:
        logs = db.query(AuditLog).filter(AuditLog.action == "login_success").all()
        assert len(logs) >= 1
        assert logs[-1].result == "success"
        assert logs[-1].target_type == "auth"
    finally:
        db.close()


def test_audit_log_on_login_failed():
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "nobody", "password": "wrong"},
    )
    assert response.status_code == 401

    db = SessionLocal()
    try:
        logs = db.query(AuditLog).filter(AuditLog.action == "login_failed").all()
        assert len(logs) >= 1
        assert logs[-1].result == "failed"
    finally:
        db.close()


# --- US-02.12: Audit log on user creation ---

def test_audit_log_on_user_creation():
    token = get_token()
    response = client.post(
        "/api/v1/auth/users",
        json={"username": "newuser", "password": "test123", "role": "analyst"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201

    db = SessionLocal()
    try:
        logs = db.query(AuditLog).filter(AuditLog.action == "create_user").all()
        assert len(logs) >= 1
        assert logs[-1].result == "success"
        assert logs[-1].target_type == "user"
    finally:
        db.close()


# --- US-02.9: Auto alert detection ---

def test_auto_alert_on_suspicious_event():
    token = get_token()
    # Send a suspicious event type
    response = client.post(
        "/api/v1/telemetry/events",
        json={
            "hostname": "endpoint1",
            "events": [
                {"event_type": "port_scan", "source_ip": "10.0.0.99", "message": "Scan detected", "severity": "medium"},
            ],
        },
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201

    db = SessionLocal()
    try:
        alerts = db.query(Alert).filter(Alert.source_ip == "10.0.0.99").all()
        assert len(alerts) >= 1
        assert "port_scan" in alerts[0].title.lower()
    finally:
        db.close()


def test_auto_alert_on_repeated_events():
    token = get_token()
    # Send 3 similar events from same IP
    for i in range(3):
        client.post(
            "/api/v1/telemetry/events",
            json={
                "hostname": "endpoint1",
                "events": [
                    {"event_type": "http_request", "source_ip": "10.0.0.50", "message": f"Request {i}", "severity": "low"},
                ],
            },
            headers={"Authorization": f"Bearer {token}"},
        )

    db = SessionLocal()
    try:
        alerts = db.query(Alert).filter(Alert.source_ip == "10.0.0.50").all()
        assert len(alerts) >= 1
        assert "r" in alerts[0].title.lower() or "p" in alerts[0].title.lower()
    finally:
        db.close()


def test_auto_alert_audit_logged():
    token = get_token()
    client.post(
        "/api/v1/telemetry/events",
        json={
            "hostname": "endpoint1",
            "events": [
                {"event_type": "failed_login", "source_ip": "10.0.0.77", "message": "Failed login", "severity": "high"},
            ],
        },
        headers={"Authorization": f"Bearer {token}"},
    )

    db = SessionLocal()
    try:
        logs = db.query(AuditLog).filter(AuditLog.action == "alert_auto_created").all()
        assert len(logs) >= 1
    finally:
        db.close()


def test_no_duplicate_alert_same_ip_same_rule():
    token = get_token()
    # Send same suspicious event twice quickly
    for _ in range(2):
        client.post(
            "/api/v1/telemetry/events",
            json={
                "hostname": "endpoint1",
                "events": [
                    {"event_type": "port_scan", "source_ip": "10.0.0.88", "message": "Scan", "severity": "medium"},
                ],
            },
            headers={"Authorization": f"Bearer {token}"},
        )

    db = SessionLocal()
    try:
        alerts = db.query(Alert).filter(Alert.source_ip == "10.0.0.88").all()
        assert len(alerts) == 1
    finally:
        db.close()


# --- US-02.10: Traffic capture ---

def test_capture_traffic():
    token = get_token()
    response = client.post(
        "/api/v1/traffic/",
        json={
            "hostname": "endpoint1",
            "source_ip": "10.0.0.1",
            "target_ip": "10.0.0.2",
            "source_port": 54321,
            "target_port": 80,
            "protocol": "tcp",
            "payload_summary": "GET / HTTP/1.1",
        },
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["protocol"] == "tcp"
    assert data["target_port"] == 80


def test_list_traffic():
    token = get_token()
    # Add some captures
    for i in range(3):
        client.post(
            "/api/v1/traffic/",
            json={
                "hostname": "endpoint1",
                "source_ip": f"10.0.0.{i+1}",
                "target_ip": "10.0.0.10",
                "source_port": 50000 + i,
                "target_port": 80,
                "protocol": "tcp",
                "payload_summary": f"Request {i}",
            },
            headers={"Authorization": f"Bearer {token}"},
        )

    response = client.get("/api/v1/traffic/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 3
    assert len(data["captures"]) == 3


def test_list_traffic_filter_protocol():
    token = get_token()
    client.post(
        "/api/v1/traffic/",
        json={
            "hostname": "endpoint1",
            "source_ip": "10.0.0.1",
            "target_ip": "10.0.0.2",
            "source_port": 12345,
            "target_port": 53,
            "protocol": "dns",
            "payload_summary": "DNS query",
        },
        headers={"Authorization": f"Bearer {token}"},
    )

    response = client.get("/api/v1/traffic/?protocol=dns", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["total"] >= 1
    assert data["captures"][0]["protocol"] == "dns"


def test_traffic_invalid_protocol():
    token = get_token()
    response = client.post(
        "/api/v1/traffic/",
        json={
            "hostname": "endpoint1",
            "source_ip": "10.0.0.1",
            "target_ip": "10.0.0.2",
            "source_port": 1234,
            "target_port": 80,
            "protocol": "invalid_protocol",
        },
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 422


def test_traffic_requires_auth():
    response = client.post("/api/v1/traffic/", json={
        "hostname": "x", "source_ip": "1.1.1.1", "target_ip": "2.2.2.2",
        "source_port": 80, "target_port": 80, "protocol": "tcp",
    })
    assert response.status_code == 401
