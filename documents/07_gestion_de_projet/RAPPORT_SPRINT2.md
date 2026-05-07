# Rapport Sprint 2 — BigBrowser

> **Date :** 7 Mai 2026
> **Sprint :** Sprint 2 (EPIC-01 — Auth & RBAC)
> **Statut :** ✅ TERMINÉ

---

## ✅ Réalisations Sprint 2

| Jalon | Description | Statut | Commit |
|---|---|---|---|
| J1 | Business Model + Business Plan générés | ✅ | 5ec2bd5 |
| J2 | Structure annexes/references conforme | ✅ | 49201eb |
| J3 | Instructions/readme.md mis à jour (BigBrowser) | ✅ | 1257c2f |
| J4 | OpenCode configuré (5 agents + skills) | ✅ | 9278699 |
| J5 | EPIC-01 planifié (14 US) | ✅ | 7d043ec |
| J6 | US-01.3 Database Setup | ✅ | ba30d0e |
| J7 | US-01.4 Data Models | ✅ | f45bf48 |
| **J8** | **US-01.5 Auth JWT complète (DB)** | **✅** | **b029ad0** |
| **J9** | **US-01.6 Init admin + POST /users** | **✅** | **b029ad0** |

---

## 📊 État d'Avancement Global

| Métrique | Valeur |
|---|---|
| US planifiées (EPIC-01) | 14 (US-01.1 à US-01.14) |
| US terminées | 6 (US-01.1 à US-01.6) |
| US en cours | 0 |
| US restantes | 8 (US-01.7 à US-01.14) |
| **Progression** | **43%** |
| Commits total Sprint 1+2 | 9 |
| Tests automatisés | 22 (100% passing) |
| Fichiers Python | 20+ |

---

## 🔧 Changements Sprint 2

### US-01.5 — Authentification JWT Complète ✅

- **Avant :** Fake users en mémoire (`fake_users_db` dict)
- **Après :** Utilisateurs persistés en SQLite via SQLAlchemy
- **Endpoints ajoutés :**
  - `GET /api/v1/auth/me` — infos utilisateur courant
  - `POST /api/v1/auth/login` — migré vers DB
- **Tests :** login valide, login invalide, analyst login, GET /me, protected route

### US-01.6 — Initialisation Admin et Utilisateurs ✅

- **Seed automatique :** `admin/admin123` + `analyst/analyst123` créés au premier démarrage
- **Endpoint ajouté :** `POST /api/v1/auth/users` (admin only)
- **RBAC :** Factory `require_role("admin")` bloque les non-admin
- **Tests :** create user admin OK, create user analyst → 403, duplicate username → 400

---

## 🧪 Tests (22/22 ✅)

| Catégorie | Tests | Résultat |
|---|---|---|
| Health | 2 | ✅ |
| Database/Models | 4 | ✅ |
| Auth login | 4 | ✅ |
| Auth /me | 2 | ✅ |
| Auth users (admin only) | 4 | ✅ |
| Protected routes | 2 | ✅ |
| Telemetry heartbeat | 4 | ✅ |

---

## 🎯 Prochain Sprint — Sprint 3 (US-01.7 + US-01.8)

| US | Description | Fichiers attendus |
|---|---|---|
| US-01.7 | Scan réseau (plage IP, validation) | `app/discovery/router.py`, `app/discovery/service.py` |
| US-01.8 | Inventaire actifs + ports | `app/assets/router.py`, CRUD assets |

---

*Rapport généré le 7 mai 2026*
