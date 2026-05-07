# BigBrowser Product

BigBrowser est un outil open-source de cybersurveillance réseau orienté SOC. Le produit vise à fournir une visibilité réseau aux PME françaises pour la conformité NIS2.

## Architecture

```
product/
├── backend/          # API FastAPI + SQLite + Frontend
├── frontend/         # Interface web Bootstrap (servie par le backend)
├── docker/           # Docker Compose + Lab de démonstration
├── agent/            # Agent Endpoint (heartbeat + events)
└── attacker/         # Scénarios offensifs contrôlés pour la démo
```

## Stack technique

- **Backend** : Python / FastAPI / SQLite
- **Frontend** : Bootstrap 5 + Vanilla JS (SPA)
- **Déploiement** : Docker Compose (3 zones : SOC, Endpoints, Attaquant)
- **Auth** : JWT avec rôles admin/analyst

## Lancement rapide

### Option 1 : Backend local

```bash
cd product/backend
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

→ http://127.0.0.1:8000 (admin / admin123)

### Option 2 : Lab Docker complet

```bash
cd product/docker
./demo.sh demo
```

→ Lance SOC + 2 Endpoints + Attaquant automatiquement

## Comptes par défaut

| Username | Password | Rôle |
|---|---|---|
| `admin` | `admin123` | Administrateur |
| `analyst` | `analyst123` | Analyste |
| `agent` | `agent_secret_mvp` | Agent (heartbeat) |

## API Endpoints

| Méthode | Endpoint | Usage | Accès |
|---|---|---|---|
| `POST` | `/api/v1/auth/login` | Authentification | Public |
| `GET` | `/api/v1/auth/me` | Infos utilisateur | Authentifié |
| `POST` | `/api/v1/auth/users` | Créer utilisateur | Admin |
| `POST` | `/api/v1/telemetry/heartbeat` | Heartbeat agent | Authentifié |
| `POST` | `/api/v1/telemetry/events` | Events agent | Authentifié |
| `POST` | `/api/v1/scan/` | Scan réseau | Admin |
| `GET` | `/api/v1/assets/` | Liste actifs | Authentifié |
| `GET` | `/api/v1/assets/{id}` | Détail actif | Authentifié |
| `GET` | `/api/v1/alerts/` | Liste alertes | Authentifié |
| `GET` | `/api/v1/alerts/{id}` | Détail alerte | Authentifié |
| `POST` | `/api/v1/alerts/` | Créer alerte | Authentifié |
| `PATCH` | `/api/v1/alerts/{id}` | Changer statut | Authentifié |
| `GET` | `/api/v1/dashboard/` | Métriques | Authentifié |
| `POST` | `/api/v1/exports/` | Export CSV/JSON | Authentifié |
| `GET` | `/api/v1/exports/{id}/download` | Télécharger export | Authentifié |
| `GET` | `/api/v1/audit-logs/` | Journaux d'audit | Admin |
| `GET` | `/api/v1/audit-logs/{id}` | Détail journal | Admin |

## Tests

```bash
cd product/backend
source .venv/bin/activate
pytest -v
```

## Documentation

- [Backend README](backend/README.md)
- [Docker Lab README](docker/README.md)
- [Cahier des charges](../../documents/06_cahier_des_charges/rendu_principal.md)
- [Architecture](../../documents/08_architecture/rendu_principal.md)
