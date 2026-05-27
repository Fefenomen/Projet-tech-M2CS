import re
from pydantic import BaseModel, field_validator


IPV4_REGEX = re.compile(
    r"^(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$"
)


def validate_ipv4(ip: str) -> bool:
    return bool(IPV4_REGEX.match(ip))


def ip_range_to_list(start_ip: str, end_ip: str) -> list[str]:
    """Generate a list of IPs between start and end (inclusive)."""
    def ip_to_int(ip: str) -> int:
        parts = ip.split(".")
        return (int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3])

    def int_to_ip(num: int) -> str:
        return f"{(num >> 24) & 0xFF}.{(num >> 16) & 0xFF}.{(num >> 8) & 0xFF}.{num & 0xFF}"

    start = ip_to_int(start_ip)
    end = ip_to_int(end_ip)
    return [int_to_ip(i) for i in range(start, end + 1)]


class ScanRequest(BaseModel):
    start_ip: str
    end_ip: str
    ports: list[int] = [22, 80, 443, 3306, 5432, 8080]
    delay: float = 0.0

    @field_validator("start_ip", "end_ip")
    @classmethod
    def validate_ip_format(cls, v: str) -> str:
        if not validate_ipv4(v):
            raise ValueError(f"Invalid IPv4 address: {v}")
        return v


class ScanResponse(BaseModel):
    scan_id: str
    start_ip: str
    end_ip: str
    status: str = "completed"
    assets_found: int = 0
    ports_scanned: int = 0
    duration_seconds: float = 0.0


class PortScanResult(BaseModel):
    ip: str
    port: int
    protocol: str = "tcp"
    state: str = "closed"
    service_name: str | None = None
