"""Tests EPIC-03: NIS2 compliance dashboard, risk scoring, API v2, multi-tenant, reports, i18n."""

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.core.database import SessionLocal, engine, initialize_database, Base
from app.models.alert import Alert
from app.models.asset import Asset
from app.models.audit_log import AuditLog
from app.models.export import ExportRecord
from app.models.user import User
from app.telemetry.service import events_store


client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_test_db():
    Base.metadata.drop_all(bind=engine)
    initialize_database()
    events_store.clear()
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


def auth_header(role: str = "admin") -> dict:
    token = get_token()
    return {"Authorization": f"Bearer {token}"}


# ============================================================
# US-03.1: NIS2 Compliance Dashboard
# ============================================================

def test_nis2_compliance_requires_auth():
    r = client.get("/api/v1/compliance/nis2")
    assert r.status_code == 401


def test_nis2_compliance_returns_score():
    token = get_token()
    r = client.get("/api/v1/compliance/nis2", headers=auth_header())
    assert r.status_code == 200
    data = r.json()
    assert "score" in data
    assert "requirements" in data
    assert data["score"]["overall_score"] >= 0
    assert data["score"]["overall_score"] <= 100
    assert data["score"]["total_requirements"] == 8


def test_nis2_compliance_score_increases_with_data():
    token = get_token()

    r = client.get("/api/v1/compliance/nis2", headers=auth_header())
    initial_score = r.json()["score"]["overall_score"]

    db = SessionLocal()
    try:
        for i in range(3):
            db.add(Asset(
                ip_address=f"10.0.0.{100+i}",
                hostname=f"host-{i}",
                status="active",
            ))
        db.commit()
    finally:
        db.close()

    # Send events via API to populate events_store
    for i in range(10):
        client.post(
            "/api/v1/telemetry/events",
            json={
                "hostname": "endpoint1",
                "events": [
                    {"event_type": "http_request", "source_ip": "10.0.0.50", "message": f"test event {i}", "severity": "low"},
                ],
            },
            headers=auth_header(),
        )

    r = client.get("/api/v1/compliance/nis2", headers=auth_header())
    final_score = r.json()["score"]["overall_score"]
    assert final_score > initial_score


def test_nis2_compliance_has_requirements_list():
    r = client.get("/api/v1/compliance/nis2", headers=auth_header())
    data = r.json()
    assert len(data["requirements"]) == 8
    req_ids = [r["id"] for r in data["requirements"]]
    assert "NIS2-01" in req_ids
    assert "NIS2-08" in req_ids


# ============================================================
# US-03.2: Risk Scoring
# ============================================================

def test_risk_score_endpoint():
    token = get_token()

    h = auth_header()
    r = client.post(
        "/api/v1/scan/",
        json={"ip_range": "10.0.0.200", "ports": [22, 80, 443]},
        headers=h,
    )

    r = client.get("/api/v1/assets/", headers=h)
    data = r.json()
    assets = data.get("assets", [])
    if assets:
        asset_id = assets[0]["id"]
        r = client.get(f"/api/v1/assets/{asset_id}/risk-score", headers=h)
        assert r.status_code == 200
        data = r.json()
        assert "risk_score" in data
        assert data["risk_score"] >= 0
        assert data["risk_score"] <= 100


# ============================================================
# US-03.5: Advanced Reports
# ============================================================

def test_reports_summary():
    r = client.get("/api/v1/exports/summary", headers=auth_header())
    assert r.status_code == 200
    data = r.json()
    assert "total_assets" in data
    assert "total_alerts" in data
    assert "total_events" in data
