from datetime import datetime, timezone
from typing import Any

from app.telemetry.schemas import HeartbeatRequest, HeartbeatResponse
from app.telemetry.schemas import TelemetryEventsRequest, TelemetryEventsResponse

# In-memory store for MVP (replace with DB later)
heartbeats: list[dict[str, Any]] = []
events_store: list[dict[str, Any]] = []


async def process_heartbeat(data: HeartbeatRequest) -> HeartbeatResponse:
    heartbeat = {
        "id": str(len(heartbeats) + 1),
        "hostname": data.hostname,
        "timestamp": data.timestamp or datetime.now(timezone.utc),
        "status": data.status,
        "version": data.version,
        "ip_address": data.ip_address,
        "agent_version": data.agent_version,
    }
    heartbeats.append(heartbeat)
    return HeartbeatResponse(**heartbeat)


async def get_heartbeats() -> list[dict[str, Any]]:
    return heartbeats


async def process_events(data: TelemetryEventsRequest) -> TelemetryEventsResponse:
    now = datetime.now(timezone.utc)
    processed = 0
    for event in data.events:
        record = {
            "id": str(len(events_store) + 1),
            "hostname": data.hostname,
            "event_type": event.event_type,
            "source_ip": event.source_ip,
            "target_ip": event.target_ip,
            "message": event.message,
            "severity": event.severity,
            "timestamp": event.timestamp or now,
            "created_at": now,
        }
        events_store.append(record)
        processed += 1
    return TelemetryEventsResponse(received=len(data.events), processed=processed)


async def get_events() -> list[dict[str, Any]]:
    return events_store
