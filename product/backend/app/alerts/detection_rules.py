"""Simple detection rules engine for MVP.

Rules:
  1. 3+ events of the same type from the same source IP within a time window → alert
  2. Known suspicious event types (port_scan, failed_login, brute_force) → alert immediately
"""

from datetime import datetime, timezone, timedelta

from app.models.alert import Alert


THRESHOLD_REPEATED_EVENTS = 3
TIME_WINDOW_MINUTES = 10


def check_rules_and_create_alerts(db, events: list[dict]) -> list[Alert]:
    """Apply detection rules on incoming events and create alerts if triggered."""
    alerts_created: list[Alert] = []
    now = datetime.now(timezone.utc)

    for event in events:
        source_ip = event.get("source_ip")
        event_type = event.get("event_type", "unknown")
        severity = event.get("severity", "low")

        if not source_ip:
            continue

        if _is_suspicious_event_type(event_type):
            alert = _create_alert(
                db,
                title=f"Activité suspecte détectée : {event_type}",
                severity=_escalate_severity(severity),
                source_ip=source_ip,
                description=f"Événement suspect détecté : {event_type} depuis {source_ip}. {event.get('message', '')}",
            )
            if alert:
                alerts_created.append(alert)
        else:
            repeated = _count_similar_events(db, source_ip, event_type, TIME_WINDOW_MINUTES)
            if repeated >= THRESHOLD_REPEATED_EVENTS:
                alert = _create_alert(
                    db,
                    title=f"Comportement répété détecté : {event_type}",
                    severity=_escalate_severity(severity),
                    source_ip=source_ip,
                    description=f"{repeated} événements similaires ({event_type}) détectés depuis {source_ip} en {TIME_WINDOW_MINUTES} minutes.",
                )
                if alert:
                    alerts_created.append(alert)

    return alerts_created


def _is_suspicious_event_type(event_type: str) -> bool:
    suspicious = {"port_scan", "failed_login", "brute_force", "unauthorized_access", "malware", "data_exfil"}
    return event_type.lower() in suspicious


def _escalate_severity(severity: str) -> str:
    if severity == "low":
        return "medium"
    if severity == "medium":
        return "high"
    return "critical"


def _create_alert(db, title: str, severity: str, source_ip: str, description: str) -> Alert | None:
    from app.alerts.service import create_alert

    recent = (
        db.query(Alert)
        .filter(
            Alert.title == title,
            Alert.source_ip == source_ip,
            Alert.created_at > datetime.now(timezone.utc) - timedelta(minutes=5),
        )
        .first()
    )
    if recent:
        return None

    return create_alert(
        db,
        title=title,
        severity=severity,
        source_ip=source_ip,
        description=description,
    )


def _count_similar_events(db, source_ip: str, event_type: str, window_minutes: int) -> int:
    cutoff = datetime.now(timezone.utc) - timedelta(minutes=window_minutes)
    from app.telemetry.service import events_store
    count = sum(
        1
        for e in events_store
        if e.get("source_ip") == source_ip
        and e.get("event_type") == event_type
        and e.get("timestamp", cutoff) > cutoff
    )
    return count
