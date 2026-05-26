# Références — Gestion de Projet BigBrowser

**Dernière mise à jour :** Mai 2026  
**Responsable :** @project-manager-tech  
**Statut global :** ✅ 85 tests, 100% passing, 21 endpoints API, 26 US totales

---

## Section 1 — EPIC-01 : MVP BigBrowser (14 US, 6 sprints, vélocité)

**Statut :** ✅ Terminé — 14/14 User Stories livrées  
**Objectif :** Livrer le MVP démontrable avec les 8 fonctionnalités core (scan réseau → détection → alertes → exports)

**Stack imposée :** Python / FastAPI / HTML/CSS/JS / SQLite  
**Déploiement :** On-premise  
**Planning :** 6 sprints de 2 jours (12 jours ouvrés)

### User Stories (US-01.1 à US-01.14)

| Sprint | Jours | US livrées | Détail | US cumulées | Tests cumulés |
|---|---|---|---|---|---|
| Sprint 1 | J1-2 | US-01.1 à US-01.4 | Health Check, Skeleton FastAPI, SQLite, Data Models | 4 | 4 |
| Sprint 2 | J3-4 | US-01.5, US-01.6 | Auth JWT + RBAC + seed admin/analyst | 6 | 22 |
| Sprint 3 | J5-6 | US-01.7, US-01.8 | Scan réseau borné + inventaire actifs/ports | 8 | 35 |
| Sprint 4 | J7-8 | US-01.9, US-01.10 | Génération d'alertes + cycle de vie (nouvelle → en cours → cloturee) | 10 | 54 |
| Sprint 5 | J9-10 | US-01.11, US-01.12 | Exports CSV/JSON + Audit logs | 12 | 68 |
| Sprint 6 | J11-12 | US-01.13, US-01.14 | Dashboard API (métriques) + Frontend Bootstrap SPA | 14 | 73 |

### Suivi de Vélocité

| Sprint | US planifiées | US livrées | Vélocité |
|---|---|---|---|
| Sprint 1 | 4 | 4 | 4 |
| Sprint 2 | 2 | 2 | 2 |
| Sprint 3 | 2 | 2 | 2 |
| Sprint 4 | 2 | 2 | 2 |
| Sprint 5 | 2 | 2 | 2 |
| Sprint 6 | 2 | 2 | 2 |
| **Total** | **14** | **14** | **2,33/sprint** |

### Modules Backend Développés

- `health` — Endpoint de santé
- `auth` — Authentification JWT + RBAC
- `telemetry` — Heartbeat + events agent
- `discovery` — Scan réseau borné (validation Pydantic + regex)
- `assets` — Inventaire des actifs et ports
- `alerts` — Moteur d'alertes + cycle de vie (machine à états)
- `reports` — Exports CSV/JSON
- `audit` — Journalisation des actions sensibles
- `dashboard` — Métriques agrégées
- `traffic` — Capture de flux réseau

### Risques Identifiés (EPIC-01)

| ID | Risque | Criticité | Mitigation |
|---|---|---|---|
| R-P01 | Rupture planning (12 jours, 14 US) | 🔴 20 | Priorisation stricte P1, livraison incrémentale |
| R-T01 | Faux positifs alertes | 🟡 12 | Tests sur réseaux variés, seuils configurables |
| R-T02 | Blocage IDS lors scan | 🟡 12 | Délais inter-requêtes configurables, scan furtif |
| R-S01 | Injection champs IP | 🟡 10 | Validation Pydantic + regex stricte |
| R-S05 | Exposition secrets GitHub | 🟡 10 | `.env` dans `.gitignore`, `.env.example` documenté |

---

## Section 2 — EPIC-02 : Lab Docker (12 US, 3 zones BBrowser_net)

**Statut :** ✅ Terminé — 12/12 User Stories livrées  
**Objectif :** Environnement Docker reproductible avec 3 zones pour la démonstration NIS2

### Topologie

- **SOC** (Docker Container SOC) : FastAPI + SQLite + Frontend Bootstrap
- **Endpoints** : 2 conteneurs supervisés avec agent heartbeat
- **Attaquant** : Conteneur offensif avec scénarios contrôlés
- **Réseau isolé BBrowser_net** : 172.20.0.0/24

### User Stories (US-02.1 à US-02.12)

| US | Titre | Agent |
|---|---|---|
| US-02.1 | Docker Compose : SOC Container | @devops-engineer |
| US-02.2 | Réseau Docker BBrowser_net | @devops-engineer |
| US-02.3 | Agent Endpoint : Heartbeat + Events | @backend-python-dev |
| US-02.4 | Endpoint Docker : Conteneur supervisé (nginx + agent) | @devops-engineer |
| US-02.5 | Attaquant Docker : Scénarios contrôlés (scan, flood, failed login) | @devops-engineer |
| US-02.6 | Script demo.sh : Orchestration (1 commande) | @devops-engineer |
| US-02.7 | Documentation lab | @devops-engineer |
| US-02.8 | Audit des connexions utilisateurs (login tracking) | @security-tech-lead |
| US-02.9 | Alertes automatiques depuis télémétrie (3 strikes → alerte) | @backend-python-dev |
| US-02.10 | Capture de trafic réseau (module traffic) | @backend-python-dev |
| US-02.11 | Interface de filtrage des alertes (UI statut/sévérité) | @backend-python-dev |
| US-02.12 | Audit de création d'utilisateurs | @security-tech-lead |

### Réseau BBrowser_net — 172.20.0.0/24

| Propriété | Valeur |
|---|---|
| Plage IP | 172.20.0.0/24 |
| SOC (FastAPI) | 172.20.0.2 |
| Endpoint 1 | 172.20.0.10 |
| Endpoint 2 | 172.20.0.11 |
| Attaquant | 172.20.0.100 |
| Driver | bridge (Docker) |
| Isolation | Aucun accès réseau externe |

### Planning

6 sprints additionnels (Sprint 7 à 12) avec 2 US par sprint en moyenne.

### Matrice de Traçabilité EPIC-02

| Besoin | US associées |
|---|---|
| Déploiement Docker reproductible | US-02.1, US-02.6 |
| Réseau isolé de démonstration | US-02.2 |
| Télémétrie depuis endpoints | US-02.3, US-02.4 |
| Scénarios offensifs contrôlés | US-02.5 |
| Documentation de reproduction | US-02.7 |
| Traçabilité des connexions | US-02.8 |
| Détection automatique (3 strikes) | US-02.9 |
| Capture de trafic réseau | US-02.10 |
| Filtrage UI des alertes | US-02.11 |
| Audit des actions admin | US-02.12 |

---

## Section 3 — Résultats des Sprints (S1→S6, 85 tests, 21 endpoints, 26 US)

### Synthèse Globale

| Métrique | Valeur |
|---|---|
| Sprints exécutés | 6 |
| EPIC couverts | 2 (EPIC-01 MVP, EPIC-02 Docker Lab) |
| User Stories totales | 26 (14 EPIC-01 + 12 EPIC-02) |
| Tests automatisés | 85 (100% passing) |
| Endpoints API | 21 |
| Commits | 17+ |
| Fichiers Python backend | 20+ |
| Modules backend | 10 |
| Pages frontend | 6 (Login, Dashboard, Actifs, Alertes, Exports, Audit) |
| Zones Docker | 3 (SOC, Endpoints, Attaquant) |
| Vélocité moyenne | 4,33 US/sprint |

### Progression des Tests

| Sprint | Tests cumulés | Tests ajoutés | % passing |
|---|---|---|---|
| Sprint 1 | 4 | 4 | 100% |
| Sprint 2 | 22 | +18 | 100% |
| Sprint 3 | 35 | +13 | 100% |
| Sprint 4 | 54 | +19 | 100% |
| Sprint 5 | 68 | +14 | 100% |
| Sprint 6 | 73 | +5 | 100% |
| EPIC-02 (extra) | 85 | +12 | 100% |

### Progression des User Stories

| Sprint | US sprint | US cumulées | Progression |
|---|---|---|---|
| Sprint 1 | 4 | 4 | 15% |
| Sprint 2 | 2 | 6 | 23% |
| Sprint 3 | 2 | 8 | 31% |
| Sprint 4 | 2 | 10 | 38% |
| Sprint 5 | 2 | 12 | 46% |
| Sprint 6 | 2 | 14 | 54% |
| EPIC-02 | 12 | 26 | 100% |

### Endpoints API (21)

| # | Méthode | Endpoint | Module | Accès |
|---|---|---|---|---|
| 1 | `GET` | `/health/` | health | Public |
| 2 | `GET` | `/` | main | Public (frontend) |
| 3 | `POST` | `/api/v1/auth/login` | auth | Public |
| 4 | `GET` | `/api/v1/auth/me` | auth | Authentifié |
| 5 | `POST` | `/api/v1/auth/users` | auth | Admin |
| 6 | `POST` | `/api/v1/telemetry/heartbeat` | telemetry | Agent |
| 7 | `POST` | `/api/v1/telemetry/events` | telemetry | Agent |
| 8 | `POST` | `/api/v1/scan/` | discovery | Admin |
| 9 | `GET` | `/api/v1/assets/` | assets | Authentifié |
| 10 | `GET` | `/api/v1/assets/{id}` | assets | Authentifié |
| 11 | `GET` | `/api/v1/alerts/` | alerts | Authentifié |
| 12 | `GET` | `/api/v1/alerts/{id}` | alerts | Authentifié |
| 13 | `POST` | `/api/v1/alerts/` | alerts | Authentifié |
| 14 | `PATCH` | `/api/v1/alerts/{id}` | alerts | Authentifié |
| 15 | `GET` | `/api/v1/dashboard/` | dashboard | Authentifié |
| 16 | `POST` | `/api/v1/exports/` | reports | Authentifié |
| 17 | `GET` | `/api/v1/exports/{id}/download` | reports | Authentifié |
| 18 | `GET` | `/api/v1/audit-logs/` | audit | Admin |
| 19 | `GET` | `/api/v1/audit-logs/{id}` | audit | Admin |
| 20 | `POST` | `/api/v1/traffic/` | traffic | Authentifié |
| 21 | `GET` | `/api/v1/traffic/` | traffic | Authentifié |

### Matrice de Risk Scoring Finale

| ID | Risque | P | I | Criticité | Statut |
|---|---|---|---|---|---|
| R-P01 | Rupture de planning | 4 | 5 | **20** | ✅ Mitigé |
| R-M01 | Adoption insuffisante open-source | 4 | 4 | **16** | ⏳ Post-MVP |
| R-M03 | Difficulté recrutement cyber | 4 | 4 | **16** | ⏳ Post-MVP |
| R-T01 | Faux positifs alertes | 4 | 3 | **12** | ✅ Mitigé |
| R-T02 | Blocage IDS lors scan | 3 | 4 | **12** | ✅ Mitigé |
| R-P02 | Conflits Git | 3 | 4 | **12** | ✅ Aucun conflit majeur |
| R-S01 | Injection de commandes | 2 | 5 | **10** | ✅ Mitigé |
| R-P03 | Défaut de preuve en démonstration | 2 | 5 | **10** | ✅ Mitigé |
| R-S05 | Exposition secrets GitHub | 2 | 5 | **10** | ✅ Mitigé |
| R-T03 | Latence UI | 3 | 3 | **9** | ✅ Mitigé |
| R-M02 | Concurrence (Wazuh, PRTG) | 3 | 3 | **9** | ⏳ Post-MVP |
| R-S02 | Exposition données exports | 2 | 4 | **8** | ✅ Mitigé |

### État Final du Projet

| Composant | Statut |
|---|---|
| **EPIC-01 : MVP** (14 US) | ✅ 100% |
| **EPIC-02 : Docker Lab** (12 US) | ✅ 100% |
| **Tests** | ✅ 85 tests — 100% passing |
| **Endpoints API** | ✅ 21 endpoints |
| **Frontend** | ✅ Bootstrap SPA (6 pages) |
| **Docker** | ✅ 3 zones, 1 commande |
| **Sécurité** | ✅ RBAC, JWT, validation, audit |
| **Preuve NIS2** | ✅ Exports CSV/JSON |

---

## Section 4 — Sources

### Documents Projet

- [EPIC-01_plan.md](../EPIC-01_plan.md) — Plan détaillé du MVP (14 US, critères d'acceptation, risques)
- [EPIC-02_plan.md](../EPIC-02_plan.md) — Plan du lab Docker (12 US, topologie 3 zones)
- Rapports de sprint : [RAPPORT_SPRINT1](../RAPPORT_SPRINT1.md) à [RAPPORT_SPRINT6](../RAPPORT_SPRINT6.md)
- [RAPPORT_JALON_6.md](../RAPPORT_JALON_6.md) — Déblocage manuel US-01.3 (DB SQLite)

### Références Externes

- [Agile/Scrum](https://www.scrum.org/) — Méthodologie Agile pour la gestion de projet
- [GitHub Issues](https://docs.github.com/en/issues) — Suivi des User Stories et bugs
- [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects) — Planification et suivi visuel des sprints
- [Docker Compose](https://docs.docker.com/compose/) — Orchestration multi-conteneurs du lab
- [Docker networking](https://docs.docker.com/network/) — Configuration réseau BBrowser_net
- [pytest](https://docs.pytest.org/) — Framework de tests automatisés (85 tests)
- [FastAPI](https://fastapi.tiangolo.com/) — Framework backend Python (21 endpoints)
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM pour la persistance SQLite/PostgreSQL
- [JWT.io](https://jwt.io/) — Authentification par tokens JWT
- [bcrypt](https://pypi.org/project/bcrypt/) — Hash des mots de passe utilisateur
- [Bootstrap 5](https://getbootstrap.com/) — Interface web responsive (6 pages)
- [OpenCode](https://github.com/opencode-ai) — Agents IA pour le développement assisté

### Conventions de Nommage

| Élément | Convention | Exemple |
|---|---|---|
| EPIC | `EPIC-NN` | EPIC-01, EPIC-02 |
| User Story | `US-NN.M` | US-01.1, US-02.8 |
| Sprint | `Sprint N` | Sprint 1, Sprint 6 |
| Rapport Sprint | `RAPPORT_SPRINTN.md` | RAPPORT_SPRINT3.md |
| Rapport Jalon | `RAPPORT_JALON_N.md` | RAPPORT_JALON_6.md |

### Contact et Responsabilités

| Rôle | Agent | Responsabilité |
|---|---|---|
| Chef de projet | @project-manager-tech | Planification, coordination, validation |
| Développeur backend | @backend-python-dev | Implémentation FastAPI, modèles, routes |
| Testeur QA | @qa-tester | Tests pytest, validation fonctionnelle |
| Audit sécurité | @security-tech-lead | Revue de code, RBAC, injections |
| DevOps | @devops-engineer | Docker Compose, scripts, CI/CD |

---

*Document consolidé à partir de 01_epic01_mvp.md, 02_epic02_lab_docker.md, 03_sprints_resultats.md et 04_sources_reference.md.*  
**Créé par :** @project-manager-tech — **Date :** Mai 2026
