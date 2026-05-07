from pydantic import BaseModel
from datetime import datetime


class DashboardMetrics(BaseModel):
    total_alerts: int
    alerts_by_status: dict
    alerts_by_severity: dict
    total_assets: int
    assets_by_status: dict
    total_audit_logs: int
    recent_alerts: list[dict]
    total_exports: int


class AlertSummary(BaseModel):
    id: int
    title: str
    severity: str
    status: str
    source_ip: str | None
    created_at: datetime


class DashboardResponse(BaseModel):
    metrics: DashboardMetrics
    recent_alerts: list[AlertSummary]
