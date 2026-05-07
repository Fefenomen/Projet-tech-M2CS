from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.auth.router import get_current_active_user
from app.traffic.schemas import TrafficCaptureRequest, TrafficCaptureResponse, TrafficListResponse
from app.traffic import service as traffic_service
from app.core.database import get_db

router = APIRouter()


@router.post("/", response_model=TrafficCaptureResponse, status_code=201)
async def create_capture(
    data: TrafficCaptureRequest,
    current_user: dict = Depends(get_current_active_user),
):
    return await traffic_service.capture_traffic(data)


@router.get("/", response_model=TrafficListResponse)
async def list_captures(
    source_ip: str | None = Query(None),
    protocol: str | None = Query(None),
    limit: int = Query(100, le=500),
    current_user: dict = Depends(get_current_active_user),
):
    captures = await traffic_service.get_traffic_captures(source_ip=source_ip, protocol=protocol, limit=limit)
    return TrafficListResponse(captures=captures, total=len(captures))
