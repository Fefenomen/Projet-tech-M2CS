from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.auth.router import get_current_active_user
from app.reports.schemas import ExportRequest, ExportResponse
from app.reports import service as report_service
from app.core.database import get_db
from app.models.audit_log import AuditLog
from app.models.alert import Alert
from app.models.asset import Asset
from app.telemetry.service import events_store
from sqlalchemy import func


router = APIRouter()


def _log_export(db: Session, role: str, scope: str, fmt: str):
    db.add(AuditLog(
        user_id=None,
        role=role,
        action="export_data",
        target_type=scope,
        result=f"export_{fmt}",
    ))
    db.commit()


@router.post("/", response_model=ExportResponse, status_code=status.HTTP_201_CREATED)
async def create_export(
    export_req: ExportRequest,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_active_user),
):
    record = report_service.generate_export(
        db,
        fmt=export_req.format,
        scope=export_req.scope,
        requested_by=current_user["username"],
    )

    _log_export(db, current_user.get("role"), export_req.scope, export_req.format)

    return ExportResponse(
        id=record.id,
        format=record.format,
        requested_by=record.requested_by,
        scope=record.scope,
        file_path=record.file_path,
        created_at=record.created_at,
        row_count=record.row_count,
    )


@router.get("/{export_id}/download")
async def download_export(
    export_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_active_user),
):
    record = db.query(report_service.ExportRecord).filter(
        report_service.ExportRecord.id == export_id
    ).first()
    if not record:
        raise HTTPException(status_code=404, detail="Export not found")

    import os
    if not os.path.exists(record.file_path):
        raise HTTPException(status_code=404, detail="Export file no longer available")

    media_type = "text/csv" if record.format == "csv" else "application/json"
    return FileResponse(
        path=record.file_path,
        filename=os.path.basename(record.file_path),
        media_type=media_type,
    )


@router.get("/summary")
async def get_reports_summary(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_active_user),
):
    """Get KPI summary for reports dashboard."""
    total_assets = db.query(func.count(Asset.id)).scalar() or 0
    total_alerts = db.query(func.count(Alert.id)).scalar() or 0
    total_events = len(events_store)
    critical_alerts = db.query(func.count(Alert.id)).filter(Alert.severity == "critical").scalar() or 0
    high_alerts = db.query(func.count(Alert.id)).filter(Alert.severity == "high").scalar() or 0
    open_alerts = db.query(func.count(Alert.id)).filter(Alert.status == "new").scalar() or 0

    return {
        "total_assets": total_assets,
        "total_alerts": total_alerts,
        "total_events": total_events,
        "critical_alerts": critical_alerts,
        "high_alerts": high_alerts,
        "open_alerts": open_alerts,
    }
