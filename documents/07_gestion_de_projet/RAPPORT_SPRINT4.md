# Rapport Sprint 4 — BigBrowser

> **Date :** 7 Mai 2026
> **Sprint :** Sprint 4 (EPIC-01 — Détection & Alerting)
> **Statut :** ✅ TERMINÉ

---

## ✅ Réalisations Sprint 4

| Jalon | Description | Statut | Commit |
|---|---|---|---|
| J1-J5 | Sprints précédents | ✅ | - |
| **J6** | **US-01.9 Détection & Alertes** | **✅** | **Sprint 4** |
| **J7** | **US-01.10 Cycle de vie alertes** | **✅** | **Sprint 4** |

---

## 📊 État d'Avancement Global

| Métrique | Valeur |
|---|---|
| US planifiées (EPIC-01) | 14 (US-01.1 à US-01.14) |
| US terminées | 10 (US-01.1 à US-01.10) |
| US en cours | 0 |
| US restantes | 4 (US-01.11 à US-01.14) |
| **Progression** | **71%** |
| Tests automatisés | 54 (100% passing) |
| Modules backend | 8 (core, auth, health, telemetry, discovery, assets, alerts, models) |

---

## 🔧 Changements Sprint 4

### US-01.9 — Détection et Alertes ✅

- **Module `app/alerts/`** créé (router, schemas, service)
- **POST /api/v1/alerts/** — création d'alertes avec validation
- **GET /api/v1/alerts/** — liste avec stats par sévérité et statut
- **GET /api/v1/alerts/{id}** — détail d'une alerte
- **Validation sévérité** : `low`, `medium`, `high`, `critical`
- **Lien asset** : alerte liée à un actif existant (vérification FK)
- **Audit log** : chaque création d'alerte journalisée

### US-01.10 — Cycle de Vie des Alertes ✅

- **PATCH /api/v1/alerts/{id}** — changement de statut avec transitions validées
- **Machine à états** :
  - `nouvelle` → `en cours` ou `cloturee`
  - `en cours` → `cloturee`
  - `cloturee` → aucune (finale)
- **Validation statut** : rejet des transitions invalides (400)
- **Audit log** : chaque changement de statut journalisé
- **Statistiques** : compteur par sévérité et statut dans la liste

---

## 🧪 Nouveaux Tests (19 ajoutés → 54 total)

| Catégorie | Tests | Résultat |
|---|---|---|
| Liste alertes | 3 | ✅ |
| Détail alerte | 2 | ✅ |
| Création alerte | 5 | ✅ |
| Cycle de vie (PATCH) | 7 | ✅ |
| Cycle complet | 1 | ✅ |
| Sécurité | 1 | ✅ |

**Couverture sécurité :**
- Sévérité invalide → 422 ✅
- Asset inexistant → 404 ✅
- Transition interdite (cloturee → nouvelle) → 400 ✅
- Sans token → 401 ✅
- Statut invalide → 422 ✅

---

## 📡 API Mise à Jour

| Méthode | Endpoint | Usage | Accès |
|---|---|---|---|
| `GET` | `/api/v1/alerts/` | Liste alertes + stats | Authentifié |
| `GET` | `/api/v1/alerts/{id}` | Détail alerte | Authentifié |
| `POST` | `/api/v1/alerts/` | Créer une alerte | Authentifié |
| `PATCH` | `/api/v1/alerts/{id}` | Changer statut | Authentifié |

---

## 🎯 Prochain Sprint — Sprint 5 (US-01.11 + US-01.12)

| US | Description | Fichiers attendus |
|---|---|---|
| US-01.11 | Exports CSV/JSON (preuve NIS2) | `app/reports/{router,service}.py` |
| US-01.12 | Audit logs complets (GET /audit-logs) | `app/audit/{router,service}.py` |

---

*Rapport généré le 7 mai 2026*
