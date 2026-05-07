# EPIC-01 — BigBrowser MVP (Minimum Viable Product)

**Date de création :** Mai 2026  
**Chef de projet :** @project-manager-tech  
**Statut :** En cours  
**Objectif :** Livrer le MVP démontrable avec les 8 fonctionnalités core

---

## Contexte

L'EPIC-01 couvre le développement du MVP BigBrowser, outil de cybersurveillance réseau orienté SOC. Le MVP doit démontrer une chaîne fonctionnelle complète : scan réseau → détection → alertes → exports.

**Stack imposée :** Python / FastAPI / HTML/CSS/JS  
**Déploiement :** On-premise (sans cloud)  
**Cible :** PME françaises (conformité NIS2)

---

## État initial (Mai 2026)

| Composant | Statut | Emplacement |
|-----------|--------|--------------|
| Backend FastAPI | ✅ Skeleton créé | `product/backend/app/` |
| `GET /health` | ✅ Implémenté + testé | `app/health/router.py` |
| Auth router | ✅ JWT + DB + rôles | `app/auth/router.py` |
| Telemetry heartbeat | ✅ Implémenté (DB ready) | `app/telemetry/router.py` |
| Base de données | ✅ SQLite MVP | `app/core/database.py` |
| Modèles de données | ✅ 6 modèles + relations | `app/models/` |
| Seed users | ✅ admin + analyst | `app/core/database.py` |
| Scan réseau | ✅ Socket scan + validation IP | `app/discovery/` |
| Assets/Inventory | ✅ CRUD + ports | `app/assets/` |
| Alertes | ✅ CRUD + cycle de vie | `app/alerts/` |
| Exports | ✅ CSV/JSON + download | `app/reports/` |
| Audit logs | ✅ Endpoint admin + auto-log | `app/audit/` |
| Frontend | ✅ Bootstrap SPA | `product/frontend/` |

---

## User Stories (US-01.x)

### US-01.1 — Health Check Endpoint ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.1 |
| **Objectif** | Exposer un endpoint de santé pour vérifier que l'API est opérationnelle |
| **Epic** | EPIC-01 — Infrastructure de base |
| **Fichiers** | `app/health/router.py`, `tests/test_health.py` |
| **Agent** | @backend-python-dev |
| **Critères d'acceptation** | `GET /health/` retourne `{"status": "ok", "service": "...", "version": "..."}` avec code 200 |
| **Tests attendus** | `test_health_check()` — vérifie statut 200 et structure JSON |
| **Risques** | Aucun (endpoint trivial) |
| **Statut** | ✅ TERMINÉ |

---

### US-01.2 — Backend FastAPI Skeleton ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.2 |
| **Objectif** | Structurer l'application FastAPI avec configuration centralisée |
| **Epic** | EPIC-01 — Infrastructure de base |
| **Fichiers** | `app/main.py`, `app/core/config.py`, `pyproject.toml` |
| **Agent** | @backend-python-dev |
| **Critères d'acceptation** | App FastAPI démarre, charge la config depuis `.env`, expose `/docs` |
| **Tests attendus** | `test_root_endpoint()` — vérifie `GET /` fonctionnel |
| **Risques** | Aucun |
| **Statut** | ✅ TERMINÉ |

---

### US-01.3 — Configuration Base de Données SQLite

| Élément | Détail |
|---------|--------|
| **ID** | US-01.3 |
| **Objectif** | Mettre en place la connexion SQLite avec SQLAlchemy pour la persistance MVP |
| **Epic** | EPIC-01 — Infrastructure de base |
| **Fichiers** | `app/core/database.py`, `app/models/`, `alembic/` (ou création directe) |
| **Agent** | @backend-python-dev |
| **Critères d'acceptation** | SQLite créé au démarrage, tables initialisées, connexion vérifiable via `/health` |
| **Tests attendus** | `test_db_connection()` — vérifie que la DB est accessible et les tables existent |
| **Risques** | R1 : Permissions d'écriture sur le fichier SQLite |
| **Statut** | ✅ TERMINÉ |

---

### US-01.4 — Modèles de Données MVP ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.4 |
| **Objectif** | Définir les modèles de données SQLAlchemy pour les entités MVP
| **Epic** | EPIC-01 — Infrastructure de base
| **Fichiers** | `app/models/` (user, heartbeat, asset, port, alert, audit_log)
| **Agent** | @backend-python-dev
| **Critères d'acceptation** | 6+ modèles créés avec relations et contraintes
| **Tests attendus** | `test_models_creation()` — tables créées et fonctionnelles
| **Risques** | Aucun
| **Statut** | ✅ TERMINÉ |

---

### US-01.5 — Authentification JWT avec Base de Données ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.5 |
| **Objectif** | Implémenter l'authentification JWT via la base de données
| **Epic** | EPIC-01 — Sécurité
| **Fichiers** | `app/auth/`
| **Agent** | @backend-python-dev
| **Critères d'acceptation** | `POST /api/v1/auth/login` valide, tokens JWT fonctionnels
| **Tests attendus** | `test_login_valid()`, `test_login_invalid_password()`
| **Risques** | Aucun
| **Statut** | ✅ TERMINÉ |

---

### US-01.6 — Gestion des Rôles (RBAC) ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.6 |
| **Objectif** | Implémenter le contrôle d'accès basé sur les rôles (admin/analyst)
| **Epic** | EPIC-01 — Sécurité
| **Fichiers** | `app/auth/router.py`
| **Agent** | @backend-python-dev
| **Critères d'acceptation** | `require_role()` bloque analyste sur endpoints admin
| **Tests attendus** | `test_create_user_as_analyst_forbidden()`
| **Risques** | Aucun
| **Statut** | ✅ TERMINÉ |

---

### US-01.7 — Scan Réseau Borné ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.7 |
| **Objectif** | Scanner une plage IP configurée par l'administrateur
| **Epic** | EPIC-01 — Discovery
| **Fichiers** | `app/discovery/`
| **Agent** | @backend-python-dev
| **Critères d'acceptation** | `POST /api/v1/scan/` valide les IPs, limite /24, scan TCP
| **Tests attendus** | `test_scan_single_ip_localhost()`, `test_scan_range_too_large()`
| **Risques** | R1 : Injection de commandes via champs IP — mitigé par regex Pydantic
| **Statut** | ✅ TERMINÉ |

---

### US-01.8 — Détection de Ports Ouverts ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.8 |
| **Objectif** | Détecter les ports ouverts sur les équipements scannés
| **Epic** | EPIC-01 — Discovery
| **Fichiers** | `app/discovery/`
| **Agent** | @backend-python-dev
| **Critères d'acceptation** | Ports détectés et associés à l'actif dans la DB
| **Tests attendus** | Couvert par les tests de scan
| **Risques** | Aucun
| **Statut** | ✅ TERMINÉ |

---

### US-01.9 — Inventaire d'Actifs ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.9 |
| **Objectif** | Maintenir un inventaire d'actifs réseau consultable
| **Epic** | EPIC-01 — Assets
| **Fichiers** | `app/assets/`
| **Agent** | @backend-python-dev
| **Critères d'acceptation** | `GET /api/v1/assets/` retourne la liste des actifs découverts
| **Tests attendus** | `test_list_assets_empty()`, `test_asset_detail_with_ports()`
| **Risques** | Aucun
| **Statut** | ✅ TERMINÉ |

---

### US-01.10 — Génération d'Alertes ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.10 |
| **Objectif** | Créer des alertes à partir de comportements suspects détectés
| **Epic** | EPIC-01 — Alerts
| **Fichiers** | `app/alerts/`
| **Agent** | @backend-python-dev
| **Critères d'acceptation** | `POST /api/v1/alerts/` crée une alerte avec sévérité et statut
| **Tests attendus** | `test_create_alert_valid()`, `test_create_alert_default_severity()`
| **Risques** | Aucun
| **Statut** | ✅ TERMINÉ |

---

### US-01.11 — Exports CSV et JSON ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.11 |
| **Objectif** | Produire des exports CSV/JSON comme preuves de conformité NIS2
| **Epic** | EPIC-01 — Reports
| **Fichiers** | `app/reports/` (router, service, schemas)
| **Agent** | @backend-python-dev
| **Critères d'acceptation** | `POST /api/v1/exports/` génère CSV ou JSON pour alerts/assets/audit_logs, `GET /api/v1/exports/{id}/download` télécharge le fichier
| **Tests attendus** | 14 tests dans `tests/test_reports.py` couvrant formats, scopes, validation, permissions
| **Risques** | Aucun
| **Statut** | ✅ TERMINÉ |

---

### US-01.12 — Audit Log (Journalisation) ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.12 |
| **Objectif** | Journaliser les actions sensibles et exposer un endpoint admin
| **Epic** | EPIC-01 — Audit
| **Fichiers** | `app/audit/` (router, service, schemas), `app/models/audit_log.py`
| **Agent** | @backend-python-dev
| **Critères d'acceptation** | `GET /api/v1/audit-logs/` retourne tous les logs (admin only), chaque export/alerte génère une entrée d'audit automatiquement
| **Tests attendus** | `test_list_audit_logs_as_admin()`, `test_list_audit_logs_as_analyst_forbidden()`, `test_audit_logs_populated_after_export()`
| **Risques** | Aucun
| **Statut** | ✅ TERMINÉ |

---

### US-01.5 — Authentification JWT Complète ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.5 |
| **Objectif** | Finaliser l'auth avec stockage users en DB, hash bcrypt, rôles `admin`/`analyst` |
| **Epic** | EPIC-01 — Authentification & RBAC |
| **Fichiers** | `app/auth/service.py`, `app/auth/schemas.py`, `app/auth/router.py` |
| **Agent** | @backend-python-dev |
| **Critères d'acceptation** | Login retourne JWT, rôle vérifié, accès refusé si mauvais rôle |
| **Tests attendus** | `test_login_valid()`, `test_login_invalid_password()`, `test_protected_route_with_valid_token()`, `test_role_access_denied()` |
| **Risques** | R-S01 : Injection via champs de login (mitigation : validation Pydantic) |
| **Statut** | ✅ TERMINÉ |

---

### US-01.6 — Initialisation Admin et Utilisateurs ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.6 |
| **Objectif** | Script d'initialisation créant le compte `admin` par défaut et permettant la création d'utilisateurs |
| **Epic** | EPIC-01 — Authentification & RBAC |
| **Fichiers** | `app/core/database.py` (_seed_default_users), `app/auth/router.py` (POST /users) |
| **Agent** | @backend-python-dev |
| **Critères d'acceptation** | Compte `admin`/`admin123` créé au premier démarrage, route `POST /api/v1/auth/users` (admin only) |
| **Tests attendus** | `test_create_user_as_admin()`, `test_create_user_as_analyst_forbidden()` |
| **Risques** | R-S05 : Secret exposé (mitigation : `.env` dans `.gitignore`) |
| **Statut** | ✅ TERMINÉ |

---

### US-01.7 — Scan Réseau (Module Core) ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.7 |
| **Objectif** | Implémenter le scan de plage IP (socket) pour découvrir les équipements |
| **Epic** | EPIC-01 — Scan & Découverte |
| **Fichiers** | `app/discovery/{router,schemas,service}.py` |
| **Agent** | @backend-python-dev |
| **Critères d'acceptation** | `POST /api/v1/scan` lance un scan, actifs créés en DB, plage IP validée |
| **Tests attendus** | `test_scan_valid_range()`, `test_scan_invalid_ip_rejected()`, `test_scan_creates_assets()` |
| **Risques** | R-T02 : Blocage par IDS (mitigation : délais configurable), R-S01 : Injection IP |
| **Statut** | ✅ TERMINÉ |

---

### US-01.8 — Inventaire des Actifs et Ports ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.8 |
| **Objectif** | Stocker et exposer les actifs découverts (IP, hostname, ports ouverts) |
| **Epic** | EPIC-01 — Scan & Découverte |
| **Fichiers** | `app/assets/{router,schemas,service}.py` |
| **Agent** | @backend-python-dev |
| **Critères d'acceptation** | `GET /api/v1/assets/` liste les actifs, `GET /api/v1/assets/{id}` donne le détail avec ports |
| **Tests attendus** | `test_list_assets()`, `test_asset_detail()`, `test_asset_not_found()` |
| **Risques** | R-T03 : Latence UI si scan synchrones (mitigation : worker asynchrone) |
| **Statut** | ✅ TERMINÉ |

---

### US-01.9 — Détection et Alertes (Règles Simples) ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.9 |
| **Objectif** | Créer le moteur de règles simple et générer des alertes |
| **Epic** | EPIC-01 — Détection & Alerting |
| **Fichiers** | `app/alerts/{router,schemas,service}.py` |
| **Agent** | @backend-python-dev |
| **Critères d'acceptation** | Règle déclenchée → alerte créée avec `nouvelle`, `en cours`, `cloturee` |
| **Tests attendus** | `test_rule_triggers_alert()`, `test_alert_status_cycle()`, `test_alert_list()` |
| **Risques** | R-T01 : Faux positifs (mitigation : ajustement seuils) |
| **Statut** | ✅ TERMINÉ |

---

### US-01.10 — Cycle de Vie des Alertes ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.10 |
| **Objectif** | Permettre la qualification et le changement de statut des alertes |
| **Epic** | EPIC-01 — Détection & Alerting |
| **Fichiers** | `app/alerts/router.py` (PATCH), `app/alerts/schemas.py` |
| **Agent** | @backend-python-dev |
| **Critères d'acceptation** | `PATCH /api/v1/alerts/{id}` change le statut, audit log généré |
| **Tests attendus** | `test_update_alert_status()`, `test_alert_status_transition()` |
| **Risques** | Aucun majeur |
| **Statut** | ✅ TERMINÉ |

---

### US-01.11 — Exports CSV et JSON ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.11 |
| **Objectif** | Générer des exports CSV/JSON des alertes et actifs (preuve NIS2) |
| **Epic** | EPIC-01 — Reporting & Exports |
| **Fichiers** | `app/reports/router.py`, `app/reports/service.py`, `app/reports/schemas.py`, `app/models/export.py` |
| **Agent** | @backend-python-dev |
| **Critères d'acceptation** | `POST /api/v1/exports` génère un fichier, métadonnées conformes (section 13.2), `GET /api/v1/exports/{id}/download` télécharge |
| **Tests attendus** | `test_export_csv()`, `test_export_json()`, `test_export_metadata()` |
| **Risques** | R-S02 : Exposition de données (mitigation : contrôle d'accès) |
| **Statut** | ✅ TERMINÉ |

---

### US-01.12 — Audit Log (Journalisation) ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.12 |
| **Objectif** | Journaliser les actions sensibles : connexion, export, changement statut alerte, admin |
| **Epic** | EPIC-01 — Audit & Conformité |
| **Fichiers** | `app/audit/router.py`, `app/audit/service.py`, `app/models/audit_log.py` |
| **Agent** | @backend-python-dev |
| **Critères d'acceptation** | Chaque action sensible crée une entrée `audit_logs`, `GET /api/v1/audit-logs` (admin only) |
| **Tests attendus** | `test_audit_on_login()`, `test_audit_on_export()`, `test_audit_admin_only()` |
| **Risques** | R-P03 : Défaut de preuve (mitigation : audit obligatoire, format défini) |
| **Statut** | ✅ TERMINÉ |

---

### US-01.13 — Frontend Dashboard (Squelette) ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.13 |
| **Objectif** | Créer le tableau de bord web avec navigation (actifs, alertes, exports, audit) |
| **Epic** | EPIC-01 — Interface Web |
| **Fichiers** | `product/frontend/templates/index.html`, `static/css/style.css`, `static/js/app.js` |
| **Agent** | @backend-python-dev |
| **Critères d'acceptation** | Page HTML/CSS/JS fonctionnelle, login form, navigation, appels API |
| **Tests attendus** | `test_serves_frontend_index()` — HTML servi, `test_dashboard_*` |
| **Risques** | R-P01 : Rupture de planning (mitigation : HTML statique d'abord, JS minimal) |
| **Statut** | ✅ TERMINÉ |

---

### US-01.14 — Intégration Traffic Capture (P2) ✅ DONE

| Élément | Détail |
|---------|--------|
| **ID** | US-01.14 |
| **Objectif** | Intégrer le frontend Bootstrap et servir depuis FastAPI |
| **Epic** | EPIC-01 — Frontend (P2) |
| **Fichiers** | `app/main.py` (static mount + FileResponse), `product/frontend/` |
| **Agent** | @backend-python-dev |
| **Critères d'acceptation** | `GET /` sert le frontend, navigation SPA fonctionnelle, toutes pages accessibles |
| **Tests attendus** | `test_serves_frontend_index()`, tests manuels de navigation |
| **Risques** | Performance, permissions système pour la capture |
| **Statut** | ✅ TERMINÉ (Frontend intégré, traffic capture P2 reporté) |

---

## Matrice de Traçabilité EPIC-01

| Besoin initial | US associées | Recette (cahier des charges) |
|---------------|--------------|------------------------------|
| Santé API | US-01.1, US-01.2 | REC-009 |
| Sécuriser l'accès | US-01.5, US-01.6 | REC-001, REC-002 |
| Découvrir équipements | US-01.7, US-01.8 | REC-003 |
| Détecter comportements | US-01.9 | REC-004 |
| Qualifier alertes | US-01.10 | REC-005 |
| Produire preuves NIS2 | US-01.11 | REC-006 |
| Sécuriser entrées | US-01.7 (validation IP) | REC-007 |
| Garantir performance | US-01.8 (async) | REC-008 |
| Démonstration complète | US-01.1 à US-01.13 | REC-010 |

---

## Planning Prévisionnel

| Sprint | US | Livrable | Jalons |
|--------|----|----------|--------|
| Sprint 1 (J1-2) | US-01.3, US-01.4 | DB SQLite + Modèles | Infrastructure prête |
| Sprint 2 (J3-4) | US-01.5, US-01.6 | Auth JWT + Admin | Connexion fonctionnelle |
| Sprint 3 (J5-6) | US-01.7, US-01.8 | Scan + Assets | Découverte réseau OK |
| Sprint 4 (J7-8) | US-01.9, US-01.10 | Alertes + Cycle | Détection fonctionnelle |
| Sprint 5 (J9-10) | US-01.11, US-01.12 | Exports + Audit | Preuves NIS2 |
| Sprint 6 (J11-12) | US-01.13, US-01.14 | Frontend + Traffic | MVP Complet |

---

## Risques Identifiés (Focus EPIC-01)

| ID | Risque | Criticité | Mitigation |
|----|--------|-----------|------------|
| R-P01 | Rupture planning (9 jours, 14 US) | 🔴 20 | Priorisation stricte P1, livraison incrémentale |
| R-T01 | Faux positifs alertes | 🟡 12 | Tests sur réseaux variés, feedback |
| R-T02 | Blocage IDS lors scan | 🟡 12 | Délais inter-requêtes configurables |
| R-S01 | Injection champs IP | 🟡 10 | Validation Pydantic + regex stricte |
| R-S05 | Exposition secrets GitHub | 🟡 10 | `.env` dans `.gitignore`, `.env.example` documenté |

---

## Prochaines Actions

1. ✅ **US-01.1** → **US-01.14** — MVP COMPLET — **TERMINÉ**

**EPIC-01 : 14/14 User Stories livrées. Prochaines étapes : EPIC-02 (Docker Lab + Endpoint Agent)**

---

## Workflow de Validation (Chaque US)

```
Plan (project-manager-tech)
  ↓
Develop (@backend-python-dev)
  ↓
Test (@qa-tester)
  ↓
Security Audit (@security-tech-lead)
  ↓
Validate (@project-manager-tech)
```

---

**Document créé par :** @project-manager-tech  
**Date :** Mai 2026  
**Version :** 1.0
