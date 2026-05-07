from collections import Counter
from datetime import datetime

from sqlalchemy.orm import Session

from app.models.alert import Alert
from app.models.asset import Asset
from app.models.audit_log import AuditLog
from app.models.export import ExportRecord


def get_dashboard_metrics(db: Session) -> dict:
    alerts = db.query(Alert).all()
    assets = db.query(Asset).all()
    audit_logs = db.query(AuditLog).all()
    exports = db.query(ExportRecord).all()

    alerts_by_status = dict(Counter(a.status for a in alerts))
    alerts_by_severity = dict(Counter(a.severity for a in alerts))
    assets_by_status = dict(Counter(a.status for a in assets))

    recent_alerts = (
        db.query(Alert)
        .order_by(Alert.created_at.desc())
        .limit(10)
        .all()
    )

    return {
        "total_alerts": len(alerts),
        "alerts_by_status": alerts_by_status,
        "alerts_by_severity": alerts_by_severity,
        "total_assets": len(assets),
        "assets_by_status": assets_by_status,
        "total_audit_logs": len(audit_logs),
        "total_exports": len(exports),
        "recent_alerts": [
            {
                "id": a.id,
                "title": a.title,
                "severity": a.severity,
                "status": a.status,
                "source_ip": a.source_ip,
                "created_at": a.created_at,
            }
            for a in recent_alerts
        ],
    }
