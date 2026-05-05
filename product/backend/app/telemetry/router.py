from fastapi import APIRouter, Depends

from app.auth.router import get_current_active_user
from app.telemetry.schemas import HeartbeatRequest, HeartbeatResponse
from app.telemetry import service as telemetry_service

router = APIRouter(dependencies=[Depends(get_current_active_user)])


@router.post("/heartbeat", response_model=HeartbeatResponse)
async def create_heartbeat(data: HeartbeatRequest):
    return await telemetry_service.process_heartbeat(data)


@router.get("/heartbeats")
async def list_heartbeats():
    return await telemetry_service.get_heartbeats()
