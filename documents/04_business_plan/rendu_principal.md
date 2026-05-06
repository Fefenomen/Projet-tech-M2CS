# Business Plan — BigBrowser

> **Plan de Développement Commercial & Opérationnel**
>
> *Avril 2026*

---

## Table des matières

1. [Résumé Exécutif](#1-résumé-exécutif)
2. [Description de l'Entreprise](#2-description-de-lentreprise)
3. [Analyse de Marché](#3-analyse-de-marché)
4. [Offre de Produits & Services](#4-offre-de-produits--services)
5. [Stratégie Go-to-Market](#5-stratégie-go-to-market)
6. [Organisation & Équipe](#6-organisation--équipe)
7. [Exploitation & Processus](#7-exploitation--processus)
8. [Plan de Développement](#8-plan-de-développement)
9. [Analyse des Risques](#9-analyse-des-risques)
10. [Projections Financières](#10-projections-financières)
11. [Besoins de Financement](#11-besoins-de-financement)
12. [Indicateurs de Performance (KPI)](#12-indicateurs-de-performance-kpi)
13. [Conclusion & Perspectives](#13-conclusion--perspectives)

---

## 1. Résumé Exécutif

BigBrowser est un projet de cybersurveillance réseau orienté SOC, adoptant un modèle **open-core hybride**. L'entreprise développe un outil de supervision et d'analyse réseau open-source, ciblant prioritairement les PME françaises soumises à la directive NIS2.

### Chiffres clés

| Indicateur | Année 1 | Année 2 | Année 3 |
|---|---|---|---|
| Chiffre d'Affaires | **84 000 €** | **338 000 €** | **881 000 €** |
| Nombre de déploiements | 500 | 2 000 | 5 000 |
| Clients support actifs | 15 | 60 | 150 |
| Missions d'audit | 10 | 35 | 80 |
| Partenaires MSP | 2 | 10 | 20+ |

### Proposition de valeur unique

> **"Splunk pour les PME, sans le prix de Splunk"**
>
> Une solution tout-en-un avec interface web unifiée, couvrant les 8 fonctionnalités clés de supervision réseau, déployable on-premise, conforme NIS2, et distribuée gratuitement en open-source.

---

## 2. Description de l'Entreprise

### 2.1. Identité

| Élément | Valeur |
|---|---|
| **Nom du projet** | BigBrowser |
| **Nature** | Outil open-source de supervision et d'analyse réseau |
| **Modèle économique** | Open-core + Services (Support, Audit, Formation) |
| **Cible prioritaire** | PME françaises (10–250 employés) soumises à NIS2 |
| **Date de lancement** | Avril 2026 (v1.0 prévue en octobre 2026) |
| **Statut juridique** | À définir (SARL / SAS envisagée) |

### 2.2. Mission & Vision

**Mission :** Démocratiser la supervision réseau pour les PME en proposant un outil professionnel, accessible et conforme aux exigences réglementaires NIS2.

**Vision :** Devenir la référence open-source de supervision réseau pour les PME en France et Europe francophone d'ici 2029.

### 2.3. Valeurs

- **Accessibilité** : Outil gratuit, interface web simple, sans expertise CLI requise
- **Conformité** : Alignement strict avec les exigences NIS2
- **Transparence** : Code open-source, communauté active
- **Excellence technique** : Stack moderne (Python/FastAPI), architecture défendable

---

## 3. Analyse de Marché

### 3.1. Taille du marché

| Segment | Valeur 2025 | Croissance | Source |
|---|---|---|---|
| Marché mondial cyber | >250 Md$ | +12%/an | Gartner |
| Marché France cyber | 6,4 Md€ | +10%/an | PAC |
| SIEM / SOC France | 441 M€ | +16%/an | PAC |
| Supervision réseau mondial | 4,1 Md$ | +9,5%/an | Mordor Intelligence |

### 3.2. Marché adressé (SAM)

- **15 000 entités françaises** soumises à NIS2 (ANSSI)
- **PME cibles** : 75 % des cyberattaques françaises les ciblent
- **Budget PME** : 3/4 investissent moins de 2 000 €/an en cyber

### 3.3. Analyse concurrentielle

| Outil | Découverte | Scan ports | Trafic | Alertes | Interface web | Export CSV/JSON |
|---|---|---|---|---|---|---|
| **BigBrowser (cible)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Nmap | ✅ | ✅ | ❌ | ⚠️ | ❌ | ❌ |
| Wireshark | ❌ | ❌ | ✅ | ❌ | ❌ | ⚠️ |
| Suricata | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ |
| Wazuh | ⚠️ | ❌ | ⚠️ | ✅ | ✅ | ✅ |
| Splunk | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Avantage concurrentiel :** Splunk est le seul concurrent complet, mais inaccessible financièrement pour les PME.

---

## 4. Offre de Produits & Services

### 4.1. Produit Core (Gratuit — Open-Source)

| Fonctionnalité | Description | Priorité |
|---|---|---|
| Scan de plages IP | Découverte d'équipements réseau | P1 |
| Détection ports ouverts | Identification services réseau | P1 |
| Capture trafic réseau | Analyse des flux | P1 |
| Détection comportements | Règles simples de détection | P1 |
| Système d'alertes | Alertes configurables et actionnables | P1 |
| Interface web unifiée | Tableau de bord temps réel | P1 |
| Exports CSV/JSON | Rapports pour audit et conformité NIS2 | P1 |
| Déploiement on-premise | Sans dépendance cloud | P1 |

### 4.2. Services Premium (Payants)

| Service | Description | Tarif | Objectif An 1 |
|---|---|---|---|
| **Support Essentiel** | Support prioritaire, mises à jour, corrections | 280 €/mois | 15 clients |
| **Audit NIS2** | Mission conformité, rapport analyse | 3 000 €/mission | 10 missions |
| **Formation** | Inter-entreprises/sur site, TP BigBrowser | 2 500 €/groupe | 5 groupes |
| **Partenariat MSP** | Licence revendeur, support dédié | 400 €/mois | 2 MSP |

---

## 5. Stratégie Go-to-Market

### 5.1. Phase 1 — Lancement & Traction (M1–M6)

**Objectifs :**
- Publication v1.0 sur GitHub avec README et documentation
- 500 déploiements visés
- 5 à 10 PME pilotes (gratuit contre REX)
- Participation FIC et Les Assises

**Actions clés :**
- Référencement ANSSI, Cybermalveillance.gouv.fr
- Présence GitHub Trending (stratégie de contenu)
- Activation 2 premiers partenaires MSP

**Jalons :** Release v1.0 — 500 déploiements — 2 MSP partenaires

### 5.2. Phase 2 — Monétisation (M6–M18)

**Objectifs :**
- 15 clients support (CA ~33k€)
- 10 missions d'audit (CA ~30k€)
- CA An 1 : ~84 000 €

**Actions clés :**
- Lancement offre support Essentiel
- Programme certification partenaires MSP
- Formations inter-entreprises
- Catalogue achats publics

### 5.3. Phase 3 — Industrialisation (M18–M36)

**Objectifs :**
- CA An 3 : ~881 000 €
- 20+ partenaires MSP
- 5 000 déploiements

**Actions clés :**
- Modules premium (IA/ML, dashboard NIS2)
- Extension réseau MSP
- Exploration offre SaaS hébergée
- Dossier France 2030 Cyber PME (100 M€)

---

## 6. Organisation & Équipe

### 6.1. Équipe cœur (Phase 1)

| Rôle | Compétences requises | Disponibilité | Statut |
|---|---|---|---|
| **Chef de projet / PO** | Gestion projet, vision produit, cyber | Temps plein | À recruter |
| **Développeur senior** | Python, FastAPI, sécurité réseau | Temps plein | À recruter |
| **Expert cyber** | NIS2, audit, IDS/IPS, Wireshark, Nmap | Partiel / prestation | À recruter |
| **Commercial / BizDev** | Vente B2B, partenariats, PME/MSP | Partiel (Phase 1) | À recruter |

### 6.2. Parties prenantes

| Partie prenante | Type | Intérêt | Implication |
|---|---|---|---|
| PME françaises | Client cible | Conformité NIS2, visibilité réseau | Fort |
| MSP / SSII | Canal indirect | Différenciation offre, upsell | Fort |
| ANSSI | Institutionnel | Conformité réglementaire | Moyen |
| Communauté GitHub | Contributeurs | Amélioration code, notoriété | Faible (Phase 1) |

---

## 7. Exploitation & Processus

### 7.1. Cycle de développement

- **Méthodologie** : Agile/Scrum, sprints de 2 semaines
- **Stack technique** : Python / FastAPI / HTML/CSS/JS
- **Déploiement** : On-premise (sans cloud), GitHub public
- **Qualité** : Tests automatisés, lint, typecheck

### 7.2. Processus de support

1. Client souscrit au support Essentiel
2. Accès portail support prioritaire
3. Gestion tickets avec SLA défini
4. Remontée bugs vers équipe dev
5. Mises à jour incluses

### 7.3. Processus d'audit NIS2

1. Prise de contact et diagnostic initial
2. Scan réseau avec BigBrowser
3. Analyse des résultats et écarts NIS2
4. Rapport de conformité détaillé
5. Préconisations et plan d'action

---

## 8. Plan de Développement

### 8.1. Jalons clés

| Date | Jalon | Livrable |
|---|---|---|
| Mois 4 | Catalogue de services | Offres support, audit, formation |
| Mois 5 | Site web & landing page | Présentation, téléchargement |
| **Mois 6** | **Release v1.0 GitHub** | **Code source, README, doc** |
| Mois 6 | 500 déploiements | Métriques GitHub |
| Mois 9 | Premiers contrats signés | Support, audit, formation |
| Mois 12 | 2 MSP partenaires | Contrats signés |
| Mois 18 | CA An 1 : 84k€ | Bilan financier |
| Mois 36 | CA An 3 : 881k€ | Positionnement leader |

### 8.2. Livrables attendus

| Livrable | Description | Échéance | Responsable |
|---|---|---|---|
| Dépôt GitHub v1.0 | Code source, README, doc installation | Mois 6 | Équipe dev |
| Documentation utilisateur | Guide installation, cas d'usage NIS2 | Mois 6 | Équipe dev |
| Catalogue de services | Offres support, audit, formation, MSP | Mois 4 | Commercial |
| Site web & landing | Présentation, téléchargement, contact | Mois 5 | Marketing |
| Rapports PME pilotes | REX de 5 à 10 PME pilotes | Mois 6 | Chef de projet |
| Premiers contrats | Support, audit et/ou formation | Mois 9 | Commercial |
| Partenariats MSP | 2 MSP intégrés au réseau | Mois 12 | Commercial |

---

## 9. Analyse des Risques

| # | Risque | Probabilité | Impact | Criticité | Mitigation |
|---|---|---|---|---|---|
| R1 | Adoption open-source insuffisante | Élevée | Élevé | **16** | Stratégie contenu, FIC, partenariat ANSSI |
| R2 | Concurrence (Wazuh, PRTG) | Moyenne | Moyen | **9** | Différenciation UX, interface unifiée |
| R3 | Retard transposition NIS2 | Moyenne | Moyen | **9** | Valeur opérationnelle indépendante réglementation |
| R4 | Difficulté recrutement cyber | Élevée | Élevé | **16** | Partenariats écoles, alternances |
| R5 | Faux positifs nuisant à crédibilité | Moyenne | Moyen | **9** | Investissement QA, bêta-test, feedback |
| R6 | Consolidation marché (Cisco-Splunk) | Faible | Faible | **4** | Positionnement prix et open-source |

---

## 10. Projections Financières

### 10.1. Compte de résultat sur 3 ans

| Poste (en €) | Année 1 | Année 2 | Année 3 |
|---|---|---|---|
| **CHIFFRE D'AFFAIRES** | **84 000** | **338 000** | **881 000** |
| Support & maintenance | 33 600 | 145 000 | 380 000 |
| Audits NIS2 | 30 000 | 105 000 | 280 000 |
| Formations | 12 500 | 50 000 | 125 000 |
| Canal MSP (licences) | 9 600 | 38 400 | 96 000 |
| **CHARGES D'EXPLOITATION** | **70 000** | **240 000** | **580 000** |
| Salaires & charges | 55 000 | 180 000 | 420 000 |
| Infrastructure & outils | 5 000 | 15 000 | 40 000 |
| Marketing & salons | 10 000 | 45 000 | 120 000 |
| **RÉSULTAT D'EXPLOITATION** | **14 000** | **98 000** | **301 000** |
| **MARGE D'EXPLOITATION** | **16,7 %** | **29,0 %** | **34,2 %** |

### 10.2. Hypothèses de croissance

- **Croissance CA An 1 → An 2** : +302 %
- **Croissance CA An 2 → An 3** : +161 %
- **Seuil de rentabilité** : Atteint dès l'Année 1 (marge positive)
- **Point mort quantitatif** : ~300 déploiements avec 3 % de conversion

---

## 11. Besoins de Financement

### 11.1. Plan de financement

| Source | Montant envisagé | Statut |
|---|---|---|
| **Fonds propres** | 20 000 € | À confirmer |
| **France 2030 Cyber PME** | 50 000–100 000 € | Dossier à déposer (M18) |
| **Prêt bancaire** | 30 000 € | Sous réserve de garanties |
| **Business Angels** | 50 000 € | Prospection Phase 2 |
| **TOTAL** | **150 000–200 000 €** | |

### 11.2. Utilisation des fonds

| Poste d'utilisation | Montant | Priorité |
|---|---|---|
| Recrutement équipe (M1–M12) | 80 000 € | Critique |
| Infrastructure & outils | 15 000 € | Moyen |
| Marketing & salons (FIC, Assises) | 25 000 € | Fort |
| Frais juridiques (statuts, CGV) | 10 000 € | Moyen |
| Trésorerie de précaution | 20 000 € | Fort |

---

## 12. Indicateurs de Performance (KPI)

### 12.1. KPI Produit & Technique

| KPI | Cible An 1 | Cible An 2 | Cible An 3 |
|---|---|---|---|
| Déploiements actifs | 500 | 2 000 | 5 000 |
| Stars GitHub | 100 | 500 | 1 500 |
| Forks GitHub | 20 | 100 | 300 |
| Contributeurs actifs | 5 | 20 | 50 |

### 12.2. KPI Commercial & Financier

| KPI | Cible An 1 | Cible An 2 | Cible An 3 |
|---|---|---|---|
| Clients support | 15 | 60 | 150 |
| Missions d'audit | 10 | 35 | 80 |
| Partenaires MSP | 2 | 10 | 20+ |
| Chiffre d'Affaires | 84 k€ | 338 k€ | 881 k€ |
| Marge d'exploitation | 16,7 % | 29,0 % | 34,2 % |

---

## 13. Conclusion & Perspectives

### 13.1. Synthèse

BigBrowser se positionne sur une opportunité de marché unique :

1. **Un marché en forte croissance** : +10 %/an, tiré par NIS2 et la numérisation des PME
2. **Un gap concurrentiel structurel** : aucun outil open-source n'unifie les 8 fonctionnalités dans une interface web
3. **Un timing réglementaire idéal** : NIS2 impose la supervision à 15 000 entités françaises d'ici 2027
4. **Un modèle économique viable** : rentabilité dès l'Année 1, croissance exponentielle

### 13.2. Facteurs clés de succès

- Qualité et fiabilité du produit (zéro faux positif toléré)
- Vitesse d'itération et réactivité aux retours terrain
- Qualité de la documentation et de l'onboarding
- Développement du réseau de partenaires MSP
- Obtention du financement France 2030 Cyber PME

### 13.3. Perspectives post-v1

- **Modules IA/ML** de détection comportementale (v2+)
- **Dashboard conformité NIS2** dédié (v2+)
- **Offre SaaS cloud** hébergée (v2+)
- **Internationalisation** (Belgique, Luxembourg)
- **Certification SecNumCloud**

---

*Business Plan établi en avril 2026 — Sources : Étude de marché, Feuille de cadrage, Business Model, Cahier des charges*
