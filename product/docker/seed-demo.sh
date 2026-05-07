#!/bin/bash
# BigBrowser — Demo Seed Script
# Pre-populates the SOC with realistic data for demonstration.
# Usage: ./seed-demo.sh [SOC_URL] [TOKEN]

set -e

SOC_URL="${1:-http://localhost:8000}"
TOKEN="${2:-}"

info() { echo "[SEED] $1"; }

# Get token if not provided
if [ -z "$TOKEN" ]; then
    info "Authenticating as admin..."
    TOKEN=$(curl -sf -X POST "$SOC_URL/api/v1/auth/login" \
        -H "Content-Type: application/json" \
        -d '{"username":"admin","password":"admin123"}' \
        | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])" 2>/dev/null)
    if [ -z "$TOKEN" ]; then
        echo "ERROR: Failed to get token. Check SOC URL and credentials."
        exit 1
    fi
    info "Token obtained."
fi

AUTH="Authorization: Bearer $TOKEN"

# 1. Run network scan
info "Step 1: Scanning network 172.20.0.0/24..."
curl -sf -X POST "$SOC_URL/api/v1/scan/" \
    -H "Content-Type: application/json" \
    -H "$AUTH" \
    -d '{"ip_range":"172.20.0.0/24","ports":[22,80,443,8080]}' \
    | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'  Found {d.get(\"assets_found\",0)} assets')" 2>/dev/null || echo "  Scan triggered (async)"

sleep 2

# 2. Send telemetry events (simulating endpoint detections)
info "Step 2: Sending endpoint events..."

# Event: Port scan detected
curl -sf -X POST "$SOC_URL/api/v1/telemetry/events" \
    -H "Content-Type: application/json" \
    -H "$AUTH" \
    -d '{
        "hostname": "endpoint1",
        "events": [
            {"event_type": "port_scan", "source_ip": "172.20.0.50", "message": "Port scan detected from attacker", "severity": "high"},
            {"event_type": "port_scan", "source_ip": "172.20.0.50", "message": "Port scan detected from attacker", "severity": "high"},
            {"event_type": "port_scan", "source_ip": "172.20.0.50", "message": "Port scan detected from attacker", "severity": "high"}
        ]
    }' > /dev/null

# Event: Failed login attempts
curl -sf -X POST "$SOC_URL/api/v1/telemetry/events" \
    -H "Content-Type: application/json" \
    -H "$AUTH" \
    -d '{
        "hostname": "endpoint1",
        "events": [
            {"event_type": "failed_login_attempt", "source_ip": "172.20.0.50", "message": "SSH brute force detected", "severity": "critical"},
            {"event_type": "failed_login_attempt", "source_ip": "172.20.0.50", "message": "SSH brute force detected", "severity": "critical"},
            {"event_type": "failed_login_attempt", "source_ip": "172.20.0.50", "message": "SSH brute force detected", "severity": "critical"}
        ]
    }' > /dev/null

# Event: HTTP flood
curl -sf -X POST "$SOC_URL/api/v1/telemetry/events" \
    -H "Content-Type: application/json" \
    -H "$AUTH" \
    -d '{
        "hostname": "endpoint2",
        "events": [
            {"event_type": "http_flood", "source_ip": "172.20.0.50", "message": "HTTP flood to /admin", "severity": "medium"},
            {"event_type": "http_flood", "source_ip": "172.20.0.50", "message": "HTTP flood to /admin", "severity": "medium"},
            {"event_type": "http_flood", "source_ip": "172.20.0.50", "message": "HTTP flood to /admin", "severity": "medium"}
        ]
    }' > /dev/null

# Event: Normal traffic (for telemetry volume)
curl -sf -X POST "$SOC_URL/api/v1/telemetry/events" \
    -H "Content-Type: application/json" \
    -H "$AUTH" \
    -d '{
        "hostname": "endpoint1",
        "events": [
            {"event_type": "http_request", "source_ip": "172.20.0.20", "message": "Normal HTTP request", "severity": "low"},
            {"event_type": "http_request", "source_ip": "172.20.0.20", "message": "Normal HTTP request", "severity": "low"},
            {"event_type": "http_request", "source_ip": "172.20.0.20", "message": "Normal HTTP request", "severity": "low"},
            {"event_type": "http_request", "source_ip": "172.20.0.20", "message": "Normal HTTP request", "severity": "low"},
            {"event_type": "http_request", "source_ip": "172.20.0.20", "message": "Normal HTTP request", "severity": "low"}
        ]
    }' > /dev/null

info "Events sent."
sleep 2

# 3. Send heartbeat
info "Step 3: Sending heartbeat..."
curl -sf -X POST "$SOC_URL/api/v1/telemetry/heartbeat" \
    -H "Content-Type: application/json" \
    -H "$AUTH" \
    -d '{"hostname":"endpoint1","ip_address":"172.20.0.20","status":"active","version":"1.0.0","agent_version":"1.0.0"}' > /dev/null

curl -sf -X POST "$SOC_URL/api/v1/telemetry/heartbeat" \
    -H "Content-Type: application/json" \
    -H "$AUTH" \
    -d '{"hostname":"endpoint2","ip_address":"172.20.0.21","status":"active","version":"1.0.0","agent_version":"1.0.0"}' > /dev/null

info "Heartbeats sent."

# 4. Generate export
info "Step 4: Generating CSV export..."
EXPORT_RESULT=$(curl -sf -X POST "$SOC_URL/api/v1/exports/" \
    -H "Content-Type: application/json" \
    -H "$AUTH" \
    -d '{"format":"csv","scope":"alerts"}' \
    | python3 -c "import sys,json; d=json.load(sys.stdin); print(f\"Export #{d['id']}: {d['row_count']} rows\")" 2>/dev/null)

if [ -n "$EXPORT_RESULT" ]; then
    info "  $EXPORT_RESULT"
else
    info "  Export triggered"
fi

# 5. Show results
info ""
info "=== SEED COMPLETE ==="
info "Fetching dashboard metrics..."

curl -sf "$SOC_URL/api/v1/dashboard/" \
    -H "$AUTH" \
    | python3 -c "
import sys, json
d = json.load(sys.stdin)
m = d.get('metrics', {})
print(f\"  Assets:       {m.get('total_assets', 0)}\")
print(f\"  Alerts:       {m.get('total_alerts', 0)}\")
print(f\"  Audit logs:   {m.get('total_audit_logs', 0)}\")
print(f\"  Exports:      {m.get('total_exports', 0)}\")
" 2>/dev/null || info "  (dashboard data not available yet)"

info ""
info "Next: Open http://localhost:8000 and login as admin / admin123"
