# BigBrowser Backend

Backend FastAPI pour la plateforme de cybersurveillance réseau BigBrowser.

## Structure

```
product/backend/
├── app/
│   ├── main.py                 # Point d'entrée FastAPI
│   ├── core/
│   │   ├── config.py           # Configuration centralisée
│   │   └── database.py         # SQLAlchemy + seed users
│   ├── health/
│   │   └── router.py           # Endpoint de santé
│   ├── auth/
│   │   ├── router.py           # Login, /me, /users, RBAC
│   │   ├── schemas.py          # Pydantic schemas
│   │   └── service.py          # JWT, bcrypt, DB queries
│   ├── discovery/
│   │   ├── router.py           # Scan réseau (POST /scan)
│   │   ├── schemas.py          # IP validation, scan schemas
│   │   └── service.py          # TCP socket port scanning
│   ├── assets/
│   │   ├── router.py           # CRUD actifs (GET /assets)
│   │   ├── schemas.py          # Asset/Port response schemas
│   │   └── service.py          # Asset DB queries
│   ├── alerts/
│   │   ├── router.py           # CRUD alertes + PATCH statut
│   │   ├── schemas.py          # Alert schemas + validation
│   │   └── service.py          # Alert DB queries + audit log
│   ├── models/
│   │   ├── user.py             # User (users table)
│   │   ├── asset.py            # Asset (assets table)
│   │   ├── port.py             # Port (ports table, +service_name)
│   │   ├── alert.py            # Alert (alerts table)
│   │   ├── audit_log.py        # AuditLog (audit_logs table)
│   │   └── export.py           # ExportRecord (exports table)
│   └── telemetry/
│       ├── router.py           # Heartbeat endpoints
│       ├── schemas.py          # Heartbeat schemas
│       └── service.py          # Heartbeat logic
├── tests/
│   ├── conftest.py             # Test DB setup
│   ├── test_health.py          # Auth, health, telemetry tests
│   ├── test_database.py        # Model + DB tests
│   ├── test_discovery.py       # Scan + assets tests
│   └── test_alerts.py          # Alert CRUD + lifecycle tests
├── pyproject.toml              # Dependencies
├── .env.example                # Variables d'environnement
└── README.md
```

## Prérequis

- Python 3.11+
- pip

## Installation

```bash
cd product/backend
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Lancement

```bash
uvicorn app.main:app --reload
```

Le serveur démarre sur http://127.0.0.1:8000

## Test

```bash
python -m pytest -v
```

## Endpoints disponibles (Sprint 4)

| Méthode | Endpoint | Usage | Accès |
|---|---|---|---|
| `GET` | `/` | Infos service | Public |
| `GET` | `/health/` | Health check | Public |
| `POST` | `/api/v1/auth/login` | Authentification | Public |
| `GET` | `/api/v1/auth/me` | Infos utilisateur courant | Authentifié |
| `POST` | `/api/v1/auth/users` | Créer un utilisateur | `admin` uniquement |
| `POST` | `/api/v1/telemetry/heartbeat` | Heartbeat endpoint | Authentifié |
| `GET` | `/api/v1/telemetry/heartbeats` | Liste heartbeats | Authentifié |
| `POST` | `/api/v1/scan/` | Lancer un scan réseau | `admin` uniquement |
| `GET` | `/api/v1/assets/` | Liste des actifs | Authentifié |
| `GET` | `/api/v1/assets/{id}` | Détail actif + ports | Authentifié |
| `GET` | `/api/v1/alerts/` | Liste alertes + stats | Authentifié |
| `GET` | `/api/v1/alerts/{id}` | Détail alerte | Authentifié |
| `POST` | `/api/v1/alerts/` | Créer une alerte | Authentifié |
| `PATCH` | `/api/v1/alerts/{id}` | Changer statut alerte | Authentifié |

## Comptes par défaut

| Username | Password | Rôle |
|---|---|---|
| `admin` | `admin123` | `admin` |
| `analyst` | `analyst123` | `analyst` |

## Documentation API

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Progression MVP

| Sprint | US | Statut |
|---|---|---|
| Sprint 1 | US-01.1 Health | ✅ |
| Sprint 1 | US-01.2 Backend skeleton | ✅ |
| Sprint 1 | US-01.3 Database SQLite | ✅ |
| Sprint 1 | US-01.4 Data Models | ✅ |
| Sprint 2 | US-01.5 Auth JWT (DB) | ✅ |
| Sprint 2 | US-01.6 Init admin + /users | ✅ |
| Sprint 3 | US-01.7 Scan réseau | ✅ |
| Sprint 3 | US-01.8 Inventaire actifs | ✅ |
| Sprint 4 | US-01.9 Détection/Alertes | ✅ |
| Sprint 4 | US-01.10 Cycle de vie alertes | ✅ |
| Sprint 5 | US-01.11 Exports CSV/JSON | ❌ |
| Sprint 5 | US-01.12 Audit logs | ❌ |
| Sprint 6 | US-01.13 Frontend | ❌ |
| Sprint 6 | US-01.14 Traffic capture (P2) | ❌ |
