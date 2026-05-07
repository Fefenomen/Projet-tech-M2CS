from datetime import datetime, timezone
from sqlalchemy.orm import Session

from app.models.alert import Alert
from app.models.audit_log import AuditLog
from app.models.asset import Asset


def get_all_alerts(db: Session) -> list[Alert]:
    return db.query(Alert).order_by(Alert.created_at.desc()).all()


def get_alert_by_id(db: Session, alert_id: int) -> Alert | None:
    return db.query(Alert).filter(Alert.id == alert_id).first()


def create_alert(
    db: Session,
    title: str,
    severity: str,
    source_ip: str | None = None,
    description: str | None = None,
    asset_id: int | None = None,
) -> Alert:
    now = datetime.now(timezone.utc)
    alert = Alert(
        title=title,
        severity=severity,
        status="nouvelle",
        source_ip=source_ip,
        description=description,
        asset_id=asset_id,
        created_at=now,
        updated_at=now,
    )
    db.add(alert)
    db.commit()
    db.refresh(alert)
    return alert


def update_alert_status(db: Session, alert_id: int, new_status: str) -> Alert | None:
    alert = get_alert_by_id(db, alert_id)
    if not alert:
        return None
    alert.status = new_status
    alert.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(alert)
    return alert


def log_alert_action(db: Session, user_id: int | None, role: str | None, action: str, target_type: str, result: str = "success"):
    db.add(AuditLog(
        user_id=user_id,
        role=role,
        action=action,
        target_type=target_type,
        result=result,
    ))
    db.commit()


def get_alert_stats(db: Session) -> dict[str, int]:
    total = db.query(Alert).count()
    by_severity = {}
    by_status = {}
    for sev in ["low", "medium", "high", "critical"]:
        by_severity[sev] = db.query(Alert).filter(Alert.severity == sev).count()
    for stat in ["nouvelle", "en cours", "cloturee"]:
        by_status[stat] = db.query(Alert).filter(Alert.status == stat).count()
    return {"total": total, "by_severity": by_severity, "by_status": by_status}
