import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.core.database import SessionLocal, engine, initialize_database, Base
from app.models.asset import Asset
from app.models.port import Port
from app.discovery.schemas import validate_ipv4, ip_range_to_list


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


# --- IP Validation ---

def test_validate_ipv4_valid():
    assert validate_ipv4("192.168.1.1") is True
    assert validate_ipv4("10.0.0.1") is True
    assert validate_ipv4("255.255.255.255") is True
    assert validate_ipv4("0.0.0.0") is True


def test_validate_ipv4_invalid():
    assert validate_ipv4("999.999.999.999") is False
    assert validate_ipv4("192.168.1") is False
    assert validate_ipv4("abc.def.ghi.jkl") is False
    assert validate_ipv4("192.168.1.1; rm -rf /") is False
    assert validate_ipv4("") is False


def test_ip_range_generation():
    ips = ip_range_to_list("192.168.1.1", "192.168.1.3")
    assert len(ips) == 3
    assert ips == ["192.168.1.1", "192.168.1.2", "192.168.1.3"]


# --- Scan endpoint ---

def test_scan_without_token():
    response = client.post(
        "/api/v1/scan/",
        json={"start_ip": "127.0.0.1", "end_ip": "127.0.0.1"},
    )
    assert response.status_code == 401


def test_scan_as_analyst_forbidden():
    token = get_token("analyst", "analyst123")
    response = client.post(
        "/api/v1/scan/",
        json={"start_ip": "127.0.0.1", "end_ip": "127.0.0.1"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 403


def test_scan_invalid_ip_rejected():
    token = get_token()
    response = client.post(
        "/api/v1/scan/",
        json={"start_ip": "invalid", "end_ip": "127.0.0.1"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 422


def test_scan_injection_rejected():
    token = get_token()
    response = client.post(
        "/api/v1/scan/",
        json={"start_ip": "127.0.0.1; rm -rf /", "end_ip": "127.0.0.1"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 422


def test_scan_range_too_large():
    token = get_token()
    response = client.post(
        "/api/v1/scan/",
        json={"start_ip": "10.0.0.1", "end_ip": "10.0.2.0"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 400
    assert "too large" in response.json()["detail"].lower()


def test_scan_single_ip_localhost():
    token = get_token()
    response = client.post(
        "/api/v1/scan/",
        json={"start_ip": "127.0.0.1", "end_ip": "127.0.0.1", "ports": [80]},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["status"] == "completed"
    assert data["start_ip"] == "127.0.0.1"
    assert data["ports_scanned"] == 1


# --- Assets endpoints ---

def test_list_assets_empty():
    token = get_token()
    response = client.get(
        "/api/v1/assets/",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 0
    assert data["assets"] == []


def test_list_assets_without_token():
    response = client.get("/api/v1/assets/")
    assert response.status_code == 401


def test_asset_not_found():
    token = get_token()
    response = client.get(
        "/api/v1/assets/99999",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 404


def test_asset_detail_with_ports():
    token = get_token()
    db = SessionLocal()
    try:
        asset = Asset(ip_address="10.0.0.1", hostname="test-server", status="active")
        db.add(asset)
        db.flush()
        db.add(Port(asset_id=asset.id, port=22, protocol="tcp", state="open", service_name="ssh"))
        db.add(Port(asset_id=asset.id, port=80, protocol="tcp", state="open", service_name="http"))
        db.commit()
        asset_id = asset.id
    finally:
        db.close()

    response = client.get(
        f"/api/v1/assets/{asset_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["ip_address"] == "10.0.0.1"
    assert data["hostname"] == "test-server"
    assert data["status"] == "active"
    assert len(data["ports"]) == 2
    assert data["ports"][0]["port"] == 22
    assert data["ports"][0]["service_name"] == "ssh"
