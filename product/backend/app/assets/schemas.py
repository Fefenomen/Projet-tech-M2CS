from pydantic import BaseModel
from datetime import datetime


class PortResponse(BaseModel):
    id: int
    port: int
    protocol: str
    state: str
    service_name: str | None = None
    observed_at: datetime


class AssetResponse(BaseModel):
    id: int
    ip_address: str
    hostname: str | None = None
    first_seen_at: datetime
    last_seen_at: datetime
    status: str


class AssetDetailResponse(AssetResponse):
    ports: list[PortResponse] = []


class AssetListResponse(BaseModel):
    assets: list[AssetResponse]
    total: int
