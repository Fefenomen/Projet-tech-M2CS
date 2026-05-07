"""API v2 — Routes avec pagination, filtering, sorting."""

import math
from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.auth.router import get_current_active_user
from app.core.database import get_db
from app.models.alert import Alert
from app.models.asset import Asset
from app.models.audit_log import AuditLog
from app.telemetry.service import events_store

from .schemas import (
    PaginatedResponse,
    AlertItem,
    AssetItem,
    EventItem,
    AuditLogItem,
)


router = APIRouter(tags=["API v2"])


def paginate(items: list, page: int, page_size: int) -> dict:
    total = len(items)
    total_pages = max(1, math.ceil(total / page_size))
    start = (page - 1) * page_size
    end = start + page_size
    return {
        "items": items[start:end],
        "total": total,
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages,
    }


@router.get("/alerts", response_model=PaginatedResponse[AlertItem])
async def list_alerts_v2(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    status: Optional[str] = Query(None),
    severity: Optional[str] = Query(None),
    source_ip: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_active_user),
):
    """List alerts with pagination and filtering.

    - **page**: Page number (1-based)
    - **page_size**: Items per page (1-100)
    - **status**: Filter by status (nouvelle, en cours, cloturee)
    - **severity**: Filter by severity (low, medium, high, critical)
    - **source_ip**: Filter by source IP
    """
    query = db.query(Alert)
    if status:
        query = query.filter(Alert.status == status)
    if severity:
        query = query.filter(Alert.severity == severity)
    if source_ip:
        query = query.filter(Alert.source_ip == source_ip)

    query = query.order_by(Alert.created_at.desc())
    alerts = query.all()

    items = [
        AlertItem(
            id=a.id,
            title=a.title,
            severity=a.severity,
            status=a.status,
            source_ip=a.source_ip,
            description=a.description,
            created_at=a.created_at,
            updated_at=getattr(a, "updated_at", None),
        )
        for a in alerts
    ]

    return paginate(items, page, page_size)


@router.get("/assets", response_model=PaginatedResponse[AssetItem])
async def list_assets_v2(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    status: Optional[str] = Query(None),
    ip_address: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_active_user),
):
    """List assets with pagination and filtering.

    - **page**: Page number (1-based)
    - **page_size**: Items per page (1-100)
    - **status**: Filter by status (active, inactive)
    - **ip_address**: Filter by IP address
    """
    query = db.query(Asset)
    if status:
        query = query.filter(Asset.status == status)
    if ip_address:
        query = query.filter(Asset.ip_address == ip_address)

    query = query.order_by(Asset.last_seen_at.desc())
    assets = query.all()

    items = [
        AssetItem(
            id=a.id,
            ip_address=a.ip_address,
            hostname=a.hostname,
            status=a.status,
            first_seen_at=a.first_seen_at,
            last_seen_at=a.last_seen_at,
        )
        for a in assets
    ]

    return paginate(items, page, page_size)


@router.get("/events", response_model=PaginatedResponse[EventItem])
async def list_events_v2(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    event_type: Optional[str] = Query(None),
    source_ip: Optional[str] = Query(None),
    severity: Optional[str] = Query(None),
    current_user: dict = Depends(get_current_active_user),
):
    """List events with pagination and filtering.

    - **page**: Page number (1-based)
    - **page_size**: Items per page (1-100)
    - **event_type**: Filter by event type
    - **source_ip**: Filter by source IP
    - **severity**: Filter by severity
    """
    events = list(events_store)

    if event_type:
        events = [e for e in events if e.get("event_type") == event_type]
    if source_ip:
        events = [e for e in events if e.get("source_ip") == source_ip]
    if severity:
        events = [e for e in events if e.get("severity") == severity]

    events = sorted(events, key=lambda x: x.get("timestamp", ""), reverse=True)

    items = [
        EventItem(
            id=e.get("id", ""),
            hostname=e.get("hostname", ""),
            event_type=e.get("event_type", ""),
            source_ip=e.get("source_ip", ""),
            target_ip=e.get("target_ip"),
            message=e.get("message", ""),
            severity=e.get("severity", ""),
            timestamp=e.get("timestamp", ""),
        )
        for e in events
    ]

    return paginate(items, page, page_size)


@router.get("/audit-logs", response_model=PaginatedResponse[AuditLogItem])
async def list_audit_logs_v2(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    action: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_active_user),
):
    """List audit logs with pagination and filtering.

    - **page**: Page number (1-based)
    - **page_size**: Items per page (1-100)
    - **action**: Filter by action type
    """
    query = db.query(AuditLog)
    if action:
        query = query.filter(AuditLog.action == action)

    query = query.order_by(AuditLog.created_at.desc())
    logs = query.all()

    items = [
        AuditLogItem(
            id=l.id,
            user_id=l.user_id,
            role=l.role,
            action=l.action,
            target_type=l.target_type,
            result=l.result,
            created_at=l.created_at,
        )
        for l in logs
    ]

    return paginate(items, page, page_size)
