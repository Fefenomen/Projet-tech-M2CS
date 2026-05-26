# Sources de Référence — MVP BigBrowser

Document consolidé des résultats métriques, statut des risques et sources mobilisées pour le rapport de complétion MVP BigBrowser (EPIC-01 et EPIC-02).

---

## Section 1 — Résultats et métriques

| Métrique | Valeur |
|---|---|
| User Stories EPIC-01 livrées | 14/14 (100 %) |
| User Stories EPIC-02 livrées | 12/12 |
| Total User Stories livrées | 26 |
| Tests unitaires et d'intégration | 85 |
| Tests passants | 85 (100 %) |
| Endpoints API | 21 |
| Exigences P1 couvertes | 21/21 (100 %) |
| Scénarios de recette (REC-001 à REC-010) | 10/10 PASS |
| Modules de test | 9 |
| Sprints réalisés | 6 (S1 à S6) |

### Couverture des exigences P1 (21/21)

| ID | Exigence | Statut | Recette |
|---|---|---|---|
| F-AUTH-001 | Authentification sécurisée | OK | REC-001 |
| F-AUTH-002 | Distinction rôles admin/analyst | OK | REC-002 |
| F-AUTH-003 | Restriction actions sensibles par rôle | OK | REC-002 |
| F-DISC-001 | Scan d'une plage IP | OK | REC-003 |
| F-DISC-002 | Identification des équipements | OK | REC-003 |
| F-DISC-003 | Détection des ports ouverts | OK | REC-003 |
| F-ASSET-001 | Inventaire d'actifs consultable | OK | REC-003 |
| F-ALERT-001 | Production d'alertes par règles | OK | REC-004 |
| F-ALERT-002 | Vue liste des alertes | OK | REC-005 |
| F-ALERT-003 | Vue détail d'une alerte | OK | REC-005 |
| F-ALERT-004 | Cycle de vie des alertes | OK | REC-005 |
| F-UI-001 | Tableau de bord de synthèse | OK | REC-001 |
| F-UI-002 | Consultation des actifs | OK | REC-003 |
| F-UI-003 | Consultation des alertes | OK | REC-004 |
| F-UI-004 | Consultation du trafic capturé | OK | REC-003 |
| F-EXP-001 | Export CSV | OK | REC-006 |
| F-EXP-002 | Export JSON | OK | REC-006 |
| F-EXP-003 | Preuve opérationnelle NIS2 | OK | REC-006 |
| F-EXP-004 | Accès restreint aux exports | OK | REC-006 |
| F-AUD-001 | Journalisation des authentifications | OK | REC-001 |
| F-AUD-002 | Journalisation des exports | OK | REC-006 |
| F-AUD-003 | Journalisation actions sensibles | OK | REC-005 |
| F-AUD-004 | Consultation journaux par admin | OK | REC-002 |

### Résultats des tests par module

| Module | Nombre de tests | Statut |
|---|---|---|
| `auth` | 12 | 12/12 PASS |
| `telemetry` | 10 | 10/10 PASS |
| `discovery` | 8 | 8/8 PASS |
| `assets` | 9 | 9/9 PASS |
| `alerts` | 15 | 15/15 PASS |
| `reports` | 10 | 10/10 PASS |
| `audit` | 8 | 8/8 PASS |
| `traffic` | 7 | 7/7 PASS |
| `main` | 6 | 6/6 PASS |
| **Total** | **85** | **85/85 PASS** |

### Endpoints API (21)

| Méthode | Endpoint | Usage | Accès |
|---|---|---|---|
| `POST` | `/api/v1/auth/login` | Authentification | Public |
| `GET` | `/api/v1/auth/me` | Infos utilisateur | Authentifié |
| `POST` | `/api/v1/auth/users` | Créer utilisateur | Admin |
| `POST` | `/api/v1/telemetry/heartbeat` | Heartbeat agent | Authentifié |
| `POST` | `/api/v1/telemetry/events` | Events agent | Authentifié |
| `GET` | `/api/v1/telemetry/events` | Lister events | Authentifié |
| `POST` | `/api/v1/scan/` | Lancer scan réseau | Admin |
| `GET` | `/api/v1/scan/status/{task_id}` | Statut scan | Admin |
| `GET` | `/api/v1/assets/` | Liste actifs | Authentifié |
| `GET` | `/api/v1/assets/{id}` | Détail actif | Authentifié |
| `GET` | `/api/v1/alerts/` | Liste alertes | Authentifié |
| `GET` | `/api/v1/alerts/{id}` | Détail alerte | Authentifié |
| `POST` | `/api/v1/alerts/` | Créer alerte | Authentifié |
| `PATCH` | `/api/v1/alerts/{id}` | Changer statut | Authentifié |
| `POST` | `/api/v1/alerts/{id}/qualify` | Qualifier alerte | Authentifié |
| `GET` | `/api/v1/dashboard/` | Métriques | Authentifié |
| `POST` | `/api/v1/exports/` | Générer export | Authentifié |
| `GET` | `/api/v1/exports/{id}/download` | Télécharger export | Authentifié |
| `GET` | `/api/v1/audit-logs/` | Journaux d'audit | Admin |
| `GET` | `/api/v1/audit-logs/{id}` | Détail journal | Admin |
| `GET` | `/health` | Santé applicative | Public |

---

## Section 2 — Statut des risques et recommandations EPIC-03

### État des risques en fin de MVP

| ID | Risque | Criticité | Statut MVP |
|---|---|---|---|
| R-P01 | Rupture de planning | 10 | Mitigé |
| R-P02 | Conflits Git | 6 | Mitigé |
| R-P03 | Défaut de preuve en démonstration | 5 | Fermé |
| R-T01 | Faux positifs dégradant la crédibilité | 9 | Actif |
| R-T02 | Blocage par IDS tiers lors du scan | 8 | Actif |
| R-T03 | Latence UI pendant scan | 3 | Fermé |
| R-S01 | Injection de commandes via champs IP | 5 | Fermé |
| R-S02 | Exposition de données lors des exports | 4 | Fermé |
| R-M01 | Adoption insuffisante open-source | 16 | Actif |
| R-M02 | Concurrence des outils établis | 9 | Actif |
| R-M03 | Difficulté à recruter des profils cyber | 12 | Actif |

### Recommandations pour EPIC-03

**Priorité 1 — Fondations techniques**
- Migration PostgreSQL
- Mise en place Celery + Redis
- Capture trafic réseau complète

**Priorité 2 — Améliorations fonctionnelles**
- Scans furtifs (SYN) avec délais configurables
- Interface web de configuration des règles d'alerte
- Dashboard conformité NIS2 dédié
- Pagination et filtres avancés

**Priorité 3 — Extensions**
- Modules IA/ML de détection comportementale
- Architecture multi-tenant pour MSP
- Offre SaaS hébergée
- API REST documentée complète (OpenAPI)
- Internationalisation (Belgique, Luxembourg)

---

## Section 3 — Sources

### Outils et technologies

- [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- [pytest](https://docs.pytest.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Bootstrap 5](https://getbootstrap.com/)
- [JWT.io](https://jwt.io/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [GitHub](https://github.com/)
- [OpenCode](https://github.com/opencode-ai)

### Plans d'EPIC

| Document | Emplacement |
|---|---|
| `EPIC-01_plan.md` | `product/backend/plans/EPIC-01_plan.md` |
| `EPIC-02_plan.md` | `product/backend/plans/EPIC-02_plan.md` |

### Rapports de sprint

| Document | Emplacement |
|---|---|
| Rapport Sprint S1 | `product/backend/sprints/S1/` |
| Rapport Sprint S2 | `product/backend/sprints/S2/` |
| Rapport Sprint S3 | `product/backend/sprints/S3/` |
| Rapport Sprint S4 | `product/backend/sprints/S4/` |
| Rapport Sprint S5 | `product/backend/sprints/S5/` |
| Rapport Sprint S6 | `product/backend/sprints/S6/` |

### Documents projet

| Document | Emplacement |
|---|---|
| Cahier des charges | `documents/06_cahier_des_charges/rendu_principal.md` |
| Architecture définitive | `documents/08_architecture/rendu_principal.md` |
| Business model | `documents/03_business_model/rendu_principal.md` |
| Business plan | `documents/04_business_plan/rendu_principal.md` |
| Étude de marché | `documents/02_etude_de_marche/rendu_principal.md` |

### Code source

| Composant | Emplacement |
|---|---|
| Backend | `product/backend/` |
| Frontend | `product/backend/app/static/` |
| Agent | `product/agent/` |
| Attaquant | `product/attacker/` |
| Docker | `product/docker/` |

### Modules de test

| Module | Emplacement | Nombre de tests |
|---|---|---|
| Auth | `product/backend/tests/auth/` | 12 |
| Telemetry | `product/backend/tests/telemetry/` | 10 |
| Discovery | `product/backend/tests/discovery/` | 8 |
| Assets | `product/backend/tests/assets/` | 9 |
| Alerts | `product/backend/tests/alerts/` | 15 |
| Reports | `product/backend/tests/reports/` | 10 |
| Audit | `product/backend/tests/audit/` | 8 |
| Traffic | `product/backend/tests/traffic/` | 7 |
| Main | `product/backend/tests/main/` | 6 |

### Conventions de nommage

| Élément | Format | Exemple |
|---|---|---|
| EPIC | `EPIC-NN` | `EPIC-01` |
| User Story | `US-NN.M` | `US-01.1` |
| Sprint | `SN` | `S1` |
| Exigence fonctionnelle | `F-DOMAINE-NNN` | `F-AUTH-001` |
| Exigence non fonctionnelle | `NF-CATEGORIE-NNN` | `NF-PERF-001` |
| Sécurité | `SEC-NNN` | `SEC-001` |
| Recette | `REC-NNN` | `REC-001` |
| Risque | `R-DOMAINE-NN` | `R-P01` |

---

*Document consolidé le 26/05/2026 — Version 1.0 — Équipe BigBrowser*
