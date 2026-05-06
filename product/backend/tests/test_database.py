from uuid import uuid4

import pytest
from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError

from app.core.database import SessionLocal, engine, initialize_database
from app.models.alert import Alert
from app.models.asset import Asset
from app.models.audit_log import AuditLog
from app.models.export import ExportRecord
from app.models.port import Port
from app.models.user import User


def test_db_connection():
    initialize_database()
    inspector = inspect(engine)
    tables = set(inspector.get_table_names())

    assert {"users", "assets", "ports", "alerts", "audit_logs", "exports"}.issubset(tables)


def test_models_creation():
    suffix = uuid4().hex[:8]
    session = SessionLocal()

    try:
        user = User(
            username=f"user_{suffix}",
            password_hash="hashed-password",
            role="admin",
            is_active=True,
        )
        asset = Asset(ip_address=f"10.0.{int(suffix[:2], 16) % 250}.{int(suffix[2:4], 16) % 250}", hostname=f"host-{suffix}")
        session.add_all([user, asset])
        session.flush()

        port = Port(asset_id=asset.id, port=443, protocol="tcp", state="open")
        alert = Alert(
            title=f"Alert {suffix}",
            severity="high",
            status="nouvelle",
            source_ip=asset.ip_address,
            description="Test alert",
            asset_id=asset.id,
        )
        audit_log = AuditLog(user_id=user.id, role=user.role, action="test_action", target_type="asset", result="success")
        export_record = ExportRecord(
            format="json",
            requested_by=user.username,
            scope="alerts",
            file_path=f"/tmp/export-{suffix}.json",
            row_count=1,
        )

        session.add_all([port, alert, audit_log, export_record])
        session.commit()

        assert user.id is not None
        assert asset.id is not None
        assert port.id is not None
        assert alert.id is not None
        assert audit_log.id is not None
        assert export_record.id is not None
    finally:
        session.close()


def test_user_username_is_unique():
    suffix = uuid4().hex[:8]
    username = f"duplicate_{suffix}"
    session = SessionLocal()

    try:
        session.add(User(username=username, password_hash="hash-1", role="admin", is_active=True))
        session.commit()

        session.add(User(username=username, password_hash="hash-2", role="analyst", is_active=True))
        with pytest.raises(IntegrityError):
            session.commit()
    finally:
        session.rollback()
        session.close()


def test_asset_delete_cascades_ports():
    suffix = uuid4().hex[:8]
    ip_address = f"10.1.{int(suffix[:2], 16) % 250}.{int(suffix[2:4], 16) % 250}"
    session = SessionLocal()

    try:
        asset = Asset(ip_address=ip_address, hostname=f"asset-{suffix}")
        session.add(asset)
        session.flush()

        port = Port(asset_id=asset.id, port=8443, protocol="tcp", state="open")
        session.add(port)
        session.commit()

        port_id = port.id
        session.delete(asset)
        session.commit()

        assert session.get(Port, port_id) is None
    finally:
        session.close()
