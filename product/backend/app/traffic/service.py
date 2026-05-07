from datetime import datetime, timezone
from typing import Any

from app.traffic.schemas import TrafficCaptureRequest, TrafficCaptureResponse

captures_store: list[dict[str, Any]] = []


async def capture_traffic(data: TrafficCaptureRequest) -> TrafficCaptureResponse:
    record = {
        "id": str(len(captures_store) + 1),
        "hostname": data.hostname,
        "source_ip": data.source_ip,
        "target_ip": data.target_ip,
        "source_port": data.source_port,
        "target_port": data.target_port,
        "protocol": data.protocol,
        "payload_summary": data.payload_summary,
        "timestamp": data.timestamp or datetime.now(timezone.utc),
        "created_at": datetime.now(timezone.utc),
    }
    captures_store.append(record)
    return TrafficCaptureResponse(**record)


async def get_traffic_captures(
    source_ip: str | None = None,
    protocol: str | None = None,
    limit: int = 100,
) -> list[dict[str, Any]]:
    results = captures_store
    if source_ip:
        results = [r for r in results if r.get("source_ip") == source_ip or r.get("target_ip") == source_ip]
    if protocol:
        results = [r for r in results if r.get("protocol") == protocol.lower()]
    return results[-limit:]
