import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.core.database import SessionLocal, engine, initialize_database, Base
from app.models.alert import Alert
from app.models.asset import Asset
from app.models.audit_log import AuditLog
from app.models.export import ExportRecord


client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_test_db():
    Base.metadata.drop_all(bind=engine)
    initialize_database()
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


def seed_data():
    db = SessionLocal()
    try:
        for i in range(3):
            alert = Alert(
                title=f"Alert {i}",
                severity=["low", "medium", "high"][i],
                status=["nouvelle", "en cours", "cloturee"][i],
                source_ip=f"10.0.0.{i+1}",
                description=f"Test alert {i}",
            )
            db.add(alert)

        for i in range(2):
            asset = Asset(ip_address=f"192.168.1.{i+1}", hostname=f"srv-{i+1}", status="active")
            db.add(asset)

        db.add(AuditLog(action="test_action", target_type="test", result="success"))
        db.add(ExportRecord(format="csv", requested_by="admin", scope="alerts", file_path="/tmp/test.csv", row_count=5))
        db.commit()
    finally:
        db.close()


def test_dashboard_requires_auth():
    response = client.get("/api/v1/dashboard/")
    assert response.status_code == 401


def test_dashboard_returns_metrics():
    token = get_token()
    seed_data()

    response = client.get(
        "/api/v1/dashboard/",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "metrics" in data
    assert "recent_alerts" in data

    m = data["metrics"]
    assert m["total_alerts"] == 3
    assert m["total_assets"] == 2
    assert m["total_audit_logs"] >= 1
    assert m["total_exports"] == 1
    assert "nouvelle" in m["alerts_by_status"]
    assert "high" in m["alerts_by_severity"]
    assert len(data["recent_alerts"]) == 3


def test_dashboard_empty_data():
    token = get_token()

    response = client.get(
        "/api/v1/dashboard/",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["metrics"]["total_alerts"] == 0
    assert data["metrics"]["total_assets"] == 0
    assert len(data["recent_alerts"]) == 0


def test_serves_frontend_index():
    response = client.get("/")
    assert response.status_code == 200
    assert "BigBrowser" in response.text
    assert "SOC Dashboard" in response.text


def test_analyst_can_access_dashboard():
    token = get_token("analyst", "analyst123")
    response = client.get(
        "/api/v1/dashboard/",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
