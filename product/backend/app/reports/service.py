import csv
import io
import json
import os
import tempfile
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.alert import Alert
from app.models.asset import Asset
from app.models.audit_log import AuditLog
from app.models.export import ExportRecord


def _export_dir() -> str:
    path = os.path.join(tempfile.gettempdir(), "bigbrowser_exports")
    os.makedirs(path, exist_ok=True)
    return path


def _alert_to_dict(alert: Alert) -> dict:
    return {
        "id": alert.id,
        "title": alert.title,
        "severity": alert.severity,
        "status": alert.status,
        "source_ip": alert.source_ip or "",
        "description": alert.description or "",
        "created_at": alert.created_at.isoformat() if alert.created_at else "",
        "updated_at": alert.updated_at.isoformat() if alert.updated_at else "",
    }


def _asset_to_dict(asset: Asset) -> dict:
    return {
        "id": asset.id,
        "ip_address": asset.ip_address,
        "hostname": asset.hostname or "",
        "status": asset.status,
        "first_seen_at": asset.first_seen_at.isoformat() if asset.first_seen_at else "",
        "last_seen_at": asset.last_seen_at.isoformat() if asset.last_seen_at else "",
        "ports": [{"port": p.port, "protocol": p.protocol, "state": p.state, "service_name": getattr(p, "service_name", "")} for p in asset.ports],
    }


def _audit_to_dict(log: AuditLog) -> dict:
    return {
        "id": log.id,
        "user_id": log.user_id,
        "role": log.role or "",
        "action": log.action,
        "target_type": log.target_type or "",
        "result": log.result,
        "created_at": log.created_at.isoformat() if log.created_at else "",
    }


def generate_export(
    db: Session,
    fmt: str,
    scope: str,
    requested_by: str,
) -> ExportRecord:
    now = datetime.now(timezone.utc)
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    export_id = f"exp_{timestamp}"

    data: list[dict] = []
    if scope == "alerts":
        items = db.query(Alert).order_by(Alert.created_at.desc()).all()
        data = [_alert_to_dict(a) for a in items]
    elif scope == "assets":
        items = db.query(Asset).order_by(Asset.last_seen_at.desc()).all()
        data = [_asset_to_dict(a) for a in items]
    elif scope == "audit_logs":
        items = db.query(AuditLog).order_by(AuditLog.created_at.desc()).all()
        data = [_audit_to_dict(a) for a in items]

    if fmt == "csv":
        file_path = os.path.join(_export_dir(), f"{export_id}.csv")
        with open(file_path, "w", newline="") as f:
            if data:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            else:
                f.write("")
    else:
        file_path = os.path.join(_export_dir(), f"{export_id}.json")
        payload = {
            "export_id": export_id,
            "generated_at": now.isoformat(),
            "format": fmt,
            "scope": scope,
            "items": data,
        }
        with open(file_path, "w") as f:
            json.dump(payload, f, indent=2, default=str)

    record = ExportRecord(
        format=fmt,
        requested_by=requested_by,
        scope=scope,
        file_path=file_path,
        created_at=now,
        row_count=len(data),
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record
