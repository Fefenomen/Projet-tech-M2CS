# Références — Gestion de Projet BigBrowser

**Dernière mise à jour :** Mai 2026  
**Responsable :** @project-manager-tech  
**Statut global :** ✅ 85 tests, 100% passing, 21 endpoints API, 26 US totales

---

## Présentation

Ce dossier regroupe les documents de référence de la gestion de projet BigBrowser. L'ensemble du projet a été mené en méthodologie Agile (Scrum adapté) sur **6 sprints de 2 jours**, avec un total de **26 User Stories** réparties sur deux EPIC.

Toutes les informations sont consolidées dans un unique fichier :

| Document | Description |
|---|---|
| `sources_reference.md` | Référence unique consolidée — EPIC-01 (14 US, 6 sprints), EPIC-02 (12 US, lab Docker), résultats S1→S6 (85 tests, 21 endpoints, 26 US), sources externes et registre transverse. |

---

## Métriques Clés du Projet

| Métrique | Valeur |
|---|---|
| EPIC planifiés | 2 (EPIC-01 MVP, EPIC-02 Docker Lab) |
| User Stories totales | 26 (14 EPIC-01 + 12 EPIC-02) |
| Sprints exécutés | 6 |
| Tests automatisés | 85 (100% passing) |
| Endpoints API | 21 |
| Commits | 15+ |
| Zones Docker | 3 (Attaquant, Endpoints, SOC) |
| Réseau de démonstration | BBrowser_net — 172.20.0.0/24 |

---

## Workflow de Gestion de Projet

```text
Planification (project-manager-tech)
    ↓
Développement (backend-python-dev)
    ↓
Tests (qa-tester)
    ↓
Audit Sécurité (security-tech-lead)
    ↓
DevOps / Docker (devops-engineer)
    ↓
Validation (project-manager-tech)
```

Chaque User Story suit ce cycle avant d'être marquée terminée.

---

## Structure du Dossier

```
references/
├── README.md                    ← Ce fichier (index)
└── sources_reference.md         ← Référence unique consolidée (EPIC-01, EPIC-02, résultats, sources)
```
