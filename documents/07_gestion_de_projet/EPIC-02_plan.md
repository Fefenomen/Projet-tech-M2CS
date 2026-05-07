# EPIC-02 — Docker Lab de Démonstration

**Date de création :** Mai 2026  
**Chef de projet :** @project-manager-tech  
**Statut :** En cours  
**Objectif :** Environnement Docker reproductible avec 3 zones (Attaquant, Endpoints, SOC) pour la démo NIS2

---

## Contexte

L'EPIC-02 construit l'environnement de démonstration Docker décrit dans l'architecture définitive. Le lab permet de reproduire le scénario complet : scan → détection → alertes → export de preuve NIS2 — en une commande `./demo.sh`.

**Topologie :**
- Zone **SOC** : Conteneur FastAPI + SQLite + Frontend Bootstrap
- Zone **Endpoints** : 2 conteneurs supervisés avec agent heartbeat
- Zone **Attaquant** : Conteneur offensif avec scénarios contrôlés
- Réseau **BBrowser_net** : 172.20.0.0/24 isolé

---

## User Stories (US-02.x)

### US-02.1 — Docker Compose : SOC container (backend + DB + frontend)

| Élément | Détail |
|---------|--------|
| **ID** | US-02.1 |
| **Objectif** | Dockeriser le SOC (FastAPI + SQLite + Frontend) |
| **Fichiers** | `product/docker/Dockerfile.soc`, `docker-compose.yml` |
| **Agent** | @devops-engineer |
| **Critères d'acceptation** | `docker compose up` → API sur :8000, frontend servi, DB persistée |
| **Statut** | 🔄 En cours |

### US-02.2 — Réseau Docker BBrowser_net + configuration

| Élément | Détail |
|---------|--------|
| **ID** | US-02.2 |
| **Objectif** | Configurer le réseau isolé 172.20.0.0/24 |
| **Fichiers** | `product/docker/docker-compose.yml` (section networks) |
| **Agent** | @devops-engineer |
| **Critères d'acceptation** | Ping entre conteneurs, pas d'accès externe inutile |
| **Statut** | 🔄 En cours |

### US-02.3 — Agent Endpoint : Heartbeat + events vers l'API

| Élément | Détail |
|---------|--------|
| **ID** | US-02.3 |
| **Objectif** | Agent Python léger envoyant heartbeats et événements au SOC |
| **Fichiers** | `product/agent/agent.py`, `product/agent/Dockerfile.endpoint` |
| **Agent** | @backend-python-dev |
| **Critères d'acceptation** | Heartbeat toutes les 30s, collecte logs, authentification API |
| **Statut** | 📋 Backlog |

### US-02.4 — Endpoint Docker : conteneur supervisé avec logs

| Élément | Détail |
|---------|--------|
| **ID** | US-02.4 |
| **Objectif** | Conteneur Endpoint avec nginx + agent |
| **Fichiers** | `product/docker/Dockerfile.endpoint`, `product/agent/entrypoint.sh` |
| **Agent** | @devops-engineer |
| **Critères d'acceptation** | nginx accessible, agent heartbeat, détectable par scan |
| **Statut** | 📋 Backlog |

### US-02.5 — Attaquant Docker : scénarios de simulation

| Élément | Détail |
|---------|--------|
| **ID** | US-02.5 |
| **Objectif** | Conteneur Attaquant avec scénarios contrôlés |
| **Fichiers** | `product/attacker/scenarios.py`, `product/docker/Dockerfile.attacker` |
| **Agent** | @devops-engineer |
| **Critères d'acceptation** | Scan de ports, HTTP flood, failed logins — pas de code destructeur |
| **Statut** | 📋 Backlog |

### US-02.6 — Script demo.sh : orchestration en 1 commande

| Élément | Détail |
|---------|--------|
| **ID** | US-02.6 |
| **Objectif** | Script unique pour lancer/stopper/reset le lab |
| **Fichiers** | `product/docker/demo.sh` |
| **Agent** | @devops-engineer |
| **Critères d'acceptation** | `./demo.sh demo` lance tout, exécute le scénario, affiche les résultats |
| **Statut** | 📋 Backlog |

### US-02.7 — Documentation lab + guide de reproduction

| Élément | Détail |
|---------|--------|
| **ID** | US-02.7 |
| **Objectif** | Documentation complète du lab pour reproduction |
| **Fichiers** | `product/docker/README.md` |
| **Agent** | @devops-engineer |
| **Critères d'acceptation** | Un tiers peut reproduire la démo sans aide |
| **Statut** | 📋 Backlog |

---

## Planning Prévisionnel

| Sprint | US | Livrable | Jalons |
|---|---|---|---|
| Sprint 7 (J1-2) | US-02.1, US-02.2 | Docker Compose + SOC | Lab structuré |
| Sprint 8 (J3-4) | US-02.3, US-02.4 | Agent + Endpoints | Télémétrie active |
| Sprint 9 (J5-6) | US-02.5, US-02.6 | Attaquant + demo.sh | Démo complète |
| Sprint 10 (J7-8) | US-02.7 | Documentation | Reproductibilité |

---

## Prochaines Actions

1. 🔄 **US-02.1** — Dockerfile SOC + docker-compose.yml — **EN COURS**
2. 🔄 **US-02.2** — Réseau BBrowser_net — **EN COURS** (inclus dans docker-compose)
3. 📋 **US-02.3** — Agent Endpoint — **À FAIRE (Sprint 8)**
4. 📋 **US-02.4** — Endpoint Docker — **À FAIRE (Sprint 8)**
5. 📋 **US-02.5** — Attaquant Docker — **À FAIRE (Sprint 9)**
6. 📋 **US-02.6** — Script demo.sh — **À FAIRE (Sprint 9)**
7. 📋 **US-02.7** — Documentation lab — **À FAIRE (Sprint 10)**

---

**Document créé par :** @project-manager-tech  
**Date :** Mai 2026  
**Version :** 1.0
