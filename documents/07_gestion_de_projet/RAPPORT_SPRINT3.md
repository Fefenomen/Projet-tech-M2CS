# Rapport Sprint 3 — BigBrowser

> **Date :** 7 Mai 2026
> **Sprint :** Sprint 3 (EPIC-01 — Scan & Découverte)
> **Statut :** ✅ TERMINÉ

---

## ✅ Réalisations Sprint 3

| Jalon | Description | Statut | Commit |
|---|---|---|---|
| J1-J5 | Sprints précédents | ✅ | - |
| **J6** | **US-01.7 Scan réseau** | **✅** | **128a5a6** |
| **J7** | **US-01.8 Inventaire actifs** | **✅** | **128a5a6** |

---

## 📊 État d'Avancement Global

| Métrique | Valeur |
|---|---|
| US planifiées (EPIC-01) | 14 (US-01.1 à US-01.14) |
| US terminées | 8 (US-01.1 à US-01.8) |
| US en cours | 0 |
| US restantes | 6 (US-01.9 à US-01.14) |
| **Progression** | **57%** |
| Tests automatisés | 35 (100% passing) |
| Modules backend | 7 (core, auth, health, telemetry, discovery, assets, models) |

---

## 🔧 Changements Sprint 3

### US-01.7 — Scan Réseau ✅

- **Module `app/discovery/`** créé avec router, schemas, service
- **Validation IP stricte** via regex Pydantic (anti-injection commande)
- **Scan TCP socket** — scan de ports sans dépendance nmap
- **Limite 256 IPs** max par scan (prévention abus)
- **Délai configurable** entre requêtes (détection furtive)
- **Détection services** — mapping ports → noms de services connus
- **Persistance automatique** — assets et ports créés en DB après scan
- **Endpoint :** `POST /api/v1/scan/` (admin only)

### US-01.8 — Inventaire des Actifs ✅

- **Module `app/assets/`** créé avec router, schemas, service
- **Liste des actifs :** `GET /api/v1/assets/` avec compteur total
- **Détail d'un actif :** `GET /api/v1/assets/{id}` avec ports associés
- **Port model enrichi :** ajout du champ `service_name`
- **Tri par `last_seen_at`** décroissant (actifs récents en premier)

---

## 🧪 Nouveaux Tests (13 ajoutés → 35 total)

| Catégorie | Tests | Résultat |
|---|---|---|
| Validation IPv4 | 2 | ✅ |
| Génération range IP | 1 | ✅ |
| Scan endpoint | 6 | ✅ |
| Assets endpoints | 4 | ✅ |

**Couverture sécurité :**
- Injection IP (`127.0.0.1; rm -rf /`) → rejetée 422 ✅
- IP invalide (`invalid`) → rejetée 422 ✅
- Analyst tente scan → 403 Forbidden ✅
- Range trop large (512 IPs) → 400 Bad Request ✅
- Scan sans token → 401 Unauthorized ✅

---

## 📡 API Mise à Jour

| Méthode | Endpoint | Usage | Accès |
|---|---|---|---|
| `POST` | `/api/v1/scan/` | Lancer un scan réseau | `admin` uniquement |
| `GET` | `/api/v1/assets/` | Liste des actifs | Authentifié |
| `GET` | `/api/v1/assets/{id}` | Détail actif + ports | Authentifié |

---

## 🎯 Prochain Sprint — Sprint 4 (US-01.9 + US-01.10)

| US | Description | Fichiers attendus |
|---|---|---|
| US-01.9 | Moteur de règles + création alertes | `app/alerts/{router,service}.py` |
| US-01.10 | Cycle de vie alertes (PATCH) | `app/alerts/router.py` (PATCH endpoint) |

---

*Rapport généré le 7 mai 2026*
