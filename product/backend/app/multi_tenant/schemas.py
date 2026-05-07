"""Multi-tenant — Schemas."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class TenantCreate(BaseModel):
    name: str
    description: str = ""


class TenantResponse(BaseModel):
    id: int
    name: str
    description: str
    created_by: str
    created_at: datetime
    is_active: bool


class TenantListResponse(BaseModel):
    tenants: list[TenantResponse]
    total: int
