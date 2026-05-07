# Rapport Sprint 5 — EPIC-01

## Objectif
Implémenter les exports CSV/JSON (US-01.11) et l'endpoint audit logs admin (US-01.12).

## Réalisations

### US-01.11 — Exports CSV/JSON
- **Module** : `app/reports/`
- **Fichiers créés** : `router.py`, `service.py`, `schemas.py`
- **Endpoints** :
  - `POST /api/v1/exports/` — Génération d'export (CSV/JSON) pour scope `alerts`, `assets`, `audit_logs`
  - `GET /api/v1/exports/{id}/download` — Téléchargement du fichier export
- **Format CSV** : colonnes standards selon cahier des charges (id, title, severity, status, source_ip, etc.)
- **Format JSON** : payload avec `export_id`, `generated_at`, `format`, `scope`, `items[]`
- **Sécurité** : authentification requise, validation Pydantic (format/scope), trace dans `audit_logs`
- **Stockage** : fichiers écrits dans `/tmp/bigbrowser_exports/`

### US-01.12 — Endpoint Audit Logs
- **Module** : `app/audit/`
- **Fichiers créés** : `router.py`, `service.py`, `schemas.py`
- **Endpoints** :
  - `GET /api/v1/audit-logs/` — Liste de tous les journaux d'audit (admin only)
  - `GET /api/v1/audit-logs/{id}` — Détail d'un journal d'audit (admin only)
- **Sécurité** : `require_role("admin")` — analyste → 403
- **Audit auto** : chaque export génère une entrée `export_data` dans les logs

### Intégration
- `main.py` mis à jour avec les routers `reports` et `audit`

## Tests
- **14 nouveaux tests** dans `tests/test_reports.py`
- Couverture : exports CSV/JSON, scopes multiples, validation, téléchargement, audit logs, permissions
- **68/68 tests passants** (100%)

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
| US-01.13 | Tableau de bord web | 🔜 Sprint 6 |
| US-01.14 | Frontend Bootstrap | 🔜 Sprint 6 |

## Prochain Sprint (6/7)
- US-01.13 : Tableau de bord API (métriques agrégées)
- US-01.14 : Frontend Bootstrap intégré (Jinja2 templates)
- Finalisation EPIC-01
