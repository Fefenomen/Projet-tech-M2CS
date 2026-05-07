from pydantic import BaseModel, field_validator
from datetime import datetime


VALID_FORMATS = {"csv", "json"}
VALID_SCOPES = {"alerts", "assets", "audit_logs"}


class ExportRequest(BaseModel):
    format: str
    scope: str = "alerts"

    @field_validator("format")
    @classmethod
    def validate_format(cls, v: str) -> str:
        v = v.lower()
        if v not in VALID_FORMATS:
            raise ValueError(f"Format must be one of {VALID_FORMATS}")
        return v

    @field_validator("scope")
    @classmethod
    def validate_scope(cls, v: str) -> str:
        v = v.lower()
        if v not in VALID_SCOPES:
            raise ValueError(f"Scope must be one of {VALID_SCOPES}")
        return v


class ExportResponse(BaseModel):
    id: int
    format: str
    requested_by: str
    scope: str
    file_path: str
    created_at: datetime
    row_count: int


class AuditLogResponse(BaseModel):
    id: int
    user_id: int | None = None
    role: str | None = None
    action: str
    target_type: str | None = None
    result: str
    created_at: datetime
