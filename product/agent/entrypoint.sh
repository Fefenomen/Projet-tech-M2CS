#!/bin/bash
set -e

echo "[$(date)] Starting nginx..."
nginx

echo "[$(date)] Starting BigBrowser Agent..."
exec python3 agent.py
