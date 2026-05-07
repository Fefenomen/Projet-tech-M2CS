"""API v2 — Schemas avec pagination et filtering."""

from typing import Optional, Generic, TypeVar
from datetime import datetime
from pydantic import BaseModel, Field


T = TypeVar("T")


class PaginatedResponse(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int
    page_size: int
    total_pages: int


class AlertItem(BaseModel):
    id: int
    title: str
    severity: str
    status: str
    source_ip: Optional[str] = None
    description: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None


class AssetItem(BaseModel):
    id: int
    ip_address: str
    hostname: Optional[str] = None
    status: str
    first_seen_at: datetime
    last_seen_at: datetime


class EventItem(BaseModel):
    id: str
    hostname: str
    event_type: str
    source_ip: str
    target_ip: Optional[str] = None
    message: str
    severity: str
    timestamp: datetime


class AuditLogItem(BaseModel):
    id: int
    user_id: Optional[int] = None
    role: str
    action: str
    target_type: Optional[str] = None
    result: str
    created_at: datetime


class ComplianceItemV2(BaseModel):
    id: str
    title: str
    description: str
    status: str
    evidence: Optional[str] = None
    recommendation: Optional[str] = None


class ComplianceResponseV2(BaseModel):
    score: dict
    requirements: list[ComplianceItemV2]
    last_updated: datetime


class RiskScoreResponse(BaseModel):
    asset_id: int
    ip_address: str
    risk_score: int
    risk_level: str
    factors: list[dict]
