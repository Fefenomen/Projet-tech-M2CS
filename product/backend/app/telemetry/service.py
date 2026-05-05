from datetime import datetime
from typing import Any

from app.telemetry.schemas import HeartbeatRequest, HeartbeatResponse

# In-memory store for MVP (replace with DB later)
heartbeats: list[dict[str, Any]] = []


async def process_heartbeat(data: HeartbeatRequest) -> HeartbeatResponse:
    heartbeat = {
        "id": str(len(heartbeats) + 1),
        "hostname": data.hostname,
        "timestamp": data.timestamp or datetime.utcnow(),
        "status": data.status,
        "version": data.version,
    }
    heartbeats.append(heartbeat)
    return HeartbeatResponse(**heartbeat)


async def get_heartbeats() -> list[dict[str, Any]]:
    return heartbeats
