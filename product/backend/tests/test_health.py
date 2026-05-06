import pytest
from fastapi.testclient import TestClient

from app.health import router as health_router
from app.main import app
from app.telemetry import service as telemetry_service

client = TestClient(app)

SECRET_KEY = "your-secret-key-here-change-me"


@pytest.fixture(autouse=True)
def clear_heartbeats():
    telemetry_service.heartbeats.clear()
    yield
    telemetry_service.heartbeats.clear()


def get_token(username: str = "admin", password: str = "admin123") -> str:
    response = client.post(
        "/api/v1/auth/login",
        json={"username": username, "password": password},
    )
    if response.status_code == 200:
        return response.json()["access_token"]
    return ""


def test_health_check():
    response = client.get("/health/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["database"] == "ok"
    assert "service" in data
    assert "version" in data


def test_health_check_degraded_database(monkeypatch):
    monkeypatch.setattr(health_router, "check_database_connection", lambda: False)

    response = client.get("/health/")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "degraded"
    assert data["database"] == "error"


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "running"
    assert "service" in data


def test_login_valid():
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "admin", "password": "admin123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_password():
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "admin", "password": "wrongpassword"},
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"


def test_login_invalid_user():
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "nonexistent", "password": "admin123"},
    )
    assert response.status_code == 401


def test_protected_route_without_token():
    response = client.get("/api/v1/protected")
    assert response.status_code == 401


def test_protected_route_with_valid_token():
    token = get_token()
    response = client.get(
        "/api/v1/protected",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["user"] == "admin"


def test_heartbeat_without_token():
    response = client.post(
        "/api/v1/telemetry/heartbeat",
        json={"hostname": "endpoint-01"},
    )
    assert response.status_code == 401


def test_heartbeat_valid():
    token = get_token()
    response = client.post(
        "/api/v1/telemetry/heartbeat",
        json={"hostname": "endpoint-01", "status": "up", "version": "1.0.0"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["hostname"] == "endpoint-01"
    assert data["status"] == "up"
    assert "id" in data
    assert data["message"] == "Heartbeat received"


def test_heartbeat_invalid_payload():
    token = get_token()
    response = client.post(
        "/api/v1/telemetry/heartbeat",
        json={},  # Missing required field 'hostname'
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 422  # Validation error


def test_list_heartbeats():
    token = get_token()
    # First, send a heartbeat
    client.post(
        "/api/v1/telemetry/heartbeat",
        json={"hostname": "endpoint-02"},
        headers={"Authorization": f"Bearer {token}"},
    )
    # Then list heartbeats
    response = client.get(
        "/api/v1/telemetry/heartbeats",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
