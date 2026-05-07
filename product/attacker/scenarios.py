#!/usr/bin/env python3
"""BigBrowser Attacker — Controlled offensive scenarios for demo."""

import os
import socket
import time
import logging
from datetime import datetime, timezone

import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s [ATTACKER] %(levelname)s %(message)s")
logger = logging.getLogger("attacker")

TARGET_SUBNET = os.getenv("TARGET_SUBNET", "172.20.0.20-172.20.0.21")
SCENARIO_DELAY = int(os.getenv("SCENARIO_DELAY", "30"))
SOC_URL = os.getenv("SOC_URL", "http://soc:8000")


def parse_target_range(net_range: str) -> list[str]:
    if "-" in net_range:
        start, end = net_range.split("-", 1)
        parts = start.split(".")
        start_last = int(parts[3])
        end_last = int(end.split(".")[3])
        prefix = ".".join(parts[:3])
        return [f"{prefix}.{i}" for i in range(start_last, end_last + 1)]
    return [net_range]


def scenario_port_scan(targets: list[str], ports: list[int] = [22, 80, 443, 8080, 3306]):
    """Simulate a port scan against target hosts."""
    logger.info("=== SCENARIO: Port Scan ===")
    for target in targets:
        for port in ports:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                result = s.connect_ex((target, port))
                if result == 0:
                    logger.info("  Port %d OPEN on %s", port, target)
                s.close()
            except Exception:
                pass
            time.sleep(0.1)
    logger.info("Port scan complete")


def scenario_http_flood(target: str, count: int = 20):
    """Simulate repeated HTTP requests (potential brute force / DoS)."""
    logger.info("=== SCENARIO: HTTP Flood on %s ===", target)
    for i in range(count):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, 80))
            s.sendall(f"GET /admin HTTP/1.1\r\nHost: {target}\r\n\r\n".encode())
            s.recv(4096)
            s.close()
            logger.info("  Request %d/%d sent", i + 1, count)
        except Exception as e:
            logger.debug("  Request %d failed: %s", i + 1, e)
        time.sleep(0.5)
    logger.info("HTTP flood complete")


def scenario_failed_logins(target: str, count: int = 5):
    """Simulate repeated failed login attempts."""
    logger.info("=== SCENARIO: Failed Logins on %s ===", target)
    for i in range(count):
        try:
            payload = f'POST /login HTTP/1.1\r\nHost: {target}\r\nContent-Length: 50\r\n\r\nusername=admin&password=wrong_pass_{i}'
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, 80))
            s.sendall(payload.encode())
            s.recv(4096)
            s.close()
            logger.info("  Failed login attempt %d/%d", i + 1, count)
        except Exception as e:
            logger.debug("  Login attempt %d failed: %s", i + 1, e)
        time.sleep(0.3)
    logger.info("Failed logins complete")


def scenario_suspicious_traffic(target: str, count: int = 10):
    """Simulate suspicious traffic patterns for detection rules."""
    logger.info("=== SCENARIO: Suspicious Traffic to %s ===", target)

    # Rapid connections to multiple ports
    for i in range(count):
        for port in [22, 23, 80, 443, 8080, 3306, 5432, 6379]:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                s.connect((target, port))
                s.close()
            except Exception:
                pass
        logger.info("  Sweep cycle %d/%d complete", i + 1, count)
        time.sleep(0.2)

    logger.info("Suspicious traffic complete")


def main():
    logger.info("BigBrowser Attacker starting")
    targets = parse_target_range(TARGET_SUBNET)
    logger.info("Targets: %s", targets)

    # Wait for targets to be ready
    time.sleep(5)

    # Run scenarios once, then repeat if configured
    iteration = 0
    while True:
        iteration += 1
        logger.info("--- Attack Iteration %d ---", iteration)

        for target in targets:
            logger.info("Target: %s", target)
            scenario_port_scan([target])
            time.sleep(2)

            scenario_http_flood(target)
            time.sleep(2)

            scenario_failed_logins(target)
            time.sleep(2)

            scenario_suspicious_traffic(target)
            time.sleep(2)

        logger.info("All scenarios complete for iteration %d", iteration)
        logger.info("Waiting %d seconds before next iteration...", SCENARIO_DELAY)
        time.sleep(SCENARIO_DELAY)


if __name__ == "__main__":
    main()
