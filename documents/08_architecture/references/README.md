# Références Architecture — BigBrowser

> Fichier d'index des documents de référence architecturale
> Projet : BigBrowser — Outil de Supervision et d'Analyse Réseau
> Version : 1.0 — Mai 2026

---

## Présentation

Ce dossier contient le document consolidé de référence détaillant l'architecture technique de BigBrowser. Il constitue le socle de conception pour l'équipe de développement et les contributeurs open-source.

---

## Documents

| Fichier | Contenu |
|---------|---------|
| [`sources_reference.md`](sources_reference.md) | Document consolidé : stack technique (13 composants), modules et flux (8 modules, 16 endpoints, 7 entités, topologie 3 zones), moteur de détection (7 règles, pipeline 5 étapes), sources documentaires avec liens officiels |

---

## Contenu du fichier consolidé

Le fichier unique `sources_reference.md` regroupe l'intégralité des références architecturales en quatre sections :

1. **Stack technique** — 13 composants avec versions cibles, justifications détaillées, alternatives écartées et prérequis système
2. **Modules et flux** — 8 modules backend, 16 endpoints API, 7 entités de données, 6 flux principaux, topologie 3 zones Docker
3. **Moteur de détection** — Pipeline 5 étapes, 7 types de règles (JSON), stockage JSONB, cycle de vie des alertes, orchestration Celery
4. **Sources** — Liens officiels de toutes les technologies, documents internes, bonnes pratiques, registre de traçabilité exigences→décisions

---

## Documents complémentaires

| Document | Emplacement |
|----------|-------------|
| Architecture technique complète | [`/documents/08_architecture/architecture_technique_bigbrowser.md`](../architecture_technique_bigbrowser.md) |
| Rapport d'architecture principal | [`/documents/08_architecture/rendu_principal.md`](../rendu_principal.md) |
| Schéma d'architecture (PNG) | [`/documents/08_architecture/assets/schema_d'architecture.png`](../assets/schema_d'architecture.png) |
| Cahier des charges | [`/documents/06_cahier_des_charges/rendu_principal.md`](../../06_cahier_des_charges/rendu_principal.md) |

---

## Consolidation

Les anciens fichiers numérotés (`01_stack_technique.md`, `02_modules_flux.md`, `03_moteur_detection.md`, `04_sources_reference.md`) ont été consolidés dans un document unique `sources_reference.md` pour simplifier la navigation et la maintenance.

---

*Document d'index — BigBrowser — Mai 2026*
