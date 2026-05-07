from pydantic import BaseModel
from datetime import datetime


class AuditLogItemResponse(BaseModel):
    id: int
    user_id: int | None = None
    role: str | None = None
    action: str
    target_type: str | None = None
    result: str
    created_at: datetime


class AuditLogListResponse(BaseModel):
    logs: list[AuditLogItemResponse]
    total: int
