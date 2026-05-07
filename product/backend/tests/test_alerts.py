import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.core.database import SessionLocal, engine, initialize_database, Base
from app.models.alert import Alert
from app.models.asset import Asset


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


# --- GET /alerts/ ---

def test_list_alerts_empty():
    token = get_token()
    response = client.get(
        "/api/v1/alerts/",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 0
    assert data["alerts"] == []
    assert data["by_severity"] == {"low": 0, "medium": 0, "high": 0, "critical": 0}
    assert data["by_status"] == {"nouvelle": 0, "en cours": 0, "cloturee": 0}


def test_list_alerts_without_token():
    response = client.get("/api/v1/alerts/")
    assert response.status_code == 401


def test_list_alerts_with_alerts():
    token = get_token()
    # Create alerts via POST
    client.post(
        "/api/v1/alerts/",
        json={"title": "Test Alert 1", "severity": "high", "source_ip": "10.0.0.1"},
        headers={"Authorization": f"Bearer {token}"},
    )
    client.post(
        "/api/v1/alerts/",
        json={"title": "Test Alert 2", "severity": "low", "source_ip": "10.0.0.2"},
        headers={"Authorization": f"Bearer {token}"},
    )

    response = client.get(
        "/api/v1/alerts/",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 2
    assert data["by_severity"]["high"] == 1
    assert data["by_severity"]["low"] == 1
    assert data["by_status"]["nouvelle"] == 2


# --- GET /alerts/{id} ---

def test_get_alert_by_id():
    token = get_token()
    # Create an alert first
    create_resp = client.post(
        "/api/v1/alerts/",
        json={"title": "Find me", "severity": "critical", "source_ip": "192.168.1.1"},
        headers={"Authorization": f"Bearer {token}"},
    )
    alert_id = create_resp.json()["id"]

    response = client.get(
        f"/api/v1/alerts/{alert_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Find me"
    assert data["severity"] == "critical"
    assert data["status"] == "nouvelle"


def test_get_alert_not_found():
    token = get_token()
    response = client.get(
        "/api/v1/alerts/99999",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 404


# --- POST /alerts/ ---

def test_create_alert_valid():
    token = get_token()
    response = client.post(
        "/api/v1/alerts/",
        json={"title": "Suspicious activity", "severity": "high", "source_ip": "10.0.0.5", "description": "3 failed logins"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Suspicious activity"
    assert data["severity"] == "high"
    assert data["status"] == "nouvelle"
    assert data["source_ip"] == "10.0.0.5"
    assert "id" in data
    assert "created_at" in data


def test_create_alert_default_severity():
    token = get_token()
    response = client.post(
        "/api/v1/alerts/",
        json={"title": "Default severity"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["severity"] == "medium"


def test_create_alert_invalid_severity():
    token = get_token()
    response = client.post(
        "/api/v1/alerts/",
        json={"title": "Bad", "severity": "super_high"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 422


def test_create_alert_without_token():
    response = client.post(
        "/api/v1/alerts/",
        json={"title": "No auth"},
    )
    assert response.status_code == 401


def test_create_alert_with_asset():
    token = get_token()
    # Create an asset first
    db = SessionLocal()
    try:
        asset = Asset(ip_address="10.10.10.1", hostname="test-host", status="active")
        db.add(asset)
        db.commit()
        asset_id = asset.id
    finally:
        db.close()

    response = client.post(
        "/api/v1/alerts/",
        json={"title": "Asset alert", "severity": "medium", "asset_id": asset_id},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["asset_id"] == asset_id


def test_create_alert_with_invalid_asset():
    token = get_token()
    response = client.post(
        "/api/v1/alerts/",
        json={"title": "Bad asset", "asset_id": 99999},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 404


# --- PATCH /alerts/{id} (status lifecycle) ---

def test_update_alert_nouvelle_to_en_cours():
    token = get_token()
    create_resp = client.post(
        "/api/v1/alerts/",
        json={"title": "Lifecycle test", "severity": "high"},
        headers={"Authorization": f"Bearer {token}"},
    )
    alert_id = create_resp.json()["id"]

    response = client.patch(
        f"/api/v1/alerts/{alert_id}",
        json={"status": "en cours"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "en cours"


def test_update_alert_en_cours_to_cloturee():
    token = get_token()
    # Create and transition to "en cours"
    create_resp = client.post(
        "/api/v1/alerts/",
        json={"title": "Close test"},
        headers={"Authorization": f"Bearer {token}"},
    )
    alert_id = create_resp.json()["id"]

    client.patch(
        f"/api/v1/alerts/{alert_id}",
        json={"status": "en cours"},
        headers={"Authorization": f"Bearer {token}"},
    )

    response = client.patch(
        f"/api/v1/alerts/{alert_id}",
        json={"status": "cloturee"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "cloturee"


def test_update_alert_nouvelle_to_cloturee_direct():
    token = get_token()
    create_resp = client.post(
        "/api/v1/alerts/",
        json={"title": "Direct close"},
        headers={"Authorization": f"Bearer {token}"},
    )
    alert_id = create_resp.json()["id"]

    # nouvelle -> cloturee is allowed
    response = client.patch(
        f"/api/v1/alerts/{alert_id}",
        json={"status": "cloturee"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "cloturee"


def test_update_alert_invalid_transition_cloturee_to_nouvelle():
    token = get_token()
    # Create, close it
    create_resp = client.post(
        "/api/v1/alerts/",
        json={"title": "Cannot reopen"},
        headers={"Authorization": f"Bearer {token}"},
    )
    alert_id = create_resp.json()["id"]

    client.patch(
        f"/api/v1/alerts/{alert_id}",
        json={"status": "cloturee"},
        headers={"Authorization": f"Bearer {token}"},
    )

    # Try to reopen
    response = client.patch(
        f"/api/v1/alerts/{alert_id}",
        json={"status": "nouvelle"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 400
    assert "Cannot transition" in response.json()["detail"]


def test_update_alert_invalid_status_value():
    token = get_token()
    create_resp = client.post(
        "/api/v1/alerts/",
        json={"title": "Bad status"},
        headers={"Authorization": f"Bearer {token}"},
    )
    alert_id = create_resp.json()["id"]

    response = client.patch(
        f"/api/v1/alerts/{alert_id}",
        json={"status": "invalid_status"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 422


def test_update_alert_not_found():
    token = get_token()
    response = client.patch(
        "/api/v1/alerts/99999",
        json={"status": "en cours"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 404


def test_update_alert_without_token():
    response = client.patch(
        "/api/v1/alerts/1",
        json={"status": "en cours"},
    )
    assert response.status_code == 401


def test_full_alert_lifecycle():
    token = get_token()
    create_resp = client.post(
        "/api/v1/alerts/",
        json={"title": "Full lifecycle", "severity": "critical", "source_ip": "1.2.3.4"},
        headers={"Authorization": f"Bearer {token}"},
    )
    alert_id = create_resp.json()["id"]
    assert create_resp.json()["status"] == "nouvelle"

    # nouvelle -> en cours
    resp = client.patch(
        f"/api/v1/alerts/{alert_id}",
        json={"status": "en cours"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 200
    assert resp.json()["status"] == "en cours"

    # en cours -> cloturee
    resp = client.patch(
        f"/api/v1/alerts/{alert_id}",
        json={"status": "cloturee"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 200
    assert resp.json()["status"] == "cloturee"

    # cloturee -> en cours (blocked)
    resp = client.patch(
        f"/api/v1/alerts/{alert_id}",
        json={"status": "en cours"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 400
