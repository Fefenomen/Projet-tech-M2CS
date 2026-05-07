from sqlalchemy.orm import Session

from app.models.audit_log import AuditLog


def get_all_audit_logs(db: Session) -> list[AuditLog]:
    return db.query(AuditLog).order_by(AuditLog.created_at.desc()).all()


def get_audit_log_by_id(db: Session, log_id: int) -> AuditLog | None:
    return db.query(AuditLog).filter(AuditLog.id == log_id).first()
