#!/bin/bash
# BigBrowser — Demo Lab Launcher
# Usage: ./demo.sh [up|down|status|logs|reset]

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

info() { echo -e "${GREEN}[BBROWSER]${NC} $1"; }
warn() { echo -e "${YELLOW}[BBROWSER]${NC} $1"; }
error() { echo -e "${RED}[BBROWSER]${NC} $1"; }

usage() {
    echo "BigBrowser Demo Lab"
    echo ""
    echo "Usage: $0 [command]"
    echo ""
    echo "Commands:"
    echo "  up       Start the full lab (SOC + Endpoints + Attacker)"
    echo "  down     Stop and remove all containers"
    echo "  status   Show container status"
    echo "  logs     Show logs from all containers"
    echo "  reset    Full reset: down + rebuild + up"
    echo "  demo     Run a quick demo scenario (up + wait + show results)"
    echo ""
    echo "After 'up', access the dashboard at: http://localhost:8000"
    echo "Default login: admin / admin123"
}

check_docker() {
    if ! command -v docker &>/dev/null; then
        error "Docker not found. Install Docker first."
        exit 1
    fi
    if ! docker compose version &>/dev/null; then
        error "Docker Compose not found. Install Docker Compose (v2+)."
        exit 1
    fi
    if ! docker compose ps &>/dev/null 2>&1; then
        error "Cannot connect to Docker daemon. Start it first."
        exit 1
    fi
}

cmd_up() {
    check_docker
    info "Starting BigBrowser Lab..."
    docker compose up -d --build
    info "Waiting for SOC to be ready..."
    for i in $(seq 1 30); do
        if curl -sf http://localhost:8000/health/ &>/dev/null; then
            info "SOC is ready!"
            echo ""
            echo -e "${GREEN}╔════════════════════════════════════════════════════════╗${NC}"
            echo -e "${GREEN}║  BigBrowser Lab — RUNNING                            ║${NC}"
            echo -e "${GREEN}║                                                      ║${NC}"
            echo -e "${GREEN}║  Dashboard:  http://localhost:8000                   ║${NC}"
            echo -e "${GREEN}║  Swagger:    http://localhost:8000/docs              ║${NC}"
            echo -e "${GREEN}║  Login:      admin / admin123                        ║${NC}"
            echo -e "${GREEN}╚════════════════════════════════════════════════════════╝${NC}"
            echo ""
            return 0
        fi
        sleep 2
    done
    error "SOC did not start in time. Check logs with: $0 logs"
    exit 1
}

cmd_down() {
    check_docker
    info "Stopping BigBrowser Lab..."
    docker compose down
    info "Lab stopped."
}

cmd_status() {
    check_docker
    docker compose ps
}

cmd_logs() {
    check_docker
    docker compose logs -f --tail=50
}

cmd_reset() {
    check_docker
    info "Full reset..."
    docker compose down -v
    docker compose build --no-cache
    docker compose up -d
    info "Reset complete. Waiting for SOC..."
    for i in $(seq 1 30); do
        if curl -sf http://localhost:8000/health/ &>/dev/null; then
            info "SOC is ready at http://localhost:8000"
            return 0
        fi
        sleep 2
    done
    error "SOC did not start in time."
    exit 1
}

cmd_demo() {
    cmd_up

    info "Waiting for endpoints to register..."
    sleep 15

    info "Seeding demo data..."
    if [ -f "./seed-demo.sh" ]; then
        chmod +x ./seed-demo.sh
        ./seed-demo.sh "http://localhost:8000"
    else
        warn "seed-demo.sh not found, skipping seed."
    fi

    info "Waiting for attacker scenarios..."
    sleep 30

    info "Fetching dashboard metrics..."
    TOKEN=$(curl -sf -X POST http://localhost:8000/api/v1/auth/login \
        -H "Content-Type: application/json" \
        -d '{"username":"admin","password":"admin123"}' | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])" 2>/dev/null)

    if [ -n "$TOKEN" ]; then
        echo ""
        info "=== DASHBOARD METRICS ==="
        curl -sf http://localhost:8000/api/v1/dashboard/ \
            -H "Authorization: Bearer $TOKEN" | python3 -m json.tool
        echo ""
        info "=== RECENT ALERTS ==="
        curl -sf http://localhost:8000/api/v1/alerts/ \
            -H "Authorization: Bearer $TOKEN" | python3 -m json.tool
        echo ""
        info "=== NIS2 COMPLIANCE ==="
        curl -sf http://localhost:8000/api/v1/compliance/nis2 \
            -H "Authorization: Bearer $TOKEN" | python3 -c "
import sys, json
d = json.load(sys.stdin)
s = d['score']
print(f\"  Score: {s['overall_score']}%\")
print(f\"  Conform: {s['compliant_count']}/{s['total_requirements']}\")
" 2>/dev/null || echo "  (not available)"
        echo ""
        info "=== AUDIT LOGS ==="
        curl -sf http://localhost:8000/api/v1/audit-logs/ \
            -H "Authorization: Bearer $TOKEN" | python3 -m json.tool
    fi

    info ""
    info "Demo complete! Dashboard: http://localhost:8000"
    info "Login: admin / admin123"
}

case "${1:-up}" in
    up)     cmd_up ;;
    down)   cmd_down ;;
    status) cmd_status ;;
    logs)   cmd_logs ;;
    reset)  cmd_reset ;;
    demo)   cmd_demo ;;
    *)      usage; exit 1 ;;
esac
