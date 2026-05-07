import socket
import time
from typing import Any

from app.discovery.schemas import ip_range_to_list, PortScanResult

WELL_KNOWN_SERVICES = {
    21: "ftp", 22: "ssh", 23: "telnet", 25: "smtp", 53: "dns",
    80: "http", 110: "pop3", 143: "imap", 443: "https", 993: "imaps",
    995: "pop3s", 3306: "mysql", 3389: "rdp", 5432: "postgresql",
    8080: "http-proxy", 8443: "https-alt",
}


def scan_port(ip: str, port: int, timeout: float = 0.5) -> PortScanResult:
    """Scan a single port on a target IP using TCP connect."""
    result = PortScanResult(ip=ip, port=port)
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            conn_result = s.connect_ex((ip, port))
            if conn_result == 0:
                result.state = "open"
                result.service_name = WELL_KNOWN_SERVICES.get(port)
    except (socket.timeout, socket.error, OSError):
        pass
    return result


def scan_ip_range(start_ip: str, end_ip: str, ports: list[int], delay: float = 0.1) -> list[dict[str, Any]]:
    """Scan an IP range for open ports. Returns list of asset findings."""
    ip_list = ip_range_to_list(start_ip, end_ip)
    assets: dict[str, dict[str, Any]] = {}

    for ip in ip_list:
        for port in ports:
            result = scan_port(ip, port)
            if result.state == "open":
                if ip not in assets:
                    assets[ip] = {"ip": ip, "ports": [], "services": []}
                assets[ip]["ports"].append(result.port)
                if result.service_name:
                    assets[ip]["services"].append(result.service_name)
            time.sleep(delay)

    return list(assets.values())
