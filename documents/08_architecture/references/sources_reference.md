# Références Architecture — BigBrowser

> Fichier consolidé des documents de référence architecturale
> Projet : BigBrowser — Outil de Supervision et d'Analyse Réseau
> Version : 1.0 — Mai 2026

---

## Section 1 — Stack technique

### 1.1 Récapitulatif des 13 composants

| Couche | Technologie | Version cible | Usage principal | Justification |
|---|---|---|---|---|
| Langage | [Python](https://www.python.org/) | 3.11+ | Backend applicatif, workers Celery, scripts auxiliaires | Écosystème réseau/sécurité mature (Scapy, python-nmap, Celery). Adoption large dans le secteur cyber. Jusqu'à 25 % plus rapide que 3.10. Alternatives écartées : Go (écosystème moins riche), Rust (courbe d'apprentissage trop raide pour MVP). |
| Framework web | [FastAPI](https://fastapi.tiangolo.com/) | 0.110+ | API REST, documentation OpenAPI automatique | Asynchrone natif (uvicorn), validation intégrée via Pydantic, documentation OpenAPI auto, performances au niveau de Node.js/Go. Alternative écartée : Flask (synchrone), Django (trop lourd pour une API REST pure). |
| ORM | [SQLAlchemy](https://www.sqlalchemy.org/) | 2.x | Abstraction base de données, migrations | ORM le plus mature de l'écosystème Python. Syntaxe 2.0 native, support PostgreSQL (JSONB, UUID). Alternative écartée : Peewee (trop limité), Tortoise ORM (moins mature). |
| Validation | [Pydantic](https://docs.pydantic.dev/) | 2.x | Schémas de validation des données API | Validation stricte des payloads, typage Python natif, moteur Rust (pydantic-core) 5-10x plus rapide que v1. Rôle clé : validation des plages IP (CIDR regex), normalisation des événements réseau. |
| Migrations BDD | [Alembic](https://alembic.sqlalchemy.org/) | Latest | Gestion des schémas et versions de base | Migrations automatiques depuis le modèle SQLAlchemy, indispensable pour l'évolution du schéma. |
| Frontend | [Bootstrap](https://getbootstrap.com/) | 5.x + Vanilla JS | Interface utilisateur responsive | Compatibilité maximale sans framework JS lourd. Plus de dépendance jQuery, composants natifs CSS/JS, dark mode natif. Alternatives écartées : React/Vue.js (complexité inutile MVP), Tailwind (nécessite une étape de build). |
| Base de données | [PostgreSQL](https://www.postgresql.org/) | 15+ | Persistance principale, données fonctionnelles | JSONB pour les règles de détection, robustesse, open-source. Répond aux exigences de traçabilité NIS2. Alternative écartée : MySQL (JSONB moins mature), SQLite (pas de JSONB natif, pas de concurrence d'écriture). |
| Queue de tâches | [Celery](https://docs.celeryq.dev/) | 5.x | Traitements asynchrones (scans, exports, détection) | Délégation des opérations longues hors du thread HTTP. Indispensable pour garantir une interface réactive (< 2 s). Alternative écartée : RQ (trop simple, pas de priorisation), RabbitMQ (plus lourd que Redis pour MVP). |
| Broker | [Redis](https://redis.io/) | 7.x | File de messages Celery, cache in-memory | Broker ultra-rapide, backend de résultats pour Celery, cache pour les métriques du tableau de bord. |
| Scan réseau | [Nmap](https://nmap.org/) | 7.94+ | Découverte d'équipements, ports, services | Référence secteur pour le scan réseau. Support des scripts NSE. Alternatives écartées : masscan (moins de fonctionnalités), Zmap (pas de NSE). |
| Capture réseau | [Scapy](https://scapy.net/) / [tcpdump](https://www.tcpdump.org/) | Latest | Analyse de paquets, mode promiscuous | Analyse de paquets Python native, décodage des protocoles. tcpdump pour les cas de trafic volumineux. Alternative écartée : libpcap (binding C), Zeek (complexe à intégrer). |
| Conteneurisation | [Docker + Compose](https://docs.docker.com/compose/) | Latest | Déploiement reproductible on-premise | Topologie 3 zones (attaquant, endpoints, SOC), isolation réseau totale. Kubernetes écarté (complexité excessive pour MVP). |
| Reverse proxy | [Nginx](https://nginx.org/) | 1.25+ | Frontend statique, proxy inverse vers FastAPI | Sert les fichiers statiques, proxy inverse, terminaison TLS, cache des assets. Support HTTP/3 (QUIC). |

### 1.2 Tests et CI/CD

| Technologie | Version cible | Usage |
|---|---|---|
| [pytest](https://docs.pytest.org/) + [httpx](https://www.python-httpx.org/) | Latest | Tests unitaires et d'intégration. Couverture ≥ 70 % sur services critiques. |
| [GitHub Actions](https://docs.github.com/en/actions) | — | Pipeline CI/CD : lint → test → build → release. |

### 1.3 Prérequis système

| Ressource | Minimum | Recommandé |
|---|---|---|
| RAM | 4 Go | 8 Go |
| CPU | 2 cœurs | 4 cœurs |
| Espace disque | 20 Go | 50 Go |
| OS | Ubuntu 22.04+ | Debian 12 / Ubuntu 24.04 |
| Docker | 24+ | 26+ |
| Docker Compose | V2 | V2 |
| Capacités réseau | `NET_RAW`, `NET_ADMIN` | — |

### 1.4 Compatibilité inter-composants

```
Frontend (Bootstrap 5.x / JS vanilla)
        │ HTTP/JSON
        ▼
Nginx 1.25+ (reverse proxy + fichiers statiques)
        │ proxy_pass
        ▼
FastAPI 0.110+ (routes, validation Pydantic 2.x)
        │
        ├──▶ SQLAlchemy 2.x ──▶ PostgreSQL 15+
        │
        └──▶ Celery 5.x ──▶ Redis 7.x
                │
                ├──▶ Nmap 7.94+ (subprocess)
                ├──▶ Scapy / tcpdump (capture)
                └──▶ Python standard library
```

---

## Section 2 — Modules et flux

### 2.1 Architecture modulaire du backend — 8 modules

```
app/
├── main.py                 # Point d'entrée FastAPI, enregistrement des routers
├── core/                   # Configuration, sécurité, exceptions, logging
│   ├── config.py           #   Variables d'environnement (pydantic-settings)
│   ├── security.py         #   Middleware CORS, dépendances JWT, validation des rôles
│   ├── exceptions.py       #   Gestion centralisée des erreurs HTTP
│   └── logging.py          #   Configuration des logs structurés JSON
├── auth/                   # Authentification, rôles, tokens JWT
│   ├── routes.py           #   Login, /me, gestion users
│   ├── schemas.py          #   Schémas Pydantic (login, user, token)
│   ├── service.py          #   Vérification identifiants, génération JWT
│   └── models.py           #   Modèle SQLAlchemy User
├── telemetry/              # Réception heartbeat + events agents
│   ├── routes.py           #   POST /telemetry/heartbeat, /telemetry/events
│   ├── schemas.py          #   Validation Pydantic + regex (IP, plages)
│   ├── service.py          #   Normalisation, persistance
│   └── models.py           #   Modèle SQLAlchemy Event
├── discovery/              # Scan réseau, découverte d'actifs
│   ├── routes.py           #   POST /scan
│   ├── schemas.py          #   Schémas scan (ip_range, ports)
│   ├── service.py          #   Orchestration Celery, parsing Nmap
│   └── models.py           #   Modèle SQLAlchemy Asset
├── assets/                 # Inventaire des actifs réseau
│   ├── routes.py           #   GET /assets, GET /assets/{id}
│   ├── schemas.py          #   Schémas actif (IP, hostname, ports)
│   ├── service.py          #   CRUD, enrichissement, pagination
│   └── models.py           #   Modèle SQLAlchemy Asset + NetworkFinding
├── alerts/                 # Alertes, cycle de vie, qualification
│   ├── routes.py           #   GET/PATCH /alerts
│   ├── schemas.py          #   Schémas alerte, statut, qualification
│   ├── service.py          #   Génération, cycle de vie, déduplication
│   └── models.py           #   Modèle SQLAlchemy Alert
├── reports/                # Rapports, exports CSV/JSON
│   ├── routes.py           #   POST /exports, GET /exports/{id}/download
│   ├── schemas.py          #   Schémas export (format, scope)
│   ├── service.py          #   Génération Celery, métadonnées
│   └── models.py           #   Modèle SQLAlchemy Export
└── audit/                  # Traçabilité des actions sensibles
    ├── routes.py           #   GET /audit-logs
    ├── schemas.py          #   Schémas audit log
    ├── service.py          #   Journalisation, consultation, filtrage
    └── models.py           #   Modèle SQLAlchemy AuditLog
```

### 2.2 Contrat API MVP — 16 endpoints

| Méthode | Endpoint | Usage | Accès | Priorité |
|---|---|---|---|---|
| `POST` | `/api/v1/auth/login` | Authentification utilisateur | Public | P1 |
| `GET` | `/api/v1/auth/me` | Informations utilisateur courant | `admin`, `analyst` | P1 |
| `POST` | `/api/v1/auth/users` | Création d'un utilisateur | `admin` | P1 |
| `GET` | `/api/v1/health` | Santé applicative (API, BDD, worker) | Public | P1 |
| `POST` | `/api/v1/telemetry/heartbeat` | Réception heartbeat agent | Agent | P1 |
| `POST` | `/api/v1/telemetry/events` | Réception événements agent | Agent | P1 |
| `POST` | `/api/v1/scan/` | Lancement d'un scan réseau | `admin` | P1 |
| `GET` | `/api/v1/assets/` | Liste des actifs | `admin`, `analyst` | P1 |
| `GET` | `/api/v1/assets/{id}` | Détail d'un actif | `admin`, `analyst` | P1 |
| `GET` | `/api/v1/alerts/` | Liste des alertes | `admin`, `analyst` | P1 |
| `GET` | `/api/v1/alerts/{id}` | Détail d'une alerte | `admin`, `analyst` | P1 |
| `PATCH` | `/api/v1/alerts/{id}` | Qualification / changement statut | `admin`, `analyst` | P1 |
| `POST` | `/api/v1/exports/` | Génération export CSV/JSON | `admin`, `analyst` | P1 |
| `GET` | `/api/v1/exports/{id}/download` | Téléchargement export | `admin`, `analyst` | P1 |
| `GET` | `/api/v1/audit-logs/` | Consultation journaux d'audit | `admin` | P2 |
| `GET` | `/api/v1/dashboard/` | Métriques du tableau de bord | `admin`, `analyst` | P1 |

### 2.3 Modèle de données — 7 entités

```
┌───────────────┐       ┌────────────────┐
│     users     │       │     assets     │
│───────────────│       │────────────────│
│ id (PK)       │       │ id (PK)        │
│ username      │       │ ip_address     │
│ password_hash │       │ hostname       │
│ role          │       │ mac_address    │
│ is_active     │       │ os_guess       │
│ created_at    │       │ first_seen_at  │
└───────────────┘       │ last_seen_at   │
                        │ status         │
                        └───────┬────────┘
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
          ▼                     ▼                     ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ network_findings │  │     events       │  │     alerts       │
│──────────────────│  │──────────────────│  │──────────────────│
│ id (PK)          │  │ id (PK)          │  │ id (PK)          │
│ asset_id (FK)    │  │ asset_id (FK)    │  │ title            │
│ port             │  │ source_ip        │  │ severity         │
│ protocol         │  │ target_ip        │  │ status           │
│ service_name     │  │ event_type       │  │ source_ip        │
│ state            │  │ severity         │  │ description      │
│ observed_at      │  │ message          │  │ created_at       │
└──────────────────┘  │ created_at       │  │ updated_at       │
                      └──────────────────┘  └──────────────────┘

┌──────────────────┐  ┌──────────────────┐
│   audit_logs     │  │     exports      │
│──────────────────│  │──────────────────│
│ id (PK)          │  │ id (PK)          │
│ user_id (FK)     │  │ format           │
│ role             │  │ requested_by     │
│ action           │  │ scope            │
│ target_type      │  │ file_path        │
│ result           │  │ created_at       │
│ created_at       │  │ row_count        │
└──────────────────┘  └──────────────────┘
```

### 2.4 Flux principaux — 6 flux

| ID | Flux | Source → Destination | Déclencheur | Données |
|---|---|---|---|---|
| FLUX-1 | Scan réseau et découverte | Attaquant → Endpoints → Backend FastAPI | Requête admin POST /scan | Plage IP, ports, services |
| FLUX-2 | Télémétrie agent | Endpoint → Agent Heartbeat → Backend FastAPI | Timer agent (30 s) | Heartbeat + events |
| FLUX-3 | Requêtes utilisateur | Frontend Bootstrap → Backend FastAPI | Navigation admin/analyst | Requêtes CRUD JSON |
| FLUX-4 | Persistance données | Backend FastAPI / Celery → PostgreSQL | Toute opération d'écriture | Insert/update/delete SQL |
| FLUX-5 | Traitement asynchrone | Backend FastAPI → Redis → Celery Worker | Scan, export, détection | Task ID, paramètres |
| FLUX-6 | Résultat traitement | Celery Worker → PostgreSQL | Fin de tâche | Résultats scan, export, alerte |

### 2.5 Topologie 3 zones Docker

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                         DOCKER HOST (Linux)                                       │
│                                                                                   │
│  ┌─────────────────────────────────────────────────────────────────────────────┐  │
│  │                          Réseau : bigbrowser_sim                             │  │
│  │                    (bridge / macvlan — simulation réseau)                    │  │
│  │                                                                              │  │
│  │  ┌────────────────────┐       ┌────────────────────┐                        │  │
│  │  │  ZONE ATTAQUANT    │       │  ZONE ENDPOINTS    │                        │  │
│  │  │                    │       │                    │                        │  │
│  │  │  [attaquant]       │──────▶│  [endpoint-1]      │                        │  │
│  │  │  - Kali Linux      │       │  - services exposés│                        │  │
│  │  │  - nmap            │       │  - Agent heartbeat │                        │  │
│  │  │  - Scapy scripts   │       │                    │                        │  │
│  │  │                    │       │  [endpoint-2]      │                        │  │
│  │  └────────────────────┘       │  - services exposés│                        │  │
│  │                               │  - Agent heartbeat │                        │  │
│  │                               └────────┬───────────┘                        │  │
│  └─────────────────────────────────────────┼───────────────────────────────────┘  │
│                                            │ Agent HTTP                           │
│  ┌─────────────────────────────────────────┼───────────────────────────────────┐  │
│  │              Réseau : bigbrowser_internal│                                   │  │
│  │                     (bridge — isolé)     │                                   │  │
│  │                                          ▼                                  │  │
│  │  ┌──────────────────────────────────────────────────────────────────────┐   │  │
│  │  │                    ZONE SOC (Docker Container SOC)                   │   │  │
│  │  │                                                                      │   │  │
│  │  │  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐       │   │  │
│  │  │  │ Frontend │    │ Backend  │    │   DB     │    │  Redis   │       │   │  │
│  │  │  │ Nginx:80 │◀──▶│ FastAPI  │◀──▶│PostgreSQL│    │  :6379   │       │   │  │
│  │  │  └──────────┘    │  :8000   │    └──────────┘    └────┬─────┘       │   │  │
│  │  │                  └──────────┘                         │             │   │  │
│  │  │                                                        │             │   │  │
│  │  │                                                 ┌──────▼──────┐     │   │  │
│  │  │                                                 │   Celery   │     │   │  │
│  │  │                                                 │   Worker   │     │   │  │
│  │  │                                                 └────────────┘     │   │  │
│  │  └──────────────────────────────────────────────────────────────────────┘   │  │
│  │                                                                              │  │
│  │  Ports exposés à l'hôte : 80 (Nginx/Frontend) · 8000 (FastAPI, dev)          │  │
│  └──────────────────────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## Section 3 — Moteur de détection

### 3.1 Pipeline de corrélation — 5 étapes

```text
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │                                                                             │
 │  [1. RAW]                     Événements bruts entrants                     │
 │  ─── heartbeat, events agent, traffic captures, scan results               │
 │         │                                                                    │
 │         ▼                                                                    │
 │  [2. NORMALISATION]          Parsing → structure commune                   │
 │  ─── Celery worker, validation Pydantic + regex                            │
 │  ─── Rejet des malformés → audit log si échec                              │
 │         │                                                                    │
 │         ▼                                                                    │
 │  [3. ENRICHISSEMENT]         Contexte ajouté à l'événement                 │
 │  ─── Résolution DNS inverse (socket.gethostbyaddr)                         │
 │  ─── Lookup actifs connus (table assets PostgreSQL)                        │
 │  ─── Agrégation temporelle (fenêtre glissante Redis)                       │
 │  ─── Calcul de métriques (compteurs par IP, port, type)                    │
 │         │                                                                    │
 │         ▼                                                                    │
 │  [4. ÉVALUATION DES RÈGLES]  Parcours des règles actives (JSONB)          │
 │  ─── Filtrage : type d'événement correspond-il à la règle ?                │
 │  ─── Agrégation : métriques dans la fenêtre temporelle                     │
 │  ─── Comparaison : la métrique dépasse-t-elle le seuil ?                   │
 │  ─── Déduplication : alerte similaire déjà générée dans les N minutes ?    │
 │         │                                                                    │
 │         ├── Condition vraie ─────────────────────────────────────┐          │
 │         │                                                       │          │
 │         ▼                                                       ▼          │
 │  [5a. GÉNÉRATION ALERTE]                                [5b. LOG]          │
 │  ─── Création entrée alerts (PostgreSQL)                     │             │
 │  ─── Statut new, horodatage created_at                      │             │
 │  ─── Lien avec événement source                              │             │
 │                                                              │             │
 │                    ┌─────────────────────────────────────────┘             │
 │                    ▼                                                       │
 │  [FIN]  Événement persiste dans events (traçabilité)                       │
 └─────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Types de règles — 7 règles supportées

#### R1 — Frequency Threshold (Seuil de fréquence)

Détecte un nombre anormalement élevé de connexions depuis une même IP.
- **Déclencheur** : Connexions TCP répétées depuis une même IP
- **Métrique** : `connection_count` | **Fenêtre** : 60 s | **Seuil** : ≥ 50 | **Sévérité** : MEDIUM
- **Suppression** : 300 s

```json
{
  "id": "rule_freq_threshold",
  "name": "Seuil de fréquence de connexions",
  "enabled": true, "category": "anomaly",
  "conditions": {
    "event_type": "connection_attempt", "metric": "connection_count",
    "operator": ">=", "threshold": 50, "window_seconds": 60, "group_by": ["source_ip"]
  },
  "severity": "MEDIUM", "suppression_seconds": 300
}
```

#### R2 — Sensitive Port (Port sensible exposé)

Alerte si un port sensible (SSH, RDP, base de données) est ouvert.
- **Déclencheur** : Port 22, 3389, 3306, 5432, 6379 ouvert
- **Métrique** : `port_state = 'open'` | **Temps réel** | **Seuil** : 1 | **Sévérité** : HIGH
- **Suppression** : 600 s

```json
{
  "id": "rule_sensitive_port",
  "name": "Port sensible exposé",
  "enabled": true, "category": "exposure",
  "conditions": {
    "event_type": "port_finding", "metric": "port_in_list",
    "sensitive_ports": [22, 3389, 3306, 5432, 6379, 27017],
    "operator": "==", "threshold": 1
  },
  "severity": "HIGH", "suppression_seconds": 600
}
```

#### R3 — Unexpected Service (Service inattendu)

Détecte un service HTTP sur un port non standard (> 1024).
- **Déclencheur** : HTTP sur port > 1024 non standard
- **Métrique** : `service != expected` | **Temps réel** | **Seuil** : 1 | **Sévérité** : MEDIUM
- **Suppression** : 600 s

```json
{
  "id": "rule_unexpected_service",
  "name": "Service inattendu",
  "enabled": true, "category": "anomaly",
  "conditions": {
    "event_type": "service_detection", "service": "http",
    "port_operator": ">", "port_threshold": 1024,
    "operator": "==", "threshold": 1
  },
  "severity": "MEDIUM", "suppression_seconds": 600
}
```

#### R4 — New Host (Nouvel hôte détecté)

Alerte quand une adresse IP inconnue est découverte sur le réseau.
- **Déclencheur** : IP inconnue apparaît dans le périmètre
- **Métrique** : `ip not in assets` | **Temps réel** | **Seuil** : 1 | **Sévérité** : LOW
- **Suppression** : 3600 s

```json
{
  "id": "rule_new_host",
  "name": "Nouvel hôte détecté",
  "enabled": true, "category": "discovery",
  "conditions": {
    "event_type": "host_discovery", "metric": "is_new_host",
    "operator": "==", "threshold": true
  },
  "severity": "LOW", "suppression_seconds": 3600
}
```

#### R5 — Heartbeat Loss (Perte de HeartBeat)

Alerte si un endpoint supervisé n'a pas envoyé de signal depuis trop longtemps.
- **Déclencheur** : Absence de signal d'un endpoint connu
- **Métrique** : `seconds_since_last` | **Continue** | **Seuil** : > 180 s | **Sévérité** : HIGH
- **Vérification** : toutes les 30 s | **Suppression** : 300 s

```json
{
  "id": "rule_heartbeat_loss",
  "name": "Perte de HeartBeat",
  "enabled": true, "category": "availability",
  "conditions": {
    "event_type": "heartbeat_check", "metric": "seconds_since_last_heartbeat",
    "operator": ">", "threshold": 180, "check_interval_seconds": 30
  },
  "severity": "HIGH", "suppression_seconds": 300
}
```

#### R6 — Port Scan (Scan de ports détecté)

Détecte un scan de ports (même IP contacte de nombreux ports distincts).
- **Déclencheur** : Même IP contacte N ports distincts
- **Métrique** : `distinct_ports` | **Fenêtre** : 30 s | **Seuil** : ≥ 20 | **Sévérité** : HIGH
- **Suppression** : 300 s

```json
{
  "id": "rule_port_scan",
  "name": "Scan de ports détecté",
  "enabled": true, "category": "attack",
  "conditions": {
    "event_type": "connection_attempt", "metric": "distinct_ports_contacted",
    "operator": ">=", "threshold": 20, "window_seconds": 30,
    "group_by": ["source_ip"]
  },
  "severity": "HIGH", "suppression_seconds": 300
}
```

#### R7 — Out-of-Hours (Trafic hors plage horaire)

Détecte une connexion établie en dehors des heures de travail configurées.
- **Déclencheur** : Connexion hors horaires configurés
- **Métrique** : `hour_of_day` | **Temps réel** | **Seuil** : hors [8h–20h] | **Sévérité** : MEDIUM
- **Jours autorisés** : lun–ven | **Suppression** : 600 s

```json
{
  "id": "rule_out_of_hours",
  "name": "Trafic hors plage horaire",
  "enabled": true, "category": "anomaly",
  "conditions": {
    "event_type": "connection_established", "metric": "hour_of_day",
    "operator": "not_between",
    "business_hours": { "start": 8, "end": 20 },
    "allowed_days": ["monday", "tuesday", "wednesday", "thursday", "friday"]
  },
  "severity": "MEDIUM", "suppression_seconds": 600
}
```

### 3.3 Stockage des règles — PostgreSQL JSONB

Table `rules` :

| Colonne | Type | Contrainte | Description |
|---|---|---|---|
| `id` | VARCHAR(32) | PK | Identifiant unique lisible (ex: `rule_port_scan`) |
| `name` | VARCHAR(128) | NOT NULL | Nom lisible de la règle |
| `description` | TEXT | NULLABLE | Description longue |
| `enabled` | BOOLEAN | DEFAULT TRUE | Activation/désactivation à chaud |
| `category` | VARCHAR(32) | NOT NULL | anomaly, exposure, attack, availability, discovery |
| `conditions` | JSONB | NOT NULL | Expression JSON complète de la règle |
| `severity` | VARCHAR(8) | NOT NULL, CHECK IN | LOW, MEDIUM, HIGH, CRITICAL |
| `suppression_seconds` | INTEGER | DEFAULT 300 | Intervalle minimum entre deux alertes identiques |
| `created_at` | TIMESTAMPTZ | DEFAULT NOW() | Date de création |
| `updated_at` | TIMESTAMPTZ | DEFAULT NOW() | Dernière modification |

Indexation :

```sql
CREATE INDEX idx_rules_conditions ON rules USING GIN (conditions);
CREATE INDEX idx_rules_enabled ON rules (enabled) WHERE enabled = true;
CREATE INDEX idx_rules_category ON rules (category);
```

### 3.4 Cycle de vie d'une alerte

```
   ┌──────────┐
   │   NEW    │  ─── Alerte générée par le moteur de corrélation
   └────┬─────┘
        │ Analyste commence le traitement
        ▼
   ┌──────────┐
   │IN_PROGRESS│  ─── Analyste qualifie l'alerte (commentaire, sévérité)
   └────┬─────┘
        │
        ├── Analyste confirme l'incident
        │      ▼
        │ ┌──────────┐
        │ │ RESOLVED │  ─── Incident traité, preuve exportée si nécessaire
        │ └──────────┘
        │
        └── Analyste identifie un faux positif
               ▼
          ┌──────────┐
          │ DISMISSED│  ─── Alerte marquée comme faux positif
          └──────────┘
```

### 3.5 Orchestration Celery

| Tâche | Déclencheur | Fréquence | Description |
|---|---|---|---|
| `detect_events` | Signal Celery Beat | 30 s | Traite les événements non encore corrélés |
| `check_heartbeats` | Signal Celery Beat | 30 s | Vérifie l'état des heartbeats (Règle R5) |
| `run_scan` | Requête utilisateur (POST /scan) | À la demande | Exécute un scan Nmap + détection post-scan |

### 3.6 Métriques de performance

| Métrique | Cible | Condition |
|---|---|---|
| Latence de détection (entrée → alerte) | < 60 s | 100 événements/s |
| Capacité de traitement | 500 événements/s | Par worker Celery |
| Temps d'évaluation d'une règle | < 10 ms | Par événement, règle typique |
| Déduplication | 0 alerte en double | Même fenêtre de suppression |
| Règles actives simultanées | Jusqu'à 50 | Sans dégradation mesurable |

### 3.7 Évolutions v2+

| Fonctionnalité | Description |
|---|---|
| Règles composées (AND/OR) | Combinaison de plusieurs conditions dans une même règle |
| Seuils adaptatifs | Ajustement automatique basé sur le bruit de fond |
| Détection comportementale (ML) | Modèle d'apprentissage supervisé pour les anomalies |
| Corrélation inter-événements | Chaînage d'alertes (scan → brute-force → compromission) |
| Notifications temps réel | WebSocket, webhook, email |
| Dashboard conformité NIS2 | Vue dédiée avec indicateurs réglementaires |

---

## Section 4 — Sources

### 4.1 Technologies de la stack

| Technologie | Lien officiel | Version |
|---|---|---|
| [Python](https://www.python.org/) | [Documentation](https://docs.python.org/3.11/) | 3.11+ |
| [FastAPI](https://fastapi.tiangolo.com/) | [Documentation](https://fastapi.tiangolo.com/) | 0.110+ |
| [SQLAlchemy](https://www.sqlalchemy.org/) | [Documentation](https://docs.sqlalchemy.org/en/20/) | 2.x |
| [Pydantic](https://docs.pydantic.dev/) | [Documentation](https://docs.pydantic.dev/latest/) | 2.x |
| [Alembic](https://alembic.sqlalchemy.org/) | [Documentation](https://alembic.sqlalchemy.org/) | Latest |
| [Bootstrap](https://getbootstrap.com/) | [Documentation](https://getbootstrap.com/docs/5.3/) | 5.x |
| [PostgreSQL](https://www.postgresql.org/) | [Documentation](https://www.postgresql.org/docs/15/) | 15+ |
| [Redis](https://redis.io/) | [Documentation](https://redis.io/documentation) | 7.x |
| [Celery](https://docs.celeryq.dev/) | [Documentation](https://docs.celeryq.dev/en/stable/) | 5.x |
| [Nmap](https://nmap.org/) | [Documentation](https://nmap.org/docs.html) | 7.94+ |
| [Scapy](https://scapy.net/) | [Documentation](https://scapy.readthedocs.io/) | Latest |
| [tcpdump](https://www.tcpdump.org/) | [Site officiel](https://www.tcpdump.org/) | Latest |
| [Nginx](https://nginx.org/) | [Documentation](https://nginx.org/en/docs/) | 1.25+ |
| [pytest](https://docs.pytest.org/) | [Documentation](https://docs.pytest.org/) | Latest |
| [httpx](https://www.python-httpx.org/) | [Documentation](https://www.python-httpx.org/) | Latest |
| [GitHub Actions](https://docs.github.com/en/actions) | [Documentation](https://docs.github.com/en/actions) | — |
| [Docker Compose](https://docs.docker.com/compose/) | [Documentation](https://docs.docker.com/compose/) | V2 |

### 4.2 Sécurité et standards

| Technologie / Standard | Lien officiel | Rôle |
|---|---|---|
| [JWT](https://jwt.io/) | [Introduction](https://jwt.io/introduction) | Authentification par tokens |
| [bcrypt](https://pypi.org/project/bcrypt/) | [PyPI](https://pypi.org/project/bcrypt/) | Hachage des mots de passe |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | [OWASP](https://owasp.org/www-project-application-security-verification-standard/) | Standard de sécurité applicatif (niveau 2 visé) |
| [NIS2 Directive](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive) | [Commission européenne](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive) | Directive européenne sur la sécurité des réseaux |
| [RGPD](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679) | [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679) | Règlement général sur la protection des données |

### 4.3 Visualisation

| Technologie | Lien officiel | Usage |
|---|---|---|
| [Vis.js](https://visjs.org/) | [Documentation](https://visjs.org/) | Visualisation de graphes réseau |
| [D3.js](https://d3js.org/) | [Documentation](https://d3js.org/) | Visualisations de données dynamiques |

### 4.4 Documents internes du projet

| Document | Emplacement | Rôle |
|---|---|---|
| Architecture technique BigBrowser | [`/documents/08_architecture/architecture_technique_bigbrowser.md`](../architecture_technique_bigbrowser.md) | Document principal de référence technique |
| Rapport d'architecture principal | [`/documents/08_architecture/rendu_principal.md`](../rendu_principal.md) | Version synthétique et défendable de l'architecture |
| Schéma d'architecture (PNG) | [`/documents/08_architecture/assets/schema_d'architecture.png`](../assets/schema_d'architecture.png) | Schéma conceptuel bigbrowser |
| Cahier des charges | [`/documents/06_cahier_des_charges/rendu_principal.md`](../../06_cahier_des_charges/rendu_principal.md) | Exigences fonctionnelles et non fonctionnelles |
| Feuille de cadrage projet | [`/documents/01_documents_pedagogiques/README.md`](../../01_documents_pedagogiques/README.md) | Périmètre projet, objectifs |
| Business Model | [`/documents/03_business_model/rendu_principal.md`](../../03_business_model/rendu_principal.md) | Modèle open-core |
| Business Plan | [`/documents/04_business_plan/rendu_principal.md`](../../04_business_plan/rendu_principal.md) | Projections financières |
| Étude de marché | [`/documents/02_etude_de_marche/rendu_principal.md`](../../02_etude_de_marche/rendu_principal.md) | Analyse concurrentielle |
| Matrice de gestion des risques | [`/documents/05_gestion_de_projet/rendu_principal.md`](../../05_gestion_de_projet/rendu_principal.md) | Risques identifiés |

### 4.5 Bonnes pratiques et guides externes

| Sujet | Source | Lien |
|---|---|---|
| Structuration projet FastAPI | FastAPI Best Practices | [github.com/zhanymkanov/fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices) |
| Modèle de corrélation SIEM | OSSEM | [github.com/OTRF/OSSEM](https://github.com/OTRF/OSSEM) |
| Détection par règles | Sigma | [github.com/SigmaHQ/sigma](https://github.com/SigmaHQ/sigma) |
| Architecture N-tiers | Martin Fowler | Ouvrage de référence |
| API-first design | Microsoft REST API Guidelines | [github.com/microsoft/api-guidelines](https://github.com/microsoft/api-guidelines) |

### 4.6 Registre de traçabilité

| Exigence (CDC) | Décision architecturale | Référence |
|---|---|---|
| F-AUTH-001 (Authentification) | JWT avec rôles admin/analyst | Module `auth`, `security.py` |
| F-DISC-001 (Scan réseau) | Nmap en subprocess via Celery worker | Module `discovery`, `scan_service.py` |
| F-ALERT-001 (Détection) | Règles JSONB + pipeline 5 étapes | Section 3 — Moteur de détection |
| F-EXP-001 (Export CSV) | Celery task → génération fichier → download endpoint | Module `reports` |
| F-AUD-001 (Audit) | Middleware FastAPI + table audit_logs | Module `audit` |
| SEC-003 (Validation entrées) | Pydantic + regex (CIDR, IP, ports) | `core/`, tous les schémas |
| NF-PERF-001 (Latence < 2 s) | Traitement asynchrone Celery | `tasks/` |
| NF-DEP-001 (On-premise) | Docker Compose, aucune dépendance cloud | `docker-compose.yml` |
| NF-TEST-001 (Testabilité) | pytest + httpx, architecture modulaire | `tests/` |

| Risque | Décision architecturale |
|---|---|
| R-T01 (Faux positifs) | Seuils configurables, `suppression_seconds`, statut `dismissed` |
| R-T02 (Blocage IDS) | Délais inter-requêtes configurables, mode SYN scan optionnel |
| R-T03 (Latence UI) | Celery + Redis pour tous les traitements > 2 s |
| R-S01 (Injection commandes) | Validation Pydantic + regex, jamais de shell concaténé |
| R-S02 (Exposition données) | PostgreSQL isolé sur réseau interne, exports contrôlés par rôle |
| R-P01 (Rupture planning) | Architecture modulaire permettant le travail parallèle Front/Back |

### 4.7 Licence et conformité

| Aspect | Détail |
|---|---|
| Licence du projet | GPLv2 ou Apache 2.0 (arbitrage juridique en cours) |
| Conformité RGPD | Données 100 % on-premise, pas d'envoi externe, journalisation des accès |
| Conformité NIS2 | Supervision continue, traçabilité complète, exports structurés |
| OWASP ASVS niveau | Niveau 2 (standard) visé pour la v1 |

---

*Document consolidé — BigBrowser — Mai 2026*
