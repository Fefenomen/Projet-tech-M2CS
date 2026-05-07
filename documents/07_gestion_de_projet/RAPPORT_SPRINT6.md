# Rapport Sprint 6 — EPIC-01

## Objectif
Implémenter le tableau de bord API (US-01.13) et le frontend Bootstrap (US-01.14) pour finaliser le MVP démontrable.

## Réalisations

### US-01.13 — Dashboard API (Métriques Agrégées)
- **Module** : `app/dashboard/`
- **Fichiers créés** : `router.py`, `service.py`, `schemas.py`
- **Endpoints** :
  - `GET /api/v1/dashboard/` — Retourne les métriques complètes
- **Métriques fournies** :
  - Total alertes, répartition par statut et sévérité
  - Total actifs, répartition par statut
  - Total journaux d'audit
  - Total exports générés
  - 10 alertes récentes (triées par date)
- **Sécurité** : authentification requise (admin et analyst)

### US-01.14 — Frontend Bootstrap
- **Répertoire** : `product/frontend/`
- **Fichiers créés** :
  - `templates/index.html` — Page unique SPA avec login + dashboard
  - `static/css/style.css` — Thème sombre SOC personnalisé
  - `static/js/app.js` — Logique SPA complète
- **Pages implémentées** :
  - **Login** : formulaire d'authentification avec gestion de session (localStorage)
  - **Tableau de bord** : 4 cartes métriques + tableau des alertes récentes
  - **Actifs** : liste avec boutons de détail, scan réseau pour admin
  - **Alertes** : liste filtrable par statut, modal de détail, changement de statut
  - **Exports** : formulaire de génération (CSV/JSON), lien de téléchargement
  - **Audit** : tableau des journaux (admin uniquement)
- **Intégration** : `GET /` sert `index.html`, `/static/` sert les assets
- **Navigation** : SPA côté client avec fetch API vers `/api/v1/*`

## Tests
- **5 nouveaux tests** dans `tests/test_dashboard.py`
- **1 test existant adapté** (`test_root_endpoint` → vérifie HTML au lieu de JSON)
- **73/73 tests passants** (100%)

## Couverture fonctionnelle EPIC-01
| ID | User Story | Statut |
|---|---|---|
| US-01.1 | Authentification JWT DB | ✅ Done |
| US-01.2 | Gestion des rôles admin/analyst | ✅ Done |
| US-01.3 | Scan réseau borné | ✅ Done |
| US-01.4 | Détection de ports ouverts | ✅ Done |
| US-01.5 | Inventaire d'actifs | ✅ Done |
| US-01.6 | Détail des actifs avec ports | ✅ Done |
| US-01.7 | Génération d'alertes | ✅ Done |
| US-01.8 | Liste/détail alertes | ✅ Done |
| US-01.9 | Cycle de vie alertes | ✅ Done |
| US-01.10 | Audit logs automatiques | ✅ Done |
| US-01.11 | Exports CSV/JSON | ✅ Done |
| US-01.12 | Endpoint audit logs admin | ✅ Done |
| US-01.13 | Dashboard API | ✅ Done |
| US-01.14 | Frontend Bootstrap | ✅ Done |

## Résultat
**EPIC-01 TERMINÉ — 14/14 User Stories livrées, 73 tests passants.**

Le MVP BigBrowser est maintenant pleinement fonctionnel avec :
- Backend API complet (13 endpoints)
- Frontend web SPA Bootstrap responsive
- Chaîne complète : scan → détection → alertes → exports → audit
- Interface accessible sans expertise CLI (conforme NIS2)
