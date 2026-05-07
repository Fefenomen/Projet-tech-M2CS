from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.router import get_current_active_user
from app.dashboard.schemas import DashboardResponse
from app.dashboard import service as dashboard_service
from app.core.database import get_db


router = APIRouter()


@router.get("/", response_model=DashboardResponse)
async def get_dashboard(
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_active_user),
):
    metrics = dashboard_service.get_dashboard_metrics(db)
    return DashboardResponse(
        metrics=metrics,
        recent_alerts=metrics["recent_alerts"],
    )
