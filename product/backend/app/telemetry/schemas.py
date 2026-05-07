from pydantic import BaseModel, Field
from datetime import datetime


class HeartbeatRequest(BaseModel):
    hostname: str
    timestamp: datetime | None = None
    status: str = "up"
    version: str | None = None
    ip_address: str | None = None
    agent_version: str | None = None


class HeartbeatResponse(BaseModel):
    id: str
    hostname: str
    timestamp: datetime
    status: str
    version: str | None = None
    message: str = "Heartbeat received"


class TelemetryEvent(BaseModel):
    event_type: str = "unknown"
    source_ip: str | None = None
    target_ip: str | None = None
    message: str = ""
    severity: str = "low"
    timestamp: datetime | None = None


class TelemetryEventsRequest(BaseModel):
    hostname: str
    events: list[TelemetryEvent]


class TelemetryEventsResponse(BaseModel):
    received: int
    processed: int
    message: str = "Events processed"
