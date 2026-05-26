# Références du Cahier des Charges — BigBrowser

Ce dossier contient le document de référence consolidé associé au cahier des charges fonctionnel et technique du projet BigBrowser (v1.0).

## Document unique

| Fichier | Contenu |
|---|---|
| [`sources_reference.md`](sources_reference.md) | Document consolidé couvrant l'intégralité des références (exigences, recettes, sécurité, sources). |

## Périmètre couvert

Le document `sources_reference.md` couvre l'intégralité du périmètre défini dans le cahier des charges :

| Domaine | Couverture |
|---|---|
| Règles métier | 8 règles (RM-001 à RM-008) |
| Exigences fonctionnelles | 16 exigences (F-AUTH-001 à F-AUD-004) |
| Exigences non fonctionnelles | 14 exigences (NF-QUAL-001 à NF-TEST-001) |
| Exigences de sécurité | 8 exigences (SEC-001 à SEC-008) |
| Priorisation | MoSCoW (P1, P2, P3) |
| Scénarios de recette | 10 scénarios (REC-001 à REC-010) |
| Matrice de traçabilité | Besoin → Exigence → Recette → Preuve |
| Permissions | Matrice admin / analyst / non authentifié |
| Flux de données | 6 flux (FLUX-001 à FLUX-006) |
| Contrat API | 13 endpoints |
| Entités de données | 7 entités (users, assets, ports, alerts, audit_logs, exports, events) |
| Référentiels normatifs | OWASP ASVS, NIS2 (2022/2555), RGPD, France 2030 |

## Références croisées

- Cahier des charges principal : [`../rendu_principal.md`](../rendu_principal.md)
- Architecture définitive : [`../../08_architecture/rendu_principal.md`](../../08_architecture/rendu_principal.md)
- Feuille de cadrage : [`../../01_documents_pedagogiques/rendu_principal.md`](../../01_documents_pedagogiques/rendu_principal.md)
- Registre des références transverses : [`../../90_references_transverses/README.md`](../../90_references_transverses/README.md)
