from pydantic import BaseModel, field_validator
from datetime import datetime


VALID_SEVERITIES = {"low", "medium", "high", "critical"}
VALID_STATUSES = {"nouvelle", "en cours", "cloturee"}


class AlertCreate(BaseModel):
    title: str
    severity: str = "medium"
    source_ip: str | None = None
    description: str | None = None
    asset_id: int | None = None

    @field_validator("severity")
    @classmethod
    def validate_severity(cls, v: str) -> str:
        v = v.lower()
        if v not in VALID_SEVERITIES:
            raise ValueError(f"Severity must be one of {VALID_SEVERITIES}, got '{v}'")
        return v


class AlertResponse(BaseModel):
    id: int
    title: str
    severity: str
    status: str
    source_ip: str | None = None
    description: str | None = None
    asset_id: int | None = None
    created_at: datetime
    updated_at: datetime


class AlertListResponse(BaseModel):
    alerts: list[AlertResponse]
    total: int
    by_severity: dict[str, int]
    by_status: dict[str, int]


class AlertStatusUpdate(BaseModel):
    status: str

    @field_validator("status")
    @classmethod
    def validate_status(cls, v: str) -> str:
        v = v.lower()
        if v not in VALID_STATUSES:
            raise ValueError(f"Status must be one of {VALID_STATUSES}, got '{v}'")
        return v


class RuleDefinition(BaseModel):
    name: str
    description: str
    condition: str
    severity: str = "medium"
