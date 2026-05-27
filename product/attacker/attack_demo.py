#!/usr/bin/env python3
"""BigBrowser Attack Demo — real attacks + SOC telemetry reporting.

Exécute les mêmes scénarios que le Docker attacker (port scan, HTTP flood,
failed logins, suspicious traffic) et reporte chaque attaque au SOC via
l'API telemetry pour que les alerts apparaissent sur le dashboard.

Usage:
    python3 attack_demo.py [--soc-url http://localhost:8080]
"""

import argparse
import logging
import os
import socket
import sys
import time
from datetime import datetime, timezone

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [ATTACK] %(message)s",
)
logger = logging.getLogger("attack_demo")


def get_token(soc_url: str) -> str:
    resp = requests.post(
        f"{soc_url}/api/v1/auth/login",
        json={"username": "admin", "password": "admin123"},
        timeout=5,
    )
    resp.raise_for_status()
    return resp.json()["access_token"]


def send_events(soc_url: str, token: str, hostname: str, events: list[dict]) -> bool:
    resp = requests.post(
        f"{soc_url}/api/v1/telemetry/events",
        json={"hostname": hostname, "events": events},
        headers={"Authorization": f"Bearer {token}"},
        timeout=10,
    )
    return resp.status_code in (200, 201)


# ── Attaques réelles (copiées de scenarios.py) ──────────────

def attack_port_scan(target: str, ports: list[int]) -> list[dict]:
    """Scanne les ports ouverts et retourne les événements telemetry."""
    logger.info("━ Port scan → %s ports=%s", target, ports)
    open_ports = []
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            if s.connect_ex((target, port)) == 0:
                open_ports.append(port)
                logger.info("  ✓ Port %d OPEN", port)
            s.close()
        except Exception:
            pass
        time.sleep(0.1)

    events = []
    if open_ports:
        events.append({
            "event_type": "port_scan",
            "source_ip": "127.0.0.1",
            "target_ip": target,
            "message": f"Port scan detected: {len(open_ports)} open ports ({','.join(map(str,open_ports))})",
            "severity": "high",
        })
    return events


def attack_http_flood(target: str, port: int, path: str, count: int = 5) -> list[dict]:
    """Émet des requêtes HTTP répétées et retourne les événements."""
    logger.info("━ HTTP flood → %s:%d%s x%d", target, port, path, count)
    successes = 0
    for i in range(count):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, port))
            s.sendall(f"GET {path} HTTP/1.1\r\nHost: {target}\r\nConnection: close\r\n\r\n".encode())
            data = s.recv(4096)
            s.close()
            successes += 1
            logger.info("  ✓ Requête %d/%d (%d bytes)", i + 1, count, len(data))
        except Exception as e:
            logger.debug("  ✗ Requête %d échouée: %s", i + 1, e)
        time.sleep(0.3)

    events = []
    if successes >= 3:
        events.append({
            "event_type": "http_flood",
            "source_ip": "127.0.0.1",
            "target_ip": target,
            "message": f"HTTP flood: {successes} requêtes vers {path} en {count} tentatives",
            "severity": "medium",
        })
        events.append({
            "event_type": "brute_force",
            "source_ip": "127.0.0.1",
            "target_ip": target,
            "message": f"Tentative d'accès répétée à {path} depuis 127.0.0.1",
            "severity": "high",
        })
    elif successes > 0:
        events.append({
            "event_type": "http_flood",
            "source_ip": "127.0.0.1",
            "target_ip": target,
            "message": f"Requêtes HTTP répétées vers {path} ({successes}成功)",
            "severity": "low",
        })
    return events


def attack_failed_logins(target: str, port: int, count: int = 5) -> list[dict]:
    """Tente des connexions HTTP avec credentials invalides."""
    logger.info("━ Failed logins → %s:%d x%d", target, port, count)
    attempts = 0
    for i in range(count):
        try:
            body = f"username=admin&password=wrong_pass_{i}"
            payload = (
                f"POST /login HTTP/1.1\r\n"
                f"Host: {target}\r\n"
                f"Content-Type: application/x-www-form-urlencoded\r\n"
                f"Content-Length: {len(body)}\r\n"
                f"Connection: close\r\n\r\n"
                f"{body}"
            )
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target, port))
            s.sendall(payload.encode())
            data = s.recv(4096)
            s.close()
            attempts += 1
            logger.info("  ✓ Tentative %d/%d", i + 1, count)
        except Exception as e:
            logger.debug("  ✗ Tentative %d échouée: %s", i + 1, e)
        time.sleep(0.2)

    events = []
    if attempts >= 3:
        events.append({
            "event_type": "failed_login",
            "source_ip": "127.0.0.1",
            "target_ip": target,
            "message": f"Tentatives de connexion échouées ({attempts} en {count} essais)",
            "severity": "critical",
        })
    elif attempts > 0:
        events.append({
            "event_type": "failed_login",
            "source_ip": "127.0.0.1",
            "target_ip": target,
            "message": f"{attempts} tentatives de connexion échouées",
            "severity": "medium",
        })
    return events


def attack_suspicious_traffic(target: str, port: int) -> list[dict]:
    """Trafic suspect: scan de ports multiples + requêtes inhabituelles."""
    logger.info("━ Suspicious traffic → %s", target)
    ports_to_test = [22, 23, 25, 53, 110, 143, 443, 3306, 5432, 6379, 8080, 8443, 9000, 27017]
    open_ports = []
    for p in ports_to_test:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            if s.connect_ex((target, p)) == 0:
                open_ports.append(p)
            s.close()
        except Exception:
            pass
        time.sleep(0.05)

    if open_ports:
        logger.info("  Ports ouverts: %s", open_ports)

    events = [
        {
            "event_type": "unauthorized_access",
            "source_ip": "127.0.0.1",
            "target_ip": target,
            "message": f"Scan de {len(ports_to_test)} ports depuis 127.0.0.1 — {len(open_ports)} ouverts",
            "severity": "high",
        },
    ]

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((target, port))
        s.sendall(
            f"GET /admin/../../etc/passwd HTTP/1.1\r\nHost: {target}\r\nConnection: close\r\n\r\n".encode()
        )
        data = s.recv(4096)
        s.close()
        events.append({
            "event_type": "malware",
            "source_ip": "127.0.0.1",
            "target_ip": target,
            "message": "Tentative d'injection path traversal: GET /admin/../../etc/passwd",
            "severity": "critical",
        })
        logger.info("  ✓ Path traversal attempt sent")
    except Exception:
        pass

    return events


# ── Main ────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="BigBrowser Attack Demo")
    parser.add_argument("--soc-url", default="http://localhost:8080", help="URL du SOC")
    parser.add_argument("--target", default="127.0.0.1", help="Cible des attaques")
    parser.add_argument("--port", type=int, default=8080, help="Port cible")
    parser.add_argument("--loop", action="store_true", help="Répéter en boucle")
    args = parser.parse_args()

    logger.info("╔══════════════════════════════════════════════╗")
    logger.info("║     BigBrowser — Attack Demo                 ║")
    logger.info("╠══════════════════════════════════════════════╣")
    logger.info("║ SOC:    %s", args.soc_url)
    logger.info("║ Target: %s:%d", args.target, args.port)
    logger.info("╚══════════════════════════════════════════════╝")

    try:
        token = get_token(args.soc_url)
        logger.info("Authentifié au SOC ✓")
    except Exception as e:
        logger.error("Impossible de s'authentifier: %s", e)
        sys.exit(1)

    iteration = 0
    while True:
        iteration += 1
        logger.info("")
        logger.info("═════ Iteration %d ═════", iteration)

        all_events = []

        # 1. Port scan
        all_events.extend(attack_port_scan(args.target, [args.port]))

        # 2. HTTP flood
        all_events.extend(attack_http_flood(args.target, args.port, "/admin"))

        # 3. Failed logins
        all_events.extend(attack_failed_logins(args.target, args.port))

        # 4. Suspicious traffic
        all_events.extend(attack_suspicious_traffic(args.target, args.port))

        if not all_events:
            logger.warning("Aucun événement généré — la cible répond-elle?")
            if not args.loop:
                break
            time.sleep(10)
            continue

        # Envoyer les événements au SOC
        logger.info("")
        logger.info("━ Envoi de %d événements au SOC...", len(all_events))
        for ev in all_events:
            logger.info("  ↳ %s [%s] %s", ev["event_type"], ev["severity"], ev["message"][:80])

        ok = send_events(args.soc_url, token, "attacker-demo", all_events)
        if ok:
            logger.info("✓ Événements reçus par le SOC")
        else:
            logger.error("✗ Échec de l'envoi au SOC")

        # Vérifier les alertes créées
        try:
            resp = requests.get(
                f"{args.soc_url}/api/v1/alerts/",
                headers={"Authorization": f"Bearer {token}"},
                timeout=5,
            )
            data = resp.json()
            total_before = data.get("total", 0)
            by_status = data.get("by_status", {})
            logger.info(
                "Alertes: %d total | nouvelles: %d | en cours: %d | cloturées: %d",
                total_before,
                by_status.get("nouvelle", 0),
                by_status.get("en cours", 0),
                by_status.get("cloturee", 0),
            )
        except Exception as e:
            logger.error("Erreur vérification alertes: %s", e)

        if not args.loop:
            break

        logger.info("Attente 30s avant prochaine itération...")
        time.sleep(30)

    logger.info("")
    logger.info("✓ Attaques terminées. Ouvre http://localhost:8080 pour voir les résultats.")


if __name__ == "__main__":
    main()
