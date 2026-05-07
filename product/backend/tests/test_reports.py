import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.core.database import SessionLocal, engine, initialize_database, Base
from app.models.alert import Alert
from app.models.asset import Asset
from app.models.audit_log import AuditLog
from app.reports.service import _export_dir, _alert_to_dict
import json
import os


client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_test_db():
    Base.metadata.drop_all(bind=engine)
    initialize_database()
    yield
    Base.metadata.drop_all(bind=engine)
    # Clean export files
    exp_dir = _export_dir()
    if os.path.exists(exp_dir):
        for f in os.listdir(exp_dir):
            os.remove(os.path.join(exp_dir, f))


def get_token(username: str = "admin", password: str = "admin123") -> str:
    response = client.post(
        "/api/v1/auth/login",
        json={"username": username, "password": password},
    )
    if response.status_code == 200:
        return response.json()["access_token"]
    return ""


# --- Export endpoints ---

def test_export_csv_alerts():
    token = get_token()
    # Create some alerts first
    for i in range(3):
        client.post(
            "/api/v1/alerts/",
            json={"title": f"Alert {i}", "severity": "high"},
            headers={"Authorization": f"Bearer {token}"},
        )

    response = client.post(
        "/api/v1/exports/",
        json={"format": "csv", "scope": "alerts"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["format"] == "csv"
    assert data["scope"] == "alerts"
    assert data["row_count"] == 3
    assert "exp_" in data["file_path"]
    assert data["file_path"].endswith(".csv")

    # Verify file exists and has content
    with open(data["file_path"]) as f:
        content = f.read()
    assert "title" in content
    assert "Alert 0" in content


def test_export_json_alerts():
    token = get_token()
    client.post(
        "/api/v1/alerts/",
        json={"title": "JSON test", "severity": "critical", "source_ip": "10.0.0.1"},
        headers={"Authorization": f"Bearer {token}"},
    )

    response = client.post(
        "/api/v1/exports/",
        json={"format": "json", "scope": "alerts"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["format"] == "json"
    assert data["row_count"] == 1

    with open(data["file_path"]) as f:
        payload = json.load(f)
    assert payload["export_id"].startswith("exp_")
    assert payload["format"] == "json"
    assert payload["scope"] == "alerts"
    assert len(payload["items"]) == 1
    assert payload["items"][0]["title"] == "JSON test"


def test_export_json_assets():
    token = get_token()
    db = SessionLocal()
    try:
        asset = Asset(ip_address="10.0.0.5", hostname="srv-web", status="active")
        db.add(asset)
        db.commit()
    finally:
        db.close()

    response = client.post(
        "/api/v1/exports/",
        json={"format": "json", "scope": "assets"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["scope"] == "assets"
    assert data["row_count"] == 1


def test_export_invalid_format():
    token = get_token()
    response = client.post(
        "/api/v1/exports/",
        json={"format": "xml", "scope": "alerts"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 422


def test_export_invalid_scope():
    token = get_token()
    response = client.post(
        "/api/v1/exports/",
        json={"format": "csv", "scope": "unknown"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 422


def test_export_without_token():
    response = client.post(
        "/api/v1/exports/",
        json={"format": "csv", "scope": "alerts"},
    )
    assert response.status_code == 401


def test_export_empty_data():
    token = get_token()
    response = client.post(
        "/api/v1/exports/",
        json={"format": "csv", "scope": "alerts"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201
    assert response.json()["row_count"] == 0


def test_export_download():
    token = get_token()
    # Create and export
    create_resp = client.post(
        "/api/v1/exports/",
        json={"format": "json", "scope": "alerts"},
        headers={"Authorization": f"Bearer {token}"},
    )
    export_id = create_resp.json()["id"]

    response = client.get(
        f"/api/v1/exports/{export_id}/download",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert response.headers["content-type"] in ("application/json", "text/csv; charset=utf-8")


def test_export_download_not_found():
    token = get_token()
    response = client.get(
        "/api/v1/exports/99999/download",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 404


# --- Audit log endpoints ---

def test_list_audit_logs_as_admin():
    token = get_token()
    response = client.get(
        "/api/v1/audit-logs/",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "logs" in data
    assert "total" in data
    assert isinstance(data["logs"], list)


def test_list_audit_logs_as_analyst_forbidden():
    token = get_token("analyst", "analyst123")
    response = client.get(
        "/api/v1/audit-logs/",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 403


def test_list_audit_logs_without_token():
    response = client.get("/api/v1/audit-logs/")
    assert response.status_code == 401


def test_audit_logs_populated_after_export():
    token = get_token()
    # Create an export to generate an audit log
    client.post(
        "/api/v1/exports/",
        json={"format": "csv", "scope": "alerts"},
        headers={"Authorization": f"Bearer {token}"},
    )

    response = client.get(
        "/api/v1/audit-logs/",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    # Should have at least the export audit log
    export_logs = [log for log in data["logs"] if log["action"] == "export_data"]
    assert len(export_logs) >= 1
    assert export_logs[0]["target_type"] == "alerts"
    assert export_logs[0]["result"] == "export_csv"


def test_audit_log_detail():
    token = get_token()
    response = client.get(
        "/api/v1/audit-logs/",
        headers={"Authorization": f"Bearer {token}"},
    )
    data = response.json()
    if data["total"] > 0:
        log_id = data["logs"][0]["id"]
        detail_resp = client.get(
            f"/api/v1/audit-logs/{log_id}",
            headers={"Authorization": f"Bearer {token}"},
        )
        assert detail_resp.status_code == 200
        assert detail_resp.json()["id"] == log_id
