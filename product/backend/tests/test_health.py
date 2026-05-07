import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.core.database import SessionLocal, engine, initialize_database, Base
from app.models.user import User
from app.auth.service import get_password_hash

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_test_db():
    """Reset DB before each test and seed default users."""
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


# --- Health ---

def test_health_check():
    response = client.get("/health/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["database"] == "ok"
    assert "service" in data
    assert "version" in data


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "BigBrowser" in response.text


# --- Auth login ---

def test_login_valid():
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "admin", "password": "admin123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_analyst():
    response = client.post(
        "/api/v1/auth/login",
        json={"username": "analyst", "password": "analyst123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data


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


# --- GET /auth/me ---

def test_get_me_valid():
    token = get_token()
    response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "admin"
    assert data["role"] == "admin"
    assert data["is_active"] is True


def test_get_me_without_token():
    response = client.get("/api/v1/auth/me")
    assert response.status_code == 401


# --- Role-based access ---

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
    assert data["user"] == "admin"
    assert data["role"] == "admin"


# --- POST /auth/users (admin only) ---

def test_create_user_as_admin():
    token = get_token()
    response = client.post(
        "/api/v1/auth/users",
        json={"username": "newuser", "password": "newpass123", "role": "analyst"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "newuser"
    assert data["role"] == "analyst"
    assert data["is_active"] is True


def test_create_user_duplicate():
    token = get_token()
    response = client.post(
        "/api/v1/auth/users",
        json={"username": "admin", "password": "whatever", "role": "analyst"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 400
    assert "already" in response.json()["detail"].lower()


def test_create_user_as_analyst_forbidden():
    token = get_token("analyst", "analyst123")
    response = client.post(
        "/api/v1/auth/users",
        json={"username": "newuser", "password": "newpass123", "role": "analyst"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 403


def test_create_user_no_token():
    response = client.post(
        "/api/v1/auth/users",
        json={"username": "newuser", "password": "newpass123", "role": "analyst"},
    )
    assert response.status_code == 401


# --- Telemetry heartbeat ---

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
        json={},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 422


def test_list_heartbeats():
    token = get_token()
    client.post(
        "/api/v1/telemetry/heartbeat",
        json={"hostname": "endpoint-02"},
        headers={"Authorization": f"Bearer {token}"},
    )
    response = client.get(
        "/api/v1/telemetry/heartbeats",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
