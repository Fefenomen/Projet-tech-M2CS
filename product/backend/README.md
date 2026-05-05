# BigBrowser Backend

Backend FastAPI pour la plateforme de cybersurveillance réseau BigBrowser.

## Structure

```
product/backend/
├── app/
│   ├── main.py           # Point d'entrée FastAPI
│   ├── core/
│   │   └── config.py     # Configuration centralisée
│   ├── health/
│   │   └── router.py     # Endpoint de santé
│   └── auth/
│       └── router.py     # Skeleton authentification
├── tests/
│   └── test_health.py    # Tests pytest
├── pyproject.toml        # Configuration du projet
└── .env.example          # Variables d'environnement
```

## Prérequis

- Python 3.11+
- pip

## Installation

```bash
cd product/backend
python -m venv .venv
source .venv/bin/activate  # Sur Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## Lancement

```bash
uvicorn app.main:app --reload
```

Le serveur démarre sur http://127.0.0.1:8000

## Test

```bash
python -m pytest
```

## Endpoints disponibles (MVP-01)

- `GET /` - Informations sur le service
- `GET /health/` - Health check (statut du service)
- `POST /auth/login` - Skeleton (à implémenter)
- `POST /auth/token` - Skeleton (à implémenter)

## Documentation API

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
