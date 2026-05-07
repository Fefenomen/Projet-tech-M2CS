from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.router import get_current_active_user
from app.alerts.schemas import AlertCreate, AlertResponse, AlertListResponse, AlertStatusUpdate
from app.alerts import service as alert_service
from app.core.database import get_db
from app.models.asset import Asset


router = APIRouter()


@router.get("/", response_model=AlertListResponse)
async def list_alerts(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_active_user),
):
    alerts = alert_service.get_all_alerts(db)
    stats = alert_service.get_alert_stats(db)

    return AlertListResponse(
        alerts=[
            AlertResponse(
                id=a.id,
                title=a.title,
                severity=a.severity,
                status=a.status,
                source_ip=a.source_ip,
                description=a.description,
                asset_id=a.asset_id,
                created_at=a.created_at,
                updated_at=a.updated_at,
            )
            for a in alerts
        ],
        total=stats["total"],
        by_severity=stats["by_severity"],
        by_status=stats["by_status"],
    )


@router.get("/{alert_id}", response_model=AlertResponse)
async def get_alert(
    alert_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_active_user),
):
    alert = alert_service.get_alert_by_id(db, alert_id)
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")

    return AlertResponse(
        id=alert.id,
        title=alert.title,
        severity=alert.severity,
        status=alert.status,
        source_ip=alert.source_ip,
        description=alert.description,
        asset_id=alert.asset_id,
        created_at=alert.created_at,
        updated_at=alert.updated_at,
    )


@router.post("/", response_model=AlertResponse, status_code=status.HTTP_201_CREATED)
async def create_alert(
    alert_data: AlertCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_active_user),
):
    if alert_data.asset_id:
        asset = db.query(Asset).filter(Asset.id == alert_data.asset_id).first()
        if not asset:
            raise HTTPException(status_code=404, detail="Asset not found")

    alert = alert_service.create_alert(
        db,
        title=alert_data.title,
        severity=alert_data.severity,
        source_ip=alert_data.source_ip,
        description=alert_data.description,
        asset_id=alert_data.asset_id,
    )

    alert_service.log_alert_action(
        db,
        user_id=None,
        role=current_user.get("role"),
        action="create_alert",
        target_type="alert",
    )

    return AlertResponse(
        id=alert.id,
        title=alert.title,
        severity=alert.severity,
        status=alert.status,
        source_ip=alert.source_ip,
        description=alert.description,
        asset_id=alert.asset_id,
        created_at=alert.created_at,
        updated_at=alert.updated_at,
    )


@router.patch("/{alert_id}", response_model=AlertResponse)
async def update_alert_status(
    alert_id: int,
    status_update: AlertStatusUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_active_user),
):
    alert = alert_service.get_alert_by_id(db, alert_id)
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")

    valid_transitions = {
        "nouvelle": ["en cours", "cloturee"],
        "en cours": ["cloturee"],
        "cloturee": [],
    }

    if status_update.status not in valid_transitions.get(alert.status, []):
        raise HTTPException(
            status_code=400,
            detail=f"Cannot transition from '{alert.status}' to '{status_update.status}'",
        )

    updated = alert_service.update_alert_status(db, alert_id, status_update.status)

    alert_service.log_alert_action(
        db,
        user_id=None,
        role=current_user.get("role"),
        action="update_alert_status",
        target_type="alert",
    )

    return AlertResponse(
        id=updated.id,
        title=updated.title,
        severity=updated.severity,
        status=updated.status,
        source_ip=updated.source_ip,
        description=updated.description,
        asset_id=updated.asset_id,
        created_at=updated.created_at,
        updated_at=updated.updated_at,
    )
