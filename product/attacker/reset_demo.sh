#!/bin/bash
# BigBrowser — Reset Demo Script
# Vide les tables de données et optionnellement relance les attaques / seed.
#
# Usage:
#   ./reset_demo.sh                    # reset minimal (alerts + ports + assets)
#   ./reset_demo.sh --all              # reset + restart server (vide events_store)
#   ./reset_demo.sh --attacks          # reset + relance attack_demo.py
#   ./reset_demo.sh --seed-compliance  # reset + re-seed les données NIS2
#   ./reset_demo.sh --all --attacks --seed-compliance  # tout en un
#   ./reset_demo.sh --no-restart       # sans redémarrer le serveur

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
BACKEND_DIR="$PROJECT_DIR/backend"
ATTACKER_DIR="$PROJECT_DIR/attacker"
DB_PATH="$BACKEND_DIR/bigbrowser.db"
SOC_URL="${SOC_URL:-http://localhost:8080}"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

info()  { echo -e "${GREEN}[RESET]${NC} $1"; }
warn()  { echo -e "${YELLOW}[RESET]${NC} $1"; }
error() { echo -e "${RED}[RESET]${NC} $1"; }

DO_ALL=false
DO_ATTACKS=false
DO_SEED=false
DO_RESTART=true

usage() {
    echo "BigBrowser — Reset Demo Script"
    echo ""
    echo "Usage: $0 [options]"
    echo ""
    echo "Options:"
    echo "  --all               Tout vider + restart serveur"
    echo "  --attacks           Relancer attack_demo.py après reset"
    echo "  --seed-compliance   Re-seed les données conformité NIS2"
    echo "  --no-restart        Ne pas redémarrer le serveur"
    echo "  --help              Affiche cette aide"
    echo ""
    echo "Exemples:"
    echo "  $0 --all --attacks           # clean + attaques fraîches"
    echo "  $0 --all --seed-compliance   # clean + conformité NIS2"
    echo "  $0 --no-restart              # reset sans toucher au serveur"
    exit 0
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --all)              DO_ALL=true; shift ;;
        --attacks)          DO_ATTACKS=true; shift ;;
        --seed-compliance)  DO_SEED=true; shift ;;
        --no-restart)       DO_RESTART=false; shift ;;
        --help)             usage ;;
        *) error "Option inconnue: $1"; usage ;;
    esac
done

# ── 1. Vider la BDD ────────────────────────────────────────

if [ ! -f "$DB_PATH" ]; then
    error "Base de données introuvable: $DB_PATH"
    exit 1
fi

info "Nettoyage de la base de données..."

python3 -c "
import sqlite3, sys
db = '$DB_PATH'
conn = sqlite3.connect(db)
c = conn.cursor()

tables = ['alerts', 'ports', 'assets']
before = {}
for t in tables:
    c.execute(f'SELECT COUNT(*) FROM {t}')
    before[t] = c.fetchone()[0]

c.execute('DELETE FROM alerts')
c.execute('DELETE FROM ports')
c.execute('DELETE FROM assets')
conn.commit()

after = {}
for t in tables:
    c.execute(f'SELECT COUNT(*) FROM {t}')
    after[t] = c.fetchone()[0]

conn.close()
print(f'  alerts:  {before[\"alerts\"]} → {after[\"alerts\"]}')
print(f'  ports:   {before[\"ports\"]} → {after[\"ports\"]}')
print(f'  assets:  {before[\"assets\"]} → {after[\"assets\"]}')
"

# ── 2. Redémarrer le serveur ────────────────────────────────

if [ "$DO_RESTART" = true ] || [ "$DO_ALL" = true ]; then
    info "Redémarrage du serveur (vide events_store)..."
    kill -9 "$(lsof -ti:8080 2>/dev/null | tail -1)" 2>/dev/null || true
    sleep 1

    cd "$BACKEND_DIR"
    setsid .venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8080 &>/tmp/uvicorn.log &
    sleep 3

    if curl -sf --max-time 3 http://localhost:8080/ &>/dev/null; then
        info "Serveur prêt sur http://localhost:8080"
    else
        error "Le serveur n'a pas démarré"
        tail -10 /tmp/uvicorn.log
        exit 1
    fi
else
    info "Serveur non redémarré (events_store conservé)"
fi

# ── 3. Seed conformité NIS2 ─────────────────────────────────

seed_compliance() {
    info "Seed des données conformité NIS2..."

    TOKEN=$(curl -sf --max-time 5 -X POST "$SOC_URL/api/v1/auth/login" \
        -H "Content-Type: application/json" \
        -d '{"username":"admin","password":"admin123"}' \
        | python3 -c "import sys,json;print(json.load(sys.stdin).get('access_token',''))")

    if [ -z "$TOKEN" ]; then
        error "Authentification échouée"
        return 1
    fi

    # Scan réseau (assets)
    curl -sf -X POST "$SOC_URL/api/v1/scan/" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $TOKEN" \
        -d '{"start_ip":"127.0.0.1","end_ip":"127.0.0.1","ports":[22,80,443,8080]}' \
        | python3 -c "import sys,json;d=json.load(sys.stdin);print(f'  Scan: {d.get(\"assets_found\",0)} assets')" 2>/dev/null

    # Events télémetry
    curl -sf -X POST "$SOC_URL/api/v1/telemetry/events" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $TOKEN" \
        -d '{
            "hostname":"seed","events":[
                {"event_type":"port_scan","source_ip":"10.0.0.1","message":"Scan SYN","severity":"high"},
                {"event_type":"port_scan","source_ip":"10.0.0.1","message":"Scan SYN port 22","severity":"high"},
                {"event_type":"port_scan","source_ip":"10.0.0.1","message":"Scan SYN port 80","severity":"high"},
                {"event_type":"failed_login","source_ip":"192.168.1.50","message":"Echec auth SSH","severity":"medium"},
                {"event_type":"failed_login","source_ip":"192.168.1.50","message":"Echec auth SSH #2","severity":"medium"},
                {"event_type":"failed_login","source_ip":"192.168.1.50","message":"Echec auth SSH #3","severity":"medium"},
                {"event_type":"brute_force","source_ip":"10.0.0.99","message":"Brute force","severity":"critical"},
                {"event_type":"unauthorized_access","source_ip":"172.16.0.10","message":"Accès non autorisé","severity":"high"},
                {"event_type":"malware","source_ip":"10.0.0.55","message":"Signature malware","severity":"critical"},
                {"event_type":"data_exfil","source_ip":"10.0.0.200","message":"Exfiltration","severity":"critical"},
                {"event_type":"dns_query","source_ip":"10.0.0.2","message":"DNS normal","severity":"low"},
                {"event_type":"http_request","source_ip":"10.0.0.3","message":"GET /","severity":"low"},
                {"event_type":"dns_query","source_ip":"10.0.0.4","message":"DNS sortant","severity":"low"},
                {"event_type":"http_request","source_ip":"10.0.0.5","message":"POST /api","severity":"low"},
                {"event_type":"connection","source_ip":"10.0.0.6","message":"Connexion établie","severity":"low"}
            ]
        }' > /dev/null
    info "  15 events télémetry envoyés"

    # Traffic captures (pour la page Trafic)
    for cap in \
      '{"hostname":"seed","source_ip":"10.0.0.1","target_ip":"192.168.1.1","source_port":40000,"target_port":80,"protocol":"http","payload_summary":"GET /"}' \
      '{"hostname":"seed","source_ip":"10.0.0.2","target_ip":"192.168.1.1","source_port":40001,"target_port":443,"protocol":"tcp","payload_summary":"TCP handshake"}' \
      '{"hostname":"seed","source_ip":"10.0.0.3","target_ip":"8.8.8.8","source_port":40002,"target_port":53,"protocol":"dns","payload_summary":"DNS query google.com"}' \
      '{"hostname":"seed","source_ip":"192.168.1.50","target_ip":"10.0.0.1","source_port":50000,"target_port":22,"protocol":"tcp","payload_summary":"SSH brute force attempt"}' \
      '{"hostname":"seed","source_ip":"172.16.0.10","target_ip":"192.168.1.1","source_port":50001,"target_port":8080,"protocol":"http","payload_summary":"POST /login — 401 Unauthorized"}' \
      '{"hostname":"seed","source_ip":"10.0.0.55","target_ip":"192.168.1.1","source_port":50002,"target_port":8443,"protocol":"tcp","payload_summary":"Suspicious outbound connection"}' \
      '{"hostname":"seed","source_ip":"10.0.0.2","target_ip":"192.168.1.1","source_port":40003,"target_port":80,"protocol":"http","payload_summary":"POST /api/v1/data"}' \
      '{"hostname":"seed","source_ip":"10.0.0.4","target_ip":"8.8.4.4","source_port":40004,"target_port":53,"protocol":"dns","payload_summary":"DNS query exfiltration-domain-xyz.com"}'; do
        curl -sf -X POST "$SOC_URL/api/v1/traffic/" \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer $TOKEN" \
            -d "$cap" > /dev/null
    done
    info "  8 captures trafic"
    sleep 1

    # Clôturer la première alerte
    curl -sf -X PATCH "$SOC_URL/api/v1/alerts/1" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $TOKEN" \
        -d '{"status":"cloturee"}' > /dev/null
    info "  1 alerte clôturée"

    # Export CSV
    curl -sf -X POST "$SOC_URL/api/v1/exports/" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $TOKEN" \
        -d '{"format":"csv","scope":"alerts"}' > /dev/null
    info "  1 export généré"

    info "Seed conformité terminé"
}

# ── 3.5 Seed conformité NIS2 ────────────────────────────────

if [ "$DO_SEED" = true ]; then
    seed_compliance
fi

# ── 4. Lancer les attaques ──────────────────────────────────

if [ "$DO_ATTACKS" = true ]; then
    info "Lancement des attaques..."
    cd "$ATTACKER_DIR"
    python3 attack_demo.py --soc-url "$SOC_URL" --target 127.0.0.1 --port 8080
fi

# ── 5. Résumé final ─────────────────────────────────────────

TOKEN=$(curl -sf --max-time 3 -X POST "$SOC_URL/api/v1/auth/login" \
    -H "Content-Type: application/json" \
    -d '{"username":"admin","password":"admin123"}' \
    | python3 -c "import sys,json;print(json.load(sys.stdin).get('access_token',''))" 2>/dev/null || echo "")

if [ -n "$TOKEN" ]; then
    info ""
    info "═ Résumé ═"
    curl -sf "$SOC_URL/api/v1/dashboard/" \
        -H "Authorization: Bearer $TOKEN" 2>/dev/null \
        | python3 -c "
import sys,json
d=json.load(sys.stdin)['metrics']
print(f'  Alertes: {d[\"total_alerts\"]}')
print(f'  Actifs:  {d[\"total_assets\"]}')
print(f'  Exports: {d[\"total_exports\"]}')
"
    info ""
    info "Dashboard: $SOC_URL"
    info "Login: admin / admin123"
fi

info "Terminé."
