from fastapi import APIRouter, Depends, status

from app.auth.router import get_current_active_user
from app.telemetry.schemas import (
    HeartbeatRequest, HeartbeatResponse,
    TelemetryEventsRequest, TelemetryEventsResponse,
)
from app.telemetry import service as telemetry_service

router = APIRouter(dependencies=[Depends(get_current_active_user)])


@router.post("/heartbeat", response_model=HeartbeatResponse)
async def create_heartbeat(data: HeartbeatRequest):
    return await telemetry_service.process_heartbeat(data)


@router.get("/heartbeats")
async def list_heartbeats():
    return await telemetry_service.get_heartbeats()


@router.post("/events", response_model=TelemetryEventsResponse, status_code=status.HTTP_201_CREATED)
async def create_events(data: TelemetryEventsRequest):
    return await telemetry_service.process_events(data)


@router.get("/events")
async def list_events():
    return await telemetry_service.get_events()
