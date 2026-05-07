"""Risk Scoring — business logic for asset risk assessment."""

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.alert import Alert
from app.models.asset import Asset
from app.models.port import Port
from app.telemetry.service import events_store


def compute_asset_risk_score(db: Session, asset: Asset) -> dict:
    """Compute a risk score (0-100) for an asset based on multiple factors.

    Factors:
    - Open ports count (more ports = higher risk)
    - Critical services exposed (SSH, RDP, etc.)
    - Alert count associated with the asset
    - Event severity distribution
    - Asset age (older without updates = higher risk)

    Returns dict with score (0-100), level (low/medium/high/critical), and factors.
    """
    factors = []
    score = 0

    # Factor 1: Open ports count
    port_count = db.query(func.count(Port.id)).filter(Port.asset_id == asset.id).scalar() or 0
    if port_count > 10:
        score += 25
        factors.append({"name": "open_ports", "value": port_count, "impact": 25, "detail": "Many open ports (>10)"})
    elif port_count > 5:
        score += 15
        factors.append({"name": "open_ports", "value": port_count, "impact": 15, "detail": "Several open ports (5-10)"})
    elif port_count > 0:
        score += 5
        factors.append({"name": "open_ports", "value": port_count, "impact": 5, "detail": "Few open ports (<5)"})

    # Factor 2: Critical services exposed
    critical_ports = db.query(Port).filter(
        Port.asset_id == asset.id,
        Port.port.in_([22, 23, 3389, 445, 1433, 3306, 5432]),
    ).all()
    if critical_ports:
        critical_count = len(critical_ports)
        critical_score = min(critical_count * 10, 30)
        score += critical_score
        factors.append({
            "name": "critical_services",
            "value": critical_count,
            "impact": critical_score,
            "detail": f"Critical services: {', '.join(str(p.port) for p in critical_ports)}",
        })

    # Factor 3: Alert count
    alert_count = db.query(func.count(Alert.id)).filter(Alert.source_ip == asset.ip_address).scalar() or 0
    if alert_count > 5:
        score += 25
        factors.append({"name": "alerts", "value": alert_count, "impact": 25, "detail": "High alert volume"})
    elif alert_count > 0:
        score += 10
        factors.append({"name": "alerts", "value": alert_count, "impact": 10, "detail": "Some alerts detected"})

    # Factor 4: Event severity
    high_events = sum(
        1 for e in events_store
        if e.get("source_ip") == asset.ip_address
        and e.get("severity") in ("high", "critical")
    )
    if high_events > 3:
        score += 20
        factors.append({"name": "high_severity_events", "value": high_events, "impact": 20, "detail": "Multiple high-severity events"})
    elif high_events > 0:
        score += 10
        factors.append({"name": "high_severity_events", "value": high_events, "impact": 10, "detail": "Some high-severity events"})

    # Cap score at 100
    score = min(score, 100)

    # Determine risk level
    if score >= 75:
        level = "critical"
    elif score >= 50:
        level = "high"
    elif score >= 25:
        level = "medium"
    else:
        level = "low"

    return {"score": score, "level": level, "factors": factors}
