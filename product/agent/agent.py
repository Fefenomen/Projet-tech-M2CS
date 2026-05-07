#!/usr/bin/env python3
"""BigBrowser Endpoint Agent — Heartbeat & Events collector."""

import os
import socket
import time
import logging
from datetime import datetime, timezone

import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s [AGENT] %(levelname)s %(message)s")
logger = logging.getLogger("agent")

SOC_URL = os.getenv("SOC_URL", "http://soc:8000")
AGENT_USERNAME = "agent"
AGENT_PASSWORD = os.getenv("AGENT_SECRET", "agent_secret_mvp")
ENDPOINT_NAME = os.getenv("ENDPOINT_NAME", socket.gethostname())
HEARTBEAT_INTERVAL = int(os.getenv("HEARTBEAT_INTERVAL", "30"))


def get_ip() -> str:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def register_agent() -> str | None:
    """Authenticate with the SOC and get a token."""
    try:
        resp = requests.post(
            f"{SOC_URL}/api/v1/auth/login",
            json={"username": AGENT_USERNAME, "password": AGENT_PASSWORD},
            timeout=5,
        )
        if resp.status_code == 200:
            return resp.json()["access_token"]
        logger.warning("Agent auth failed: %s", resp.status_code)
    except Exception as e:
        logger.error("Cannot reach SOC: %s", e)
    return None


def send_heartbeat(token: str) -> bool:
    """Send heartbeat to the SOC."""
    try:
        resp = requests.post(
            f"{SOC_URL}/api/v1/telemetry/heartbeat",
            json={
                "hostname": ENDPOINT_NAME,
                "ip_address": get_ip(),
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "agent_version": "1.0.0",
                "status": "active",
            },
            headers={"Authorization": f"Bearer {token}"},
            timeout=5,
        )
        if resp.status_code in (200, 201):
            logger.info("Heartbeat sent")
            return True
        logger.warning("Heartbeat rejected: %s", resp.status_code)
    except Exception as e:
        logger.error("Heartbeat error: %s", e)
    return False


def send_events(token: str, events: list[dict]) -> bool:
    """Send collected events to the SOC."""
    if not events:
        return True
    try:
        resp = requests.post(
            f"{SOC_URL}/api/v1/telemetry/events",
            json={"hostname": ENDPOINT_NAME, "events": events},
            headers={"Authorization": f"Bearer {token}"},
            timeout=5,
        )
        if resp.status_code in (200, 201):
            logger.info("Sent %d events", len(events))
            return True
        logger.warning("Events rejected: %s", resp.status_code)
    except Exception as e:
        logger.error("Events error: %s", e)
    return False


def collect_local_events() -> list[dict]:
    """Collect local events (simulated for demo: connections, logs)."""
    events = []
    try:
        with open("/var/log/nginx/access.log") as f:
            for line in f.readlines()[-10:]:
                parts = line.split()
                if len(parts) >= 7:
                    events.append({
                        "event_type": "http_request",
                        "source_ip": parts[0],
                        "message": f"HTTP {parts[5]} {parts[6]}",
                        "severity": "low",
                    })
    except FileNotFoundError:
        pass

    try:
        with open("/var/log/nginx/error.log") as f:
            for line in f.readlines()[-5:]:
                events.append({
                    "event_type": "error",
                    "source_ip": get_ip(),
                    "message": line.strip()[:200],
                    "severity": "medium",
                })
    except FileNotFoundError:
        pass

    return events


def main():
    logger.info("BigBrowser Agent starting on %s", ENDPOINT_NAME)
    logger.info("SOC URL: %s", SOC_URL)

    token = None
    consecutive_errors = 0

    while True:
        try:
            if not token:
                logger.info("Authenticating with SOC...")
                token = register_agent()
                if not token:
                    consecutive_errors += 1
                    time.sleep(min(HEARTBEAT_INTERVAL * consecutive_errors, 300))
                    continue

            consecutive_errors = 0
            send_heartbeat(token)

            events = collect_local_events()
            if events:
                send_events(token, events)

        except Exception as e:
            logger.error("Unexpected error: %s", e)
            token = None
            consecutive_errors += 1

        time.sleep(HEARTBEAT_INTERVAL)


if __name__ == "__main__":
    main()
