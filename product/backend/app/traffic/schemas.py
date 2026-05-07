from pydantic import BaseModel, field_validator
from datetime import datetime


class TrafficCaptureRequest(BaseModel):
    hostname: str
    source_ip: str
    target_ip: str
    source_port: int
    target_port: int
    protocol: str = "tcp"
    payload_summary: str = ""
    timestamp: datetime | None = None

    @field_validator("protocol")
    @classmethod
    def validate_protocol(cls, v: str) -> str:
        v = v.lower()
        if v not in {"tcp", "udp", "icmp", "http", "dns"}:
            raise ValueError(f"Protocol must be one of tcp, udp, icmp, http, dns")
        return v


class TrafficCaptureResponse(BaseModel):
    id: str
    hostname: str
    source_ip: str
    target_ip: str
    source_port: int
    target_port: int
    protocol: str
    payload_summary: str
    timestamp: datetime


class TrafficListResponse(BaseModel):
    captures: list[TrafficCaptureResponse]
    total: int
