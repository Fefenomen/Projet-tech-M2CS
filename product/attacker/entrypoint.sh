#!/bin/bash
set -e

echo "[$(date)] BigBrowser Attacker starting..."
echo "[$(date)] Targets: $TARGET_SUBNET"
echo "[$(date)] Scenario delay: ${SCENARIO_DELAY}s"

exec python3 scenarios.py
