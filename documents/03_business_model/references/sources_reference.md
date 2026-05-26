# Références — Business Model

> **Documents de référence du modèle économique BigBrowser**
>
> *Consolidation v1.0 — Mai 2026*

---

## Table des matières

- [Section 1 : Cadrage méthodologique](#section-1--cadrage-methodologique)
- [Section 2 : Hypothèses de marché](#section-2--hypotheses-de-marche)
- [Section 3 : Modèle open-core](#section-3--modele-open-core)
- [Section 4 : Projections 3 ans](#section-4--projections-3-ans)
- [Section 5 : Sources de référence](#section-5--sources-de-reference)

---

## Section 1 : Cadrage méthodologique

> **Méthode : Lean Canvas / Business Model Canvas**
>
> *Référence v1.0 — Mai 2026*

### 1.1 Objectif

Ce document formalise le cadrage méthodologique du business model de BigBrowser. Il décrit la méthode employée (Lean Canvas et Business Model Canvas), les sources mobilisées, les décisions structurantes et le modèle retenu : l'open-core hybride.

### 1.2 Méthodologie

Le business model a été construit selon une approche combinant deux frameworks complémentaires.

#### 1.2.1 Business Model Canvas (BMC)

Le BMC fournit une vision complète et structurée des 9 blocs constitutifs du modèle :

| Bloc BMC | Application BigBrowser |
|---|---|
| Proposition de valeur | Supervision réseau complète, interface web unifiée, conformité NIS2, open-source |
| Segments de clientèle | PME françaises NIS2, secteur public, formation/éducation, MSP/SSII |
| Canaux | GitHub, site web, partenaires MSP, salons (FIC, Assises), référencement ANSSI |
| Relations client | Self-service (communauté), support payant, accompagnement audit, formation |
| Flux de revenus | Support mensuel, audits NIS2, formations, licences MSP |
| Ressources clés | Équipe technique, code source, marque/communauté, documentation |
| Activités clés | Développement produit, support client, audit NIS2, formation, marketing |
| Partenariats clés | MSP/SSII, ANSSI, écoles/formation, prestataires cloud |
| Structure de coûts | Salaires (>60 %), infrastructure (5-10 %), marketing (10-15 %), juridique |

#### 1.2.2 Lean Canvas

Le Lean Canvas a été utilisé pour identifier et prioriser les risques du modèle :

| Bloc Lean Canvas | Élément critique BigBrowser |
|---|---|
| Problème | Absence d'outil open-source unifié pour la supervision réseau PME |
| Solution | Plateforme web 8-en-1 (scan, détection, alertes, exports, dashboard) |
| Métriques clés | Déploiements (500 Y1), taux conversion (3-5 %), CA (84K→881K €) |
| Avantage concurrentiel | Interface web unifiée 8 fonctionnalités — inédit en open-source |
| Canaux | GitHub first, puis MSP, puis salons |
| Segments client | PME 10-250 employés (prioritaire), secteur public, éducation |
| Structure coûts | Allégée (infra légère, pas de licence tierce lourde) |
| Flux revenus | Services récurrents (support, MSP) + missions ponctuelles (audit, formation) |

### 1.3 Sources mobilisées

- **Étude de marché** (`documents/02_etude_de_marche/rendu_principal.md`) : données marché (6,4 Md€ France, 250 Md$ monde), analyse concurrentielle, segments cibles
- **Feuille de cadrage projet** : objectifs, périmètre, contraintes
- **Matrice de gestion des risques** : risques projet et marché

### 1.4 Positionnement stratégique

| Axe | Positionnement BigBrowser |
|---|---|
| Type de produit | Open-source de supervision réseau |
| Cible principale | PME françaises (10-250 employés) |
| Besoin adressé | Conformité NIS2 + visibilité réseau |
| Différenciateur clé | 8 fonctionnalités intégrées dans une interface web unifiée |
| Modèle de monétisation | Open-core hybride (produit gratuit, services payants) |
| Canal de distribution prioritaire | GitHub + site web (direct), MSP (indirect) |

### 1.5 Modèle retenu : open-core hybride

L'arbitrage entre les trois modèles candidats a été tranché comme suit :

| Critère | Pure open-source | Open-core hybride (retenu) | Propriétaire |
|---|---|---|---|
| Adoption | Maximale | Très élevée | Faible (friction licence) |
| Revenus | Aucun (dons seulement) | Multiples (support, audit, formation) | Licence + SaaS |
| Scalabilité | Limitée | Forte (effet réseau open-source + services) | Limitée (vente directe) |
| Alignement NIS2 | Oui | Oui | Oui |
| Risque concurrence | Faible (différenciation par services) | Maîtrisé (cœur gratuit attire, services fidélisent) | Élevé (prix, lock-in) |
| Complexité juridique | Faible | Modérée (licence open-source) | Élevée (contrats, protection) |

Le modèle open-core hybride a été retenu car il maximise l'adoption (cœur gratuit) tout en générant des revenus récurrents via des services à forte valeur ajoutée (support, audit, formation, MSP).

### 1.6 Hypothèses fondatrices

Les hypothèses suivantes sont au cœur du modèle et doivent être validées ou invalidées par l'expérience :

1. **Le marché PME cyber français croît structurellement** sous l'effet NIS2
2. **Un taux de conversion de 3 à 5 %** est atteignable (benchmark SaaS open-source)
3. **Les PME acceptent un coût de 280 €/mois** pour un support de supervision réseau
4. **Les MSP peuvent revendre BigBrowser** comme outil de diagnostic
5. **500 déploiements en année 1** sont réalisables via GitHub et les partenaires
6. **15 clients support en année 1** peuvent être convertis sur la base de 500 déploiements

### 1.7 Références

- Business Model Canvas original : Osterwalder & Pigneur, *Business Model Generation*, 2010
- Lean Canvas : Ash Maurya, *Running Lean*, 2012
- Open-core model : Sid Sijbrandij (GitLab) / Sources historiques open-source
- Benchmark conversion SaaS open-source : données publiques GitLab, Mattermost, Grafana
- Étude de marché BigBrowser (Avril 2026)
- Feuille de cadrage projet BigBrowser (Avril 2026)

---

## Section 2 : Hypothèses de marché

> **22 paramètres du modèle économique**
>
> *Référence v1.0 — Mai 2026*

### 2.1 Présentation

Ce document détaille les 22 hypothèses qui fondent le modèle économique de BigBrowser. Chaque paramètre est issu du fichier `business_model_assumptions.csv` (cf. [annexes](../annexes/business_model_assumptions.csv)). Ces hypothèses couvrent le marché, la conversion, le pricing, les objectifs de déploiement et les ressources disponibles.

### 2.2 Paramètres de marché

| Paramètre | Valeur | Unité | Source |
|---|---|---|---|
| `market_size_france_2025` | 6,4 | Md€ | PAC |
| `market_growth_rate` | 10 | % | PAC |
| `sam_france_be_ch` | 195,2 | M€ | Calcul bottom-up |
| `som_24_36_months` | 4,2 | M€ | Business plan |
| `nis2_entities_france` | 15 000 | entités | ANSSI |
| `nis2_deadline` | 2027 | année | ANSSI |
| `france_2030_envelope` | 100 | M€ | France 2030 Cyber PME |

#### 2.2.1 Analyse du marché adressable

Le marché français de la cybersécurité est estimé à **6,4 milliards d'euros en 2025**, avec un taux de croissance annuel de **10 %**. Le SAM (Serviceable Addressable Market) France, Belgique et Suisse est estimé à **195,2 M€** par calcul bottom-up, en segmentant par type d'organisation assujettie à NIS2.

Le SOM (Serviceable Obtainable Market) à 24-36 mois est projeté à **4,2 M€**, soit environ **2,2 % du SAM**, ce qui constitue une hypothèse prudente pour un acteur open-source émergent.

#### 2.2.2 Catalyseur réglementaire NIS2

La directive NIS2 constitue le catalyseur principal du modèle :

- **15 000 entités** françaises devant se conformer d'ici 2027 (source ANSSI)
- Supervision réseau devenue obligatoire
- Calendrier connu et non négociable → fenêtre d'opportunité temporelle

#### 2.2.3 Enveloppe France 2030 Cyber PME

**100 millions d'euros** sont disponibles via le programme France 2030 Cyber PME. Ce dispositif peut financer tout ou partie des déploiements BigBrowser chez les PME cibles. Il constitue une opportunité de passage à l'échelle pour la phase 3 (Mois 18-36).

### 2.3 Paramètres de conversion

| Paramètre | Valeur | Unité | Source |
|---|---|---|---|
| `conversion_rate_min` | 3 | % | Benchmark SaaS open-source |
| `conversion_rate_max` | 5 | % | Benchmark SaaS open-source |

#### 2.3.1 Justification du taux de conversion

Le taux de conversion de 3 à 5 % est aligné sur les benchmarks observés chez les éditeurs open-source comparables (GitLab, Mattermost, Grafana) :

- **3 %** : hypothèse prudente, utilisée dans le scénario de base
- **5 %** : hypothèse optimiste, utilisée dans le scénario optimiste

Ces taux s'appliquent au nombre de déploiements actifs pour estimer le nombre de clients support, d'audits et de formations.

### 2.4 Paramètres de pricing

| Paramètre | Valeur | Unité | Note |
|---|---|---|---|
| `support_monthly_price` | 280 | €/mois | Support Essentiel |
| `audit_mission_price` | 3 000 | €/mission | Audit NIS2 de base |
| `training_group_price` | 2 500 | €/groupe | Formation inter-entreprises |
| `msp_monthly_price` | 400 | €/mois | Licence partenaire MSP |

#### 2.4.1 Logique de pricing

- **Support** : 280 €/mois (prix compétitif face aux SIEM propriétaires à 500-2000+ €/mois)
- **Audit** : 3 000 €/mission (forfait adapté au budget PME, 2-3 jours d'intervention)
- **Formation** : 2 500 €/groupe (inter-entreprises, 8-12 participants)
- **MSP** : 400 €/mois (licence + support technique, revente possible par le partenaire)

### 2.5 Paramètres d'objectifs

| Paramètre | Valeur | Unité |
|---|---|---|
| `support_target_y1` | 15 | clients |
| `audit_target_y1` | 10 | missions |
| `training_target_y1` | 5 | groupes |
| `msp_target_y1` | 2 | partenaires |
| `deployments_target_y1` | 500 | déploiements |

#### 2.5.1 Relation entre déploiements et clients

L'estimation des clients support (15 en Y1) est dérivée du nombre de déploiements cible (500) et du taux de conversion (3 %) :

`15 = 500 × 3 %`

Cette hypothèse de conversion est conservative et pourra être ajustée à la hausse si la courbe d'adoption est plus rapide que prévu.

### 2.6 Paramètres financiers

| Paramètre | Valeur | Unité |
|---|---|---|
| `ca_target_y1` | 84 000 | € |
| `ca_target_y2` | 338 000 | € |
| `ca_target_y3` | 881 000 | € |

#### 2.6.1 Structure de progression

La progression du chiffre d'affaires suit une courbe de croissance forte :

- **Y1 → Y2** : +302 % (effet base faible + premiers contrats récurrents annualisés)
- **Y2 → Y3** : +161 % (montée en charge MSP + récurrence support + audits)

### 2.7 Synthèse des risques associés aux hypothèses

| Hypothèse | Risque si non vérifiée | Impact |
|---|---|---|
| Taux de conversion 3-5 % | Clients insuffisants pour atteindre le CA cible | Critique |
| 500 déploiements Y1 | Base d'adoption trop faible pour générer des conversions | Critique |
| Prix support 280 €/mois accepté | Rejet du pricing par les PME | Élevé |
| Marché NIS2 = 15 000 entités | Marché plus petit ou calendrier repoussé | Élevé |
| Croissance 10 %/an du marché | Ralentissement macro-économique | Modéré |

### 2.8 Références

- Fichier source : `annexes/business_model_assumptions.csv`
- Étude de marché BigBrowser (Avril 2026)
- ANSSI — Rapport d'activité 2024
- France 2030 — Cyber PME, enveloppe 100 M€
- Benchmark conversion SaaS open-source : GitLab, Mattermost, Grafana (données publiques)

---

## Section 3 : Modèle open-core

> **4 familles de services, licence open-source, grille de prix**
>
> *Référence v1.0 — Mai 2026*

### 3.1 Principe du modèle open-core

BigBrowser adopte un modèle **open-core hybride** : le produit cœur (core product) est distribué gratuitement sous licence open-source, tandis que la monétisation est construite autour de services à valeur ajoutée.

Ce modèle repose sur un constat simple : **les PME n'ont pas besoin d'acheter une licence logicielle**, elles ont besoin d'être accompagnées dans leur mise en conformité NIS2. Le produit gratuit est le moteur d'adoption ; les services payants sont le moteur de revenus.

### 3.2 Les 4 familles de services

#### 3.2.1 Support & Maintenance

| Tier | Prix | Inclus | Cible |
|---|---|---|---|
| Essential | 280 €/mois | Support prioritaire (tickets), mises à jour, corrections, documentation étendue | PME avec besoin de continuité |
| Premium | 500 €/mois | Essential + SLA 24h, support téléphonique, onboarding accompagné | PME/ETI avec enjeux critiques |
| Enterprise | Sur devis | Premium + engagement SLA personnalisé, support dédié, déploiement assisté | Grands comptes, collectivités |

#### 3.2.2 Audits & Conformité NIS2

| Prestation | Prix | Contenu | Volume cible Y1 |
|---|---|---|---|
| NIS2 Basic | 3 000 € | Audit de conformité NIS2 sur site ou distanciel, rapport d'analyse, plan d'actions | 10 missions |
| NIS2 Full | 5 000 € | Basic + diagnostic réseau complet BigBrowser, préconisations détaillées, accompagnement post-audit | 5 missions |

Les audits constituent le service à plus forte marge (peu ou pas de coût technique récurrent, valorisation de l'expertise).

#### 3.2.3 Formation

| Format | Prix | Durée | Public |
|---|---|---|---|
| Inter-entreprises | 2 500 €/groupe | 2 jours (8-12 participants) | DSI, analystes, administrateurs |
| Sur site (intra) | 5 000 €/jour | 1-2 jours, sur mesure | Équipes IT, services cybersécurité |

La formation inter-entreprises est le produit d'appel ; la formation sur site est le produit à plus forte valeur.

#### 3.2.4 Canal MSP (Managed Service Providers)

| Offre | Prix | Inclus |
|---|---|---|
| Licence partenaire | 400 €/mois | Licence de revente, support technique prioritaire, accès documentation revendeur |
| Certification | 2 000 € (one-time) | Formation certifiante, kit de déploiement client, badge partenaire |

Le canal MSP est stratégique pour la phase 2 (Mois 6-18) : il permet de scaler la distribution sans alourdir la structure de vente directe.

### 3.3 Grille de prix consolidée

Source : [`annexes/pricing_grid.csv`](../annexes/pricing_grid.csv)

| Service | Tier | Prix unitaire | Cycle |
|---|---|---|---|
| Support | Essential | 280 € | Mensuel |
| Support | Premium | 500 € | Mensuel |
| Support | Enterprise | Sur devis | Personnalisé |
| Audit | NIS2 Basic | 3 000 € | Par mission |
| Audit | NIS2 Full | 5 000 € | Par mission |
| Formation | Inter-entreprises | 2 500 € | Par groupe |
| Formation | Sur site | 5 000 € | Par jour |
| MSP | Licence partenaire | 400 € | Mensuel |
| MSP | Certification | 2 000 € | One-time |

### 3.4 Licence open-source

#### 3.4.1 Licence retenue

Deux options sont en arbitrage :

| Critère | GPLv2 | Apache 2.0 |
|---|---|---|
| Copyleft | Fort | Faible |
| Compatibilité commerciale | Modérée (contamination) | Bonne |
| Protection brevet | Non | Oui |
| Adoption entreprise | Modérée | Élevée |
| Communauté open-source | Historique large | Large |
| Recommandation projet | Option A (par défaut) | Option B |

**Recommandation provisoire** : GPLv2 pour garantir que les améliorations restent dans la communauté, avec une clause de compatibilité pour les intégrations tierces. L'arbitrage final nécessite un conseil juridique spécialisé en propriété intellectuelle open-source.

#### 3.4.2 Implication du choix de licence

Le choix de licence impacte directement :

- **La contribution** : GPLv2 peut freiner certains contributeurs corporate par crainte de contamination
- **La distribution** : GPLv2 impose de distribuer le code source avec les binaires
- **Le modèle de services** : aucune des deux licences n'empêche la vente de services (support, audit, formation)
- **Les intégrations** : Apache 2.0 facilite l'intégration avec des outils propriétaires

### 3.5 Justification du modèle open-core vs alternatives

#### 3.5.1 Pourquoi pas 100 % open-source ?

Le modèle 100 % open-source (financement par dons uniquement) ne permet pas de couvrir les charges salariales (>60 % des coûts) et ne génère pas de revenus prévisibles. Il repose sur des mécanismes de financement incertains (Open Collective, GitHub Sponsors).

#### 3.5.2 Pourquoi pas totalement propriétaire ?

Le modèle propriétaire crée une friction à l'adoption (essai limité, licence coûteuse, lock-in) qui est incompatible avec la cible PME :

- Budget inférieur à 1 000 €/an pour 60 % des PME
- Aucun outil propriétaire ne couvre les 8 fonctionnalités en dessous de 500 €/mois
- La concurrence Wazuh (open-source) est déjà installée chez les PME les plus matures

#### 3.5.3 Pourquoi open-core hybride ?

L'open-core hybride combine les avantages des deux mondes :

- **Produit gratuit** → adoption massive, pas de barrière à l'entrée
- **Services payants** → revenus récurrents et scalables
- **Alignement PME** : elles paient pour l'accompagnement, pas pour la licence
- **Effet réseau** : plus le produit est déployé, plus la marque gagne en crédibilité
- **Communauté** : les utilisateurs gratuits contribuent au produit (issues, documentation, retours)

### 3.6 Schéma du funnel de conversion

```text
Déploiements GitHub          → 500 (Y1)
    ↓ (taux conversion 3-5 %)
Clients support              → 15 (Y1)
    ↓ (upsell naturel)
Audits NIS2                  → 10 missions (Y1)
    ↓ (cross-sell)
Formations                   → 5 groupes (Y1)
    ↓ (effet réseau)
Partenaires MSP              → 2 (Y1)
```

### 3.7 Références

- Fichier source pricing : `annexes/pricing_grid.csv`
- Fichier source hypothèses : `annexes/business_model_assumptions.csv`
- Rendu principal business model : `../rendu_principal.md`
- Analyse des modèles open-source : GitLab (Sid Sijbrandij), Mattermost, Grafana Labs
- Licences : GNU GPLv2 (Free Software Foundation), Apache License 2.0 (Apache Software Foundation)

---

## Section 4 : Projections 3 ans

> **CA 84K → 338K → 881K €, scénarios, KPIs et structure de coûts**
>
> *Référence v1.0 — Mai 2026*

### 4.1 Compte de résultat prévisionnel — Scénario de base

#### 4.1.1 Chiffre d'affaires par source de revenus

Source : [`annexes/forecast_3y_base.csv`](../annexes/forecast_3y_base.csv)

| Source de revenus | Année 1 | Année 2 | Année 3 | Croissance Y1→Y3 |
|---|---|---|---|---|
| Support & maintenance | 33 600 € | 145 000 € | 380 000 € | ×11,3 |
| Audits NIS2 | 30 000 € | 105 000 € | 280 000 € | ×9,3 |
| Formations | 12 500 € | 50 000 € | 125 000 € | ×10 |
| Licences MSP | 9 600 € | 38 400 € | 96 000 € | ×10 |
| **Total CA** | **84 000 €** | **338 400 €** | **881 000 €** | **×10,5** |

#### 4.1.2 Structure de coûts prévisionnelle

| Poste de charge | Y1 | Y2 | Y3 | % CA Y3 |
|---|---|---|---|---|
| Salaires & charges (équipe) | ~55 000 € | ~180 000 € | ~400 000 € | ~45 % |
| Infrastructure & CI/CD | ~5 000 € | ~15 000 € | ~45 000 € | ~5 % |
| Marketing & salons | ~10 000 € | ~35 000 € | ~90 000 € | ~10 % |
| Outils & licences | ~2 000 € | ~8 000 € | ~25 000 € | ~3 % |
| Frais juridiques & admin | ~3 000 € | ~10 000 € | ~25 000 € | ~3 % |
| **Total charges** | **~75 000 €** | **~248 000 €** | **~585 000 €** | **~66 %** |
| **Résultat d'exploitation** | **~9 000 €** | **~90 400 €** | **~296 000 €** | **~34 %** |
| **Marge opérationnelle** | **~10,7 %** | **~26,7 %** | **~33,6 %** | |

#### 4.1.3 Hypothèses de construction du compte de résultat

**Année 1** (démarrage progressif) :
- Support : 15 clients × 280 € × 8 mois (démarrage en mai, pas janvier)
- Audits : 10 missions × 3 000 €
- Formations : 5 groupes × 2 500 €
- MSP : 2 partenaires × 400 € × 12 mois
- 1 ETP à temps partiel + expert externalisé pour les audits

**Année 2** (montée en charge) :
- Support : 60 clients × 280 € × 9 mois (annualisation progressive)
- Audits : 35 missions × 3 000 €
- Formations : 20 groupes × 2 500 €
- MSP : 10 partenaires × 400 € × 12 mois (effet réseau)
- 2-3 ETP dont 1 commercial, 1 support technique, 1 expert cyber

**Année 3** (industrialisation) :
- Support : 150 clients × 280 € × 12 mois (récurrence annualisée)
- Audits : 80 missions × 3 500 € (prix moyen en hausse avec la réputation)
- Formations : 50 groupes × 2 500 €
- MSP : 20 partenaires × 400 € × 12 mois

### 4.2 Scénarios — Analyse de sensibilité

Source : [`annexes/scenario_model.csv`](../annexes/scenario_model.csv)

| Scénario | Déploiements Y1 | Taux conversion | CA Y1 |
|---|---|---|---|
| **Base case** | 500 | 3 % | 84 000 € |
| **Optimistic** | 800 | 5 % | 140 000 € |
| **Pessimistic** | 300 | 2 % | 50 000 € |

#### 4.2.1 Projection des 3 scénarios sur 3 ans

| Scénario | Y1 | Y2 | Y3 | Commentaire |
|---|---|---|---|---|
| Base | 84 K€ | 338 K€ | 881 K€ | Croissance régulière, marché NIS2 confirmé |
| Optimistic | 140 K€ | 520 K€ | 1 250 K€ | Adoption accélérée, 2-3 MSP majeurs signés Y1 |
| Pessimistic | 50 K€ | 180 K€ | 450 K€ | Marché plus lent, concurrence agressive |

#### 4.2.2 Analyse des points d'attention par scénario

**Scénario pessimiste** :
- Si le marché NIS2 est plus lent que prévu (calendrier repoussé après 2027)
- Si Wazuh ou PRTG captent la majorité des déploiements
- Si le taux de conversion réel est < 2 %
- Seuil plancher : 50 K€/an permet de survivre avec 0,5 ETP et peu d'investissement

**Scénario optimiste** :
- Si le gap concurrentiel se confirme (8 fonctionnalités unifiées)
- Si France 2030 Cyber PME finance des déploiements groupés
- Si 2-3 MSP de taille significative adoptent BigBrowser comme outil standard

### 4.3 Plan de mix canal

Source : [`annexes/channel_mix_plan.csv`](../annexes/channel_mix_plan.csv)

| Canal | Année 1 | Année 2 | Année 3 | Évolution |
|---|---|---|---|---|
| Vente directe | 70 % | 60 % | 50 % | Décroissance volontaire |
| Partenaires MSP | 20 % | 30 % | 35 % | Croissance forte |
| Éducation / Formation | 10 % | 10 % | 15 % | Croissance modérée |
| **Total** | **100 %** | **100 %** | **100 %** | |

La stratégie canal prévoit un **transfert progressif de la vente directe vers le canal indirect MSP**. En année 1, la vente directe représente 70 % des revenus (nécessaire pour établir le produit). En année 3, les MSP représentent 35 % des revenus, permettant de scaler sans augmenter proportionnellement la force commerciale interne.

### 4.4 KPIs cibles

Source : [`annexes/kpi_targets.csv`](../annexes/kpi_targets.csv)

| KPI | Année 1 | Année 2 | Année 3 |
|---|---|---|---|
| Déploiements | 500 | 2 000 | 5 000 |
| GitHub stars | 100 | 500 | 1 500 |
| GitHub forks | 20 | 100 | 300 |
| Contributeurs actifs | 5 | 20 | 50 |
| Clients support | 15 | 60 | 150 |
| Missions d'audit | 10 | 35 | 80 |
| Partenaires MSP | 2 | 10 | 20 |
| Chiffre d'affaires | 84 000 € | 338 000 € | 881 000 € |
| Marge opérationnelle | ~10,7 % | ~26,7 % | ~33,6 % |

#### 4.4.1 Relation entre les KPIs

Les KPIs sont liés entre eux par des relations de cause à effet :

```text
GitHub stars + forks → notoriété → déploiements → clients support
                                                        ↓
                                               audits + formations + MSP
```

La croissance des déploiements (500 → 5 000) est le moteur principal de l'ensemble des autres KPIs commerciaux.

### 4.5 Seuil de rentabilité (Break-even)

- **Point mort estimé** : ~300 déploiements actifs avec 3 % de conversion
- **Revenu mensuel récurrent (MRR) cible Y1** : ~7 000 €/mois
- **MRR cible Y2** : ~28 000 €/mois
- **MRR cible Y3** : ~73 000 €/mois

Le modèle devient rentable dès lors que le MRR couvre les charges fixes mensuelles (~5 000 €/mois en Y1).

### 4.6 Analyse de sensibilité

| Variable | Variation | Impact sur CA Y3 |
|---|---|---|
| Taux de conversion (3 % → 4 %) | +33 % | +293 K€ (+33 %) |
| Prix support (280 → 350 €/mois) | +25 % | +~135 K€ |
| Nombre déploiements Y1 (500 → 400) | -20 % | -~60 K€ |
| Missions audit (10 → 7) | -30 % | -~9 K€ en Y1 |

La variable la plus sensible est le **taux de conversion**, qui impacte directement le nombre de clients support et donc le MRR.

### 4.7 Références

- Fichiers sources : `annexes/forecast_3y_base.csv`, `annexes/kpi_targets.csv`, `annexes/channel_mix_plan.csv`, `annexes/scenario_model.csv`
- Rendu principal business model : `../rendu_principal.md`
- Benchmark SaaS open-source : GitLab, Mattermost, Grafana Labs (données publiques financières)

---

## Section 5 : Sources de référence

> **Registre des sources formelles, fichiers CSV et documents connexes**
>
> *Référence v1.0 — Mai 2026*

### 5.1 Sources documentaires primaires

Les documents suivants constituent les sources fondatrices du business model BigBrowser :

| Document | Emplacement | Usage dans le business model |
|---|---|---|
| Étude de marché (rendu principal) | `documents/02_etude_de_marche/rendu_principal.md` | Données marché, concurrence, segments, TAM/SAM/SOM |
| Feuille de cadrage projet | `documents/01_documents_pedagogiques/` | Objectifs, périmètre, contraintes projet |
| Cahier des charges | `documents/06_cahier_des_charges/rendu_principal.md` | Exigences produit, matrice traçabilité, scénarios recette |
| Architecture | `documents/08_architecture/rendu_principal.md` | Architecture technique, composants, flux |
| Business plan | `documents/04_business_plan/rendu_principal.md` | Stratégie, plan d'actions, jalons |

### 5.2 Fichiers annexes — Données chiffrées

Les fichiers CSV suivants sont produits dans le dossier `annexes/` et constituent les données sources des projections financières et des hypothèses du modèle :

| Fichier | Contenu | Utilisation |
|---|---|---|
| [`business_model_assumptions.csv`](../annexes/business_model_assumptions.csv) | 22 paramètres du modèle (marché, conversion, pricing, objectifs) | Fondement chiffré de toutes les projections |
| [`pricing_grid.csv`](../annexes/pricing_grid.csv) | Grille de prix détaillée (9 lignes de service) | Définition des tarifs support, audit, formation, MSP |
| [`forecast_3y_base.csv`](../annexes/forecast_3y_base.csv) | Projection CA 3 ans par source de revenus (scénario base) | Compte de résultat prévisionnel |
| [`kpi_targets.csv`](../annexes/kpi_targets.csv) | 9 KPIs cibles sur 3 ans | Tableau de bord et suivi performance |
| [`channel_mix_plan.csv`](../annexes/channel_mix_plan.csv) | Mix canal direct/MSP/éducation sur 3 ans | Plan de distribution |
| [`scenario_model.csv`](../annexes/scenario_model.csv) | 3 scénarios (Base/Optimistic/Pessimistic) | Analyse de sensibilité |

### 5.3 Sources externes — Liens

- [Lean Canvas / Strategyzer](https://www.strategyzer.com/)
- [Business Model Canvas](https://www.strategyzer.com/library/the-business-model-canvas)
- [GNU GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html)
- [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
- [Modèle open-core (Wikipedia)](https://en.wikipedia.org/wiki/Open-core_model)
- [ANSSI](https://cyber.gouv.fr/)
- [NIS2 Directive](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive)
- [France 2030](https://www.france2030.gouv.fr/)
- [INSEE](https://www.insee.fr/)

### 5.4 Sources transverses

Le registre transverse du projet ([`documents/90_references_transverses/`](../../90_references_transverses/)) référence les sources externes suivantes utilisées dans le business model :

#### Sources marché

- **PAC** — Données marché cybersécurité France 2025 (taille, croissance, segments)
- **ANSSI** — Rapport d'activité 2024, chiffres NIS2
- **Mordor Intelligence** — Marché mondial supervision réseau
- **Gartner** — Marché SIEM, gestion des événements de sécurité
- **OPIIEC** — Observations économiques cybersécurité France

#### Sources réglementaires

- **Directive NIS2 (2022/2555)** — Texte officiel et calendrier de transposition
- **France 2030 Cyber PME** — Enveloppe, critères d'éligibilité, calendrier

#### Sources benchmark open-source

- **GitLab** — Modèle open-core, données publiques conversion et pricing
- **Mattermost** — Modèle open-core, pricing support
- **Grafana Labs** — Modèle open-source + services
- **Wazuh** — Concurrent direct open-source SIEM/XDR

#### Sources méthodologiques

- **Osterwalder & Pigneur** — Business Model Generation, 2010
- **Ash Maurya** — Running Lean, 2012
- **OWASP ASVS** — Application Security Verification Standard

### 5.5 Cartographie des liens entre documents et fichiers

```text
Références transverses
    ↓
Étude de marché (02_etude_de_marche)
    ↓
Business Model (03_business_model)
    ├── rendu_principal.md              ← synthèse
    ├── references/
    │   └── sources_reference.md        ← registre consolidé des sources
    └── annexes (6 fichiers CSV)
    ↓
Business Plan (04_business_plan)
    ↓
Cahier des charges (06_cahier_des_charges)
```

### 5.6 Notes de version

| Version | Date | Modifications |
|---|---|---|
| v1.0 | Mai 2026 | Consolidation des 5 documents de référence en un fichier unique — couvre cadrage, hypothèses, modèle open-core, projections et sources |
