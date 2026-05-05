from pydantic import BaseModel, Field
from datetime import datetime


class HeartbeatRequest(BaseModel):
    hostname: str
    timestamp: datetime | None = None
    status: str = "up"
    version: str | None = None


class HeartbeatResponse(BaseModel):
    id: str
    hostname: str
    timestamp: datetime
    status: str
    version: str | None = None
    message: str = "Heartbeat received"
