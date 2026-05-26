# Sources de Référence — BigBrowser

> Document consolidé des objectifs SMART, du périmètre/risques et des sources mobilisées pour la feuille de cadrage du projet BigBrowser.
>
> *Document de référence — Mai 2026*

---

## Section 1 — Objectifs SMART

### 1.1. Méthode SMART

Chaque objectif est défini selon les critères SMART :

| Critère | Définition |
|---|---|
| **S**pécifique | Objectif précis, sans ambiguïté |
| **M**esurable | Indicateur quantitatif associé |
| **A**tteignable | Réaliste au vu des ressources disponibles |
| **R**éaliste | Cohérent avec le contexte et les contraintes |
| **T**emporellement défini | Échéance clairement identifiée |

### 1.2. Les 6 objectifs SMART

#### O1 — Publier la v1.0 open-source sur GitHub

| Critère | Valeur |
|---|---|
| **Objectif** | Publier la version 1.0 de BigBrowser sur GitHub avec les 8 fonctionnalités clés du périmètre MVP |
| **Indicateur** | Release GitHub live, taguée, documentée et reproductible |
| **Cible** | Mois 6 (octobre 2026) |
| **Hypothèse** | Développement sur 6 mois avec 2-3 développeurs, stack Python/FastAPI maîtrisée |
| **Référence** | Cahier des charges §6.1, Architecture §18 |

#### O2 — Générer 500 déploiements de l'outil

| Critère | Valeur |
|---|---|
| **Objectif** | Atteindre 500 déploiements actifs (téléchargements Docker, clones Git, installations documentées) |
| **Indicateur** | Nombre de déploiements comptabilisés (GitHub Releases downloads + Docker pulls + déclarations) |
| **Cible** | 500 déploiements en année 1 |
| **Hypothèse** | Taux de conversion basé sur le benchmark d'outils open-source comparables (Wazuh, Security Onion) |
| **Référence** | Business model §6.2, Stratégie GTM Phase 1 |

#### O3 — Convertir 15 utilisateurs en clients de support payant

| Critère | Valeur |
|---|---|
| **Objectif** | Convertir 15 utilisateurs open-source en clients de support payant (offre Support Essentiel à 280 €/mois) |
| **Indicateur** | Nombre de contrats de support actifs signés |
| **Cible** | 15 clients support actifs en année 1 |
| **Hypothèse** | Taux de conversion 3-5 % (benchmark SaaS open-source). Hypothèse retenue : 3 % de 500 déploiements = 15 clients |
| **Référence** | Business model §6.2, Business plan §10 |

#### O4 — Réaliser 10 missions d'audit NIS2

| Critère | Valeur |
|---|---|
| **Objectif** | Réaliser 10 missions d'audit de conformité NIS2 auprès de PME et collectivités |
| **Indicateur** | Nombre de missions d'audit facturées et réalisées |
| **Cible** | 10 missions en année 1 |
| **Hypothèse** | Panier moyen audit : 3 000 €/mission. Conquête via les PME pilotes (5-10 déploiements gratuits Phase 1) |
| **Référence** | Business model §2.2, Business plan §7 |

#### O5 — Atteindre 84 000 € de chiffre d'affaires

| Critère | Valeur |
|---|---|
| **Objectif** | Atteindre un chiffre d'affaires consolidé de 84 000 € à l'issue de la première année |
| **Indicateur** | Chiffre d'affaires total facturé et encaissé |
| **Cible** | ~84 000 € en année 1 |
| **Hypothèse** | 15 clients support × 280 €/mois × 12 mois (~32 000 € proratisé) + 10 audits × 3 000 € (~30 000 €) + formations (~12 500 €) + 2 MSP × 400 €/mois × 12 mois (~9 600 €) |
| **Référence** | Business model §6.1, Business plan §10, Feuille de cadrage §8.2 |

#### O6 — Activer 2 partenariats MSP/SSII

| Critère | Valeur |
|---|---|
| **Objectif** | Signer 2 partenariats actifs avec des MSP ou SSII intégrant BigBrowser dans leur offre |
| **Indicateur** | Nombre de partenaires ayant signé un contrat et réalisé au moins une mission |
| **Cible** | 2 MSP actifs en année 1 |
| **Hypothèse** | Partenaires recrutés via salons (FIC, Les Assises), réseautage direct et PME pilotes. Panier moyen : 400 €/mois |
| **Référence** | Business model §9, Business plan §5 |

### 1.3. Synthèse des objectifs

| Objectif | Indicateur | Cible An 1 | Échéance | Poids CA |
|---|---|---|---|---|
| **O1** — GitHub v1.0 | Release live | Mois 6 | Oct. 2026 | Prérequis |
| **O2** — Déploiements | Compteur téléchargements | 500 | Mois 12 | Funnel |
| **O3** — Clients support | Contrats signés | 15 | Mois 12 | ~38 % |
| **O4** — Missions audit | Missions facturées | 10 | Mois 12 | ~36 % |
| **O5** — CA total | Euros encaissés | ~84 000 € | Mois 12 | 100 % |
| **O6** — Partenaires MSP | Contrats partenaires | 2 | Mois 12 | ~11 % |

### 1.4. Macro-planning 3 phases (36 mois)

#### Phase 1 — Lancement & Traction (Mois 1-6)

| Période | Jalons clés | Objectifs |
|---|---|---|
| M1-M2 | Cadrage finalisé, architecture validée, stack technique installée | O1 |
| M3-M4 | Développement du MVP (scans, détection, alertes, UI) | O1 |
| M5-M6 | Finalisation v1.0, documentation, publication GitHub, PME pilotes | O1, O2 |
| M6 | **Release GitHub v1.0** — 500 déploiements visés, 2 MSP partenaires | O1, O2, O6 |

#### Phase 2 — Monétisation (Mois 6-18)

| Période | Jalons clés | Objectifs |
|---|---|---|
| M6-M9 | Lancement offre de support, premières missions d'audit | O3, O4 |
| M9-M12 | Programme certification partenaires, formations inter-entreprises | O5, O6 |
| M12 | **15 clients support, 10 missions, 84 K€ CA** | O3, O4, O5 |
| M12-M18 | Extension réseau MSP, catalogue achats publics | O6 |

#### Phase 3 — Industrialisation (Mois 18-36)

| Période | Jalons clés | Objectifs |
|---|---|---|
| M18-M24 | Modules premium (IA/ML, NIS2 dashboard), 20+ MSP | O6 |
| M24-M30 | Exploration SaaS hébergé, dossier France 2030 | — |
| M30-M36 | Internationalisation BE/LU, 5 000 déploiements | O2 |
| M36 | **881 K€ CA An 3, 20+ MSP, 5 000 déploiements** | O5, O6, O2 |

---

## Section 2 — Périmètre et Risques

### 2.1. Périmètre MVP

#### Dans le périmètre (10 items)

| # | Fonctionnalité | Priorité | Objectif |
|---|---|---|---|
| 1 | Scan de plages IP et découverte d'équipements | P1 | O1, O2 |
| 2 | Détection de ports ouverts et services réseau | P1 | O1, O2 |
| 3 | Capture et analyse du trafic réseau | P1 | O1, O2 |
| 4 | Détection de comportements suspects (règles) | P1 | O1 |
| 5 | Système d'alertes configurables | P1 | O1 |
| 6 | Interface web unifiée (tableau de bord) | P1 | O1, O2 |
| 7 | Export JSON et CSV des rapports | P1 | O1, O4 |
| 8 | Déployable on-premise (sans cloud) | P1 | O2 |
| 9 | Services : support, audit NIS2, formation | P2 | O3, O4, O5 |
| 10 | Canal de distribution partenaires MSP/SSII | P2 | O6 |

#### Hors périmètre v1 (8 items)

| # | Fonctionnalité | Report | Justification |
|---|---|---|---|
| 1 | Modules IA/ML de détection comportementale | v2+ | Complexité technique, nécessite données d'apprentissage |
| 2 | Offre SaaS cloud hébergée | v2+ | Contrainte on-premise, coût d'infrastructure |
| 3 | Dashboard conformité NIS2 dédié | v2+ | Non bloquant pour la démonstration MVP |
| 4 | Intégration native SIEM (CEF/LEEF) | v2+ | Connaissance des formats propriétaires nécessaire |
| 5 | Certification SecNumCloud | v2+ | Processus long et coûteux |
| 6 | Internationalisation (Belgique, Luxembourg) | v2+ | Focus France en v1 |
| 7 | API REST documentée complète | v2+ | Documentation suffisante pour le MVP |
| 8 | Module scoring de risque IA | v2+ | Dépend du module IA/ML |

### 2.2. Analyse des 6 risques projet

#### R1 — Adoption insuffisante de la version open-source

| Propriété | Valeur |
|---|---|
| **Probabilité** | 4/5 (Élevée) |
| **Impact** | 4/5 (Élevé) |
| **Criticité** | **16/25 (Élevée)** |
| **Période** | M1-M12 |

**Mitigation** : Stratégie de contenu active, présence GitHub Trending, partenariat ANSSI, salons FIC/Assises, programme PME pilotes.

**Indicateur d'alerte** : Moins de 50 déploiements à M3 ou moins de 200 à M6.

#### R2 — Concurrence des outils établis (Wazuh, PRTG, Security Onion)

| Propriété | Valeur |
|---|---|
| **Probabilité** | 3/5 (Moyenne) |
| **Impact** | 3/5 (Moyen) |
| **Criticité** | **9/25 (Moyenne)** |
| **Période** | Continue |

**Mitigation** : Différenciation UX (8 fonctionnalités unifiées), positionnement « Splunk pour les PME », ciblage du gap concurrentiel identifié.

#### R3 — Retard de transposition NIS2 en France

| Propriété | Valeur |
|---|---|
| **Probabilité** | 3/5 (Moyenne) |
| **Impact** | 3/5 (Moyen) |
| **Criticité** | **9/25 (Moyenne)** |
| **Période** | 2026-2027 |

**Mitigation** : Réorientation discours commercial sur valeur opérationnelle, ciblage early adopters, marché formation comme relais.

#### R4 — Difficulté à recruter des profils cyber expérimentés

| Propriété | Valeur |
|---|---|
| **Probabilité** | 4/5 (Élevée) |
| **Impact** | 4/5 (Élevé) |
| **Criticité** | **16/25 (Élevée)** |
| **Période** | M1-M12 |

**Mitigation** : Partenariats écoles, valorisation open-source, prestation externalisée, programme de mentorat interne, flexibilité du travail.

#### R5 — Faux positifs dégradant la crédibilité du produit

| Propriété | Valeur |
|---|---|
| **Probabilité** | 3/5 (Moyenne) |
| **Impact** | 3/5 (Moyen) |
| **Criticité** | **9/25 (Moyenne)** |
| **Période** | M3-M12 |

**Mitigation** : QA important, bêta-test 5-10 PME pilotes, feedback intégré, configuration conservative par défaut.

**Indicateur d'alerte** : Taux de faux positifs > 30 % remonté par les pilotes.

#### R6 — Consolidation du marché (Cisco-Splunk) réduisant l'espace concurrentiel

| Propriété | Valeur |
|---|---|
| **Probabilité** | 2/5 (Faible) |
| **Impact** | 2/5 (Faible) |
| **Criticité** | **4/25 (Faible)** |
| **Période** | M12-M36 |

**Mitigation** : Avantage structurel open-source, agilité d'itération, proximité humaine, indépendance technologique.

### 2.3. Synthèse des risques

| Risque | P | I | Criticité | Priorité |
|---|---|---|---|---|
| **R1** — Adoption insuffisante | 4 | 4 | **16 (Élevée)** | Plan d'urgence |
| **R4** — Recrutement difficile | 4 | 4 | **16 (Élevée)** | Action immédiate |
| **R2** — Concurrence | 3 | 3 | **9 (Moyenne)** | Différenciation active |
| **R3** — Retard NIS2 | 3 | 3 | **9 (Moyenne)** | Réorientation possible |
| **R5** — Faux positifs | 3 | 3 | **9 (Moyenne)** | Atténué par QA |
| **R6** — Consolidation marché | 2 | 2 | **4 (Faible)** | Avantage structurel |

### 2.4. Facteurs critiques de succès (FCS)

#### Facteurs internes

| FCS | Description | Indicateur |
|---|---|---|
| **Qualité et fiabilité du produit** | Fonctionnement prévisible, faux positifs maîtrisés | Satisfaction > 4/5, faux positifs < 20 % |
| **Vitesse d'itération** | Intégration rapide des retours terrain | Bug critique < 48 h, release mensuelle |
| **Qualité documentation** | Déploiement autonome sans support | Installation < 30 min, documentation > 4/5 |
| **Stabilité équipe** | Continuité des membres clés | Rétention > 80 % sur 12 mois |
| **Industrialisation services** | Processus standardisés et reproductibles | Missions sans incident > 90 % |

#### Facteurs externes

| FCS | Description | Indicateur |
|---|---|---|
| **Dynamique NIS2** | Maintien du calendrier et du niveau d'exigence | Calendrier respecté, pas d'assouplissement |
| **Croissance marché PME** | Croissance à deux chiffres du marché cyber | Croissance > 8 %/an, budget en hausse |
| **Réseau partenaires MSP** | Engagement des distributeurs indirects | Partenaires actifs, volume d'affaires |
| **Notoriété GitHub** | Visibilité communautaire | Étoiles, forks, contributeurs, Trending |
| **Financement France 2030** | Obtention de l'enveloppe Cyber PME (100 M€) | Dossier déposé et éligible |

---

## Section 3 — Sources

### 3.1. Sources primaires (produites par l'équipe)

| Source | Emplacement | Apport |
|---|---|---|
| **KICKOFF.md** | `documents/01_documents_pedagogiques/kickoff/KICKOFF.md` | Besoin initial, contraintes techniques, grille de validation, périmètre fonctionnel minimal |
| **Étude de marché** | `documents/02_etude_de_marche/rendu_principal.md` | Chiffres clés, analyse concurrentielle, gap concurrentiel, segmentation clients, SWOT |
| **Business model** | `documents/03_business_model/rendu_principal.md` | Modèle open-core, structure des revenus, hypothèses de conversion, segments, canaux |
| **Business plan** | `documents/04_business_plan/rendu_principal.md` | Projections financières (84 K€ An 1, 338 K€ An 2, 881 K€ An 3), GTM 3 phases, KPI |
| **Registre transverse** | `documents/90_references_transverses/` | Définitions, acronymes, tables de correspondance (en cours de constitution) |

### 3.2. Sources externes citées

| Source | Type | Apport |
|---|---|---|
| [SMART criteria](https://en.wikipedia.org/wiki/SMART_criteria) | Méthodologique | Définition des critères de formulation des objectifs |
| [ANSSI](https://cyber.gouv.fr/) | Institutionnel | Chiffres clés de la menace cyber en France, référencement outil |
| [NIS2 Directive](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive) | Réglementaire | Cadre réglementaire, obligations de supervision, échéances 2027 |
| [France 2030](https://www.france2030.gouv.fr/) | Programme public | Enveloppe de 100 M€ pour la mise en conformité des PME |
| [GNU GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) | Licence | Option de licence open-source pour le cœur du produit |
| [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) | Licence | Option de licence open-source permissive |
| [OWASP Risk Rating](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology) | Technique | Méthodologie d'évaluation des risques de sécurité |
| [GitHub](https://github.com/) | Plateforme | Hébergement du code, release management, communauté |
| [FIC](https://www.forum-fic.com/) | Salon professionnel | Forum International de la Cybersécurité — visibilité et partenariats |
| [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) | Documentation | Gestion des versions et des livrables open-source |

### 3.3. Correspondance sources / sections

| Section de la feuille de cadrage | Sources principales |
|---|---|
| §1 Identification | KICKOFF.md |
| §2 Contexte et justification | KICKOFF.md, Étude de marché, ANSSI, NIS2 |
| §3 Objectifs | KICKOFF.md, Business model, Business plan |
| §4 Périmètre | KICKOFF.md, Cahier des charges |
| §5 Livrables | Business plan |
| §6 Planning macro | Business plan |
| §7 Parties prenantes | Étude de marché, Business model |
| §8 Budget et ressources | Business model, Business plan, France 2030 |
| §9 Risques | Business plan, Cahier des charges, OWASP |
| §10 Facteurs critiques de succès | Étude de marché, Business model |
| §11 Hypothèses et contraintes | Business model, Business plan |

---

*Document consolidé — Version 1.0 — Mai 2026*
