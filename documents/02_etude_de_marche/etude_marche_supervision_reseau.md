# Étude de Marché — Outil de Supervision et d'Analyse Réseau

> **Contexte, Marché, Concurrence & Opportunités**
>
> *Avril 2026*

---

## Table des matières

1. [Résumé Exécutif](#1-résumé-exécutif)
2. [Contexte du Marché et Facteurs de Croissance](#2-contexte-du-marché-et-facteurs-de-croissance)
   - 2.1 [Une menace cyber en accélération constante](#21-une-menace-cyber-en-accélération-constante)
   - 2.2 [La maturité cyber des PME : un retard structurel](#22-la-maturité-cyber-des-pme--un-retard-structurel)
   - 2.3 [Le cadre réglementaire : NIS2 comme catalyseur de marché](#23-le-cadre-réglementaire--nis2-comme-catalyseur-de-marché)
3. [Taille et Structure du Marché](#3-taille-et-structure-du-marché)
   - 3.1 [Le marché mondial de la cybersécurité](#31-le-marché-mondial-de-la-cybersécurité)
   - 3.2 [Le marché français : un écosystème en forte expansion](#32-le-marché-français--un-écosystème-en-forte-expansion)
   - 3.3 [Le marché spécifique de la supervision réseau](#33-le-marché-spécifique-de-la-supervision-réseau)
4. [Analyse Concurrentielle](#4-analyse-concurrentielle)
   - 4.1 [Cartographie des acteurs](#41-cartographie-des-acteurs)
   - 4.2 [La matrice de positionnement](#42-la-matrice-de-positionnement)
5. [Analyse des Segments Cibles](#5-analyse-des-segments-cibles)
   - 5.1 [Segmentation du marché adressé](#51-segmentation-du-marché-adressé)
   - 5.2 [Focus : les PME, premier marché adressé](#52-focus--les-pme-premier-marché-adressé)
   - 5.3 [Focus : le marché de la formation et de l'enseignement](#53-focus--le-marché-de-la-formation-et-de-lenseignement)
6. [Tendances du Marché et Axes d'Innovation](#6-tendances-du-marché-et-axes-dinnovation)
   - 6.1 [L'IA et le machine learning comme standard](#61-lia-et-le-machine-learning-comme-standard)
   - 6.2 [La convergence des outils : de la fragmentation à l'unification](#62-la-convergence-des-outils--de-la-fragmentation-à-lunification)
   - 6.3 [L'open-source comme modèle dominant pour les PME](#63-lopen-source-comme-modèle-dominant-pour-les-pme)
   - 6.4 [La supervision comme obligation légale (NIS2 et DORA)](#64-la-supervision-comme-obligation-légale-nis2-et-dora)
7. [Analyse SWOT](#7-analyse-swot)
8. [Recommandations Stratégiques](#8-recommandations-stratégiques)
   - 8.1 [Positionnement recommandé](#81-positionnement-recommandé)
   - 8.2 [Fonctionnalités à prioriser pour maximiser la valeur](#82-fonctionnalités-à-prioriser-pour-maximiser-la-valeur)
   - 8.3 [Pistes d'évolution post-v1](#83-pistes-dévolution-post-v1)
9. [Conclusion](#9-conclusion)

---

## 1. Résumé Exécutif

Le secteur de la cybersécurité constitue l'un des marchés les plus dynamiques de l'économie numérique mondiale. En 2025, il représente plus de 250 milliards de dollars à l'échelle mondiale, dont 6,4 milliards d'euros en France. La supervision et l'analyse réseau en sont l'un des segments les plus stratégiques, avec un taux de croissance annuel supérieur à 10 %.

| Indicateur | Valeur |
|---|---|
| Marché mondial cyber (2025) | **>250 Md$** — +12%/an |
| Marché France (2025) | **6,4 Md€** — +10%/an |
| SIEM / SOC France | **441 M€** — +16%/an |
| Supervision réseau mondial | **4,1 Md$** — TCAC 9,5% |

Cette étude s'appuie sur une demande réelle et documentée : les organisations, en particulier les PME et les structures publiques, manquent cruellement d'outils de supervision réseau à la fois accessibles, unifiés et abordables. La directive européenne **NIS2**, entrée en vigueur en octobre 2024, impose désormais à plus de 15 000 entités en France de mettre en place une supervision continue de leurs systèmes d'information.

---

## 2. Contexte du Marché et Facteurs de Croissance

### 2.1 Une menace cyber en accélération constante

L'ampleur de la menace numérique n'a jamais été aussi élevée. Selon le Panorama de la Cybermenace 2024 publié par l'ANSSI, l'agence a traité 4 386 événements de sécurité en 2024, soit une augmentation de 15 % par rapport à 2023. Parmi ces événements, 3 004 signalements et 1 361 incidents confirmés ont été portés à la connaissance de l'agence.

Les attaques par ransomware restent le vecteur le plus fréquent, avec 144 compromissions documentées. Les PME représentent 37 % des victimes.

| Indicateur | Chiffre clé | Source |
|---|---|---|
| Événements sécurité traités en France (2024) | 4 386 (+15%) | ANSSI 2024 |
| Incidents confirmés (2024) | 1 361 | ANSSI 2024 |
| Attaques ransomware documentées (2024) | 144 | ANSSI 2024 |
| PME victimes de cyberattaques (France) | 75 % des attaques | Cybermalveillance 2025 |
| PME fermant après une attaque sérieuse | 60 % en 6 mois | Jedha 2025 |
| Cyberattaques réussies contre PME (2023) | 330 000+ | Diginamic 2025 |
| Perte moyenne d'action après une attaque (grands comptes) | -19,5 % sur 1 an | CSB School 2025 |

### 2.2 La maturité cyber des PME : un retard structurel

Malgré une prise de conscience croissante, le tissu économique français reste très vulnérable. Le baromètre national 2025 de Cybermalveillance.gouv.fr dresse un tableau préoccupant :

- 16 % des entreprises déclarent avoir subi au moins un incident cyber dans les 12 derniers mois
- 3/4 des PME investissent moins de 2 000 euros par an en cybersécurité
- 94 % des grandes entreprises disposent d'une assurance cyber, contre seulement 3,5 % des PME
- 60 % des entreprises françaises sous-investissent en cybersécurité (moins de 1 000 euros/an)
- Seules 40 % des PME ont mis en place des procédures complètes de gestion des incidents
- 6 PME sur 10 ne sauraient pas évaluer les conséquences d'une cyberattaque

**Paradoxe central :** 93 % des dirigeants de PME se disent bien protégés alors que 75 % des cyberattaques en France visent précisément les PME. Ce décalage entre perception et réalité crée un besoin urgent d'outils pédagogiques, accessibles et visualisables.

### 2.3 Le cadre réglementaire : NIS2 comme catalyseur de marché

La directive européenne NIS2 (Network and Information Security 2), entrée en vigueur le 18 octobre 2024, constitue le principal catalyseur réglementaire du marché. Elle élargit considérablement le périmètre de son prédécesseur NIS1 :

- De 7 à 18 secteurs d'activité concernés (énergie, santé, banque, transport, télécoms, administrations publiques, secteur spatial…)
- De moins de 300 entités régulées sous NIS1 à 10 000–15 000 entités en France selon l'ANSSI
- Obligation de supervision continue des systèmes d'information
- Notification obligatoire des incidents significatifs aux autorités (ANSSI)
- Sanctions pouvant aller jusqu'à 2 % du CA annuel mondial pour les entités essentielles, 1,4 % pour les importantes
- Responsabilité personnelle engagée pour les dirigeants en cas de manquement grave

| | NIS1 (2016–2024) | NIS2 (depuis oct. 2024) |
|---|---|---|
| Secteurs | 7 | 18 |
| Entités en France | ~300 | 10 000–15 000 |
| Supervision | Recommandée | **OBLIGATOIRE** |
| Sanctions | Limitées | Jusqu'à 2 % du CA mondial |

---

## 3. Taille et Structure du Marché

### 3.1 Le marché mondial de la cybersécurité

Le marché mondial de la cybersécurité représente plus de 250 milliards de dollars en 2025. Sa croissance est soutenue par trois moteurs structurels :

- L'augmentation exponentielle des cyberattaques, dopées par l'IA générative
- La pression réglementaire accrue (NIS2, DORA, Cyber Resilience Act)
- La transformation numérique des entreprises et l'explosion de l'IoT

Selon Gartner, les dépenses mondiales de cybersécurité ont crû de 13,4 % en 2024 et devraient encore croître de 15,1 % en 2025. Le marché devrait dépasser 350 milliards de dollars d'ici 2029.

### 3.2 Le marché français : un écosystème en forte expansion

En France, le marché de la cybersécurité est l'un des plus dynamiques d'Europe. Il est estimé à 6,4 milliards d'euros en 2025 et devrait atteindre 11,36 milliards d'euros en 2029, selon le cabinet PAC. La part de la cybersécurité dans les dépenses IT est passée de 6 % en 2014 à 11,6 % en 2025.

| Segment | Dépenses 2025 (France) | TCAM |
|---|---|---|
| SOC / SIEM / Gouvernance et conformité | 441 M€ | +16% |
| Sécurité périmétrique (EDR, XDR, MDR) | 790 M€ | +11% |
| Gestion des identités et des accès | 209 M€ | +13,1% |
| Chiffrement | 65 M€ | +13,7% |
| Services managés de cybersécurité (MSSP) | Part majeure des 4,96 Md€ | +14% |

### 3.3 Le marché spécifique de la supervision réseau

Le segment directement adressé par notre solution est le marché des outils de supervision et de monitoring réseau. Les données consolidées de plusieurs cabinets d'étude convergent :

| Périmètre | Valeur 2024–2025 | Projection | TCAC | Source |
|---|---|---|---|---|
| Network Monitoring (strict) | 2,88–4,13 Md$ | 5–9,5 Md$ (2030-34) | 9–11% | Fortune BI / Mordor |
| Network Monitoring & Management | 12,5 Md$ | 25,5 Md$ (2033) | 9,2% | Future Market Report |
| Monitoring Tools (incl. sécurité) | 36,6 Md$ | 185 Md$ (2034) | 17,6% | Precedence Research |
| Logiciels supervision réseau | 8,7 Md$ | 15,5 Md$ (2032) | 7,25% | Future Market Report |
| SIEM global | 4,8 Md$ (2021) | 11,3 Md$ (2026) | 14,5% | Splunk/Mordor |

Le sous-segment des outils de supervision réseau pour PME constitue une opportunité particulièrement intéressante : la demande est forte, l'offre open-source reste fragmentée, et les solutions commerciales sont hors budget pour la majorité des structures de taille intermédiaire.

---

## 4. Analyse Concurrentielle

### 4.1 Cartographie des acteurs

Le paysage concurrentiel se structure en trois grandes catégories : les outils open-source spécialisés, les solutions commerciales enterprise, et un espace intermédiaire peu occupé qui constitue la fenêtre d'opportunité principale.

#### Catégorie 1 : Outils open-source spécialisés

| Outil | Fonction principale | Forces | Limite clé | Licence |
|---|---|---|---|---|
| Nmap | Scan de ports et découverte réseau | Très complet, NSE scripts, référence du secteur | CLI uniquement, pas d'interface web ni d'alertes | GPLv2 |
| Wireshark | Capture et inspection de paquets en profondeur | 759 protocoles, multiplateforme, pédagogique | Interface desktop, pas d'alertes ni de cartographie | GPLv2 |
| Suricata | IDS/IPS haute performance (multi-thread) | DPI, sortie JSON, intégration SIEM, très actif | Pas d'interface unifiée, pas de scan de plages IP | GPLv2 |
| Snort | IDS/IPS basé sur signatures (Cisco) | Communauté énorme, règles personnalisables | Architecture mono-thread, interface limitée | GPLv2 |
| Zeek (ex-Bro) | Analyse comportementale et forensique réseau | Logs structurés, détection d'anomalies, scriptable | Pas d'interface web, configuration complexe | BSD |
| Wazuh | SIEM/HIDS open-source avec interface web | Gratuit, tableaux de bord, alertes, logs | Orienté hôte (HIDS), pas de scan de ports | GPLv2 |
| Nagios | Supervision infrastructure et disponibilité | Stable, plugins nombreux, monitoring de services | Orienté uptime/performance, pas de sécurité avancée | GPLv2 |

#### Catégorie 2 : Solutions commerciales enterprise

| Solution | Éditeur | Positionnement | Tarif approximatif | Accessible PME ? |
|---|---|---|---|---|
| Splunk Enterprise | Cisco (acq. 28 Md$ 2024) | SIEM full-stack, analytique IA | Très élevé (>10k$/an) | Non |
| Microsoft Sentinel | Microsoft | SIEM cloud-natif Azure | Usage-based, élevé | Non |
| Palo Alto Cortex XDR | Palo Alto Networks | XDR + SIEM intégré | Très élevé | Non |
| IBM QRadar | IBM / Palo Alto Networks | SIEM enterprise mature | Enterprise uniquement | Non |
| PRTG Network Monitor | Paessler AG | Supervision performance réseau | Abordable (gratuit jusqu'à 100 capteurs) | Partiel |
| SolarWinds NPM | SolarWinds | Surveillance réseau IT | Moyen-haut de gamme | Partiel |
| Elastic SIEM | Elastic | SIEM basé sur Elasticsearch | Freemium, mais technique | Compétences requises |

### 4.2 La matrice de positionnement

L'analyse concurrentielle révèle une lacune de marché claire : aucun outil ne combine simultanément les huit fonctionnalités clés (détection d'équipements, scan IP, ports ouverts, services réseau, trafic, comportements suspects, alertes, exports JSON/CSV) dans une interface web unifiée, accessible et déployable sur un réseau local sans infrastructure cloud.

| Outil | Découverte | Scan ports | Trafic | Détection | Alertes | Interface web | Export CSV/JSON |
|---|---|---|---|---|---|---|---|
| **Notre solution (cible)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Nmap | ✅ | ✅ | ❌ | ⚠️ | ❌ | ❌ | ⚠️ |
| Wireshark | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ⚠️ |
| Suricata | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ |
| Zeek | ❌ | ❌ | ✅ | ✅ | ⚠️ | ❌ | ✅ |
| Wazuh | ⚠️ | ❌ | ⚠️ | ✅ | ✅ | ✅ | ✅ |
| PRTG | ✅ | ✅ | ⚠️ | ❌ | ✅ | ✅ | ⚠️ |
| Splunk | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

> ✅ Fonctionnalité native — ⚠️ Partielle ou nécessitant une configuration avancée — ❌ Absente

**Conclusion :** Splunk est le seul concurrent à cocher toutes les cases, mais il est inaccessible financièrement et techniquement pour les PME et les organisations à budget contraint. Notre solution occupe un espace vide entre les outils CLI gratuits et les solutions enterprise.

---

## 5. Analyse des Segments Cibles

### 5.1 Segmentation du marché adressé

Notre outil s'adresse à plusieurs segments distincts, chacun avec ses propres besoins et critères de décision :

| Segment | Profil | Besoin spécifique | Disposition à payer | Potentiel |
|---|---|---|---|---|
| PME / ETI | 50–500 employés, DSI inexistante ou limitée | Visibilité réseau simple, alertes en langage clair, conformité NIS2 | Faible (<2000€/an) | Très fort |
| Secteur public (collectivités, hôpitaux) | Entités NIS2 "importantes", budget contraint | Conformité réglementaire, rapports pour auditeurs | Moyen (budget public) | Fort |
| Formation / Éducation | Écoles d'ingénieurs, BTS, IUT, formations cyber | Outil opérationnel pour TP et démonstrations | Faible (gratuit) | Fort (volume) |
| MSP / SSII | Prestataires IT gérant des PME | Outil de diagnostic réseau pour audits clients | Moyen | Fort |
| Admins réseau indépendants | Consultants, freelances cyber | Toolbox complète, exportable pour rapports clients | Moyen | Moyen |
| Grands comptes (PoC) | DSI de grands groupes | Complément de leur SIEM, test avant déploiement | Élevé | Faible (concurrence forte) |

### 5.2 Focus : les PME, premier marché adressé

Les PME françaises représentent la cible prioritaire et la plus urgente. Leur profil cyber est préoccupant :

- 75 % des cyberattaques en France ciblent les TPE et PME
- 60 % des PME victimes d'une attaque sérieuse ferment dans les 6 mois suivants
- Seules 3,5 % des PME disposent d'une assurance cyber
- 3/4 des PME investissent moins de 2 000 euros par an en cybersécurité
- 57 % expriment un besoin d'outils de protection, 1 sur 4 n'a recours à aucun acteur spécialisé
- La principale barrière est le coût et la complexité des outils existants

**Opportunité directe :** un outil open-source avec interface web intuitive, sans prérequis de configuration avancé, répondant aux obligations NIS2 avec des rapports exportables, cible exactement ce que 57 % des PME expriment comme besoin prioritaire.

### 5.3 Focus : le marché de la formation et de l'enseignement

Le marché de la formation en cybersécurité est en pleine expansion. En France, l'OPIIEC recense plus de 900 formations en cybersécurité. Le secteur compte environ 45 000 professionnels en 2023 et en nécessitera au moins 70 000 d'ici 2028. Les offres d'emploi en cybersécurité représentent 3 % des postes Tech en France.

Dans ce contexte, un outil opérationnel combinant scan réseau, détection d'intrusion et reporting dans une interface web lisible présente une forte valeur ajoutée pour les établissements de formation. Il permet aux apprenants de travailler sur un outil proche du réel, sans la complexité de configuration de Suricata ou la technicité de Zeek.

---

## 6. Tendances du Marché et Axes d'Innovation

### 6.1 L'IA et le machine learning comme standard

La grande tendance du marché en 2024–2025 est l'intégration de l'intelligence artificielle dans les outils de supervision. Les acteurs leaders (Cisco/Splunk, CrowdStrike, Microsoft) investissent massivement dans :

- La détection d'anomalies par modèles d'apprentissage automatique
- Le scoring comportemental des équipements et utilisateurs (UEBA)
- L'automatisation de la réponse aux incidents (SOAR)
- La corrélation automatique des événements et la réduction du bruit d'alertes

Les fabricants adoptant le SIEM activé par IA réduisent le temps d'investigation manuelle de 60 %, selon Mordor Intelligence. Une détection par règles simples (scores de risque, seuils d'alertes) constitue une base solide pour une v1, avec une intégration de modules de détection comportementale envisageable comme évolution future.

### 6.2 La convergence des outils : de la fragmentation à l'unification

Le marché évolue d'un paysage d'outils spécialisés (un outil par fonction) vers des plateformes unifiées. Cette tendance est documentée par les grandes acquisitions de 2024 (Cisco-Splunk, Palo Alto-QRadar) et reflète une "fatigue des outils" chez les équipes de sécurité.

La demande pour des solutions qui unifient SIEM + supervision réseau + scan + alertes + reporting est forte, en particulier chez les PME qui n'ont ni le temps ni les ressources de déployer et maintenir plusieurs outils distincts. Notre approche de plateforme intégrée est donc parfaitement alignée sur cette tendance de fond.

### 6.3 L'open-source comme modèle dominant pour les PME

La croissance des solutions open-source (Wazuh, Suricata, Zeek) démontre que le marché accepte et valorise les alternatives gratuites. Les PME et les structures publiques avec des budgets contraints se tournent de plus en plus vers l'open-source, à condition que :

- L'interface soit accessible (web, non-CLI)
- La documentation soit claire et la configuration guidée
- Les sorties soient standardisées (JSON, CSV) pour intégration dans des rapports d'audit

Notre stack technique (Python + FastAPI + HTML/CSS/JS) correspond exactement à ce modèle : déployable sur n'importe quelle machine, sans dépendance cloud, avec une interface web moderne.

### 6.4 La supervision comme obligation légale (NIS2 et DORA)

NIS2 impose explicitement la "supervision de sécurité des systèmes d'information" pour les entités essentielles. DORA (Digital Operational Resilience Act, entrée en vigueur en janvier 2025) ajoute des obligations similaires pour le secteur financier. Ces deux directives créent un marché captif de 15 000+ entités en France qui doivent se doter d'outils de supervision d'ici 2027.

La capacité de notre outil à générer des rapports exportables en JSON et CSV répond directement aux besoins de documentation et d'audit que NIS2 impose.

---

## 7. Analyse SWOT

| 💪 **FORCES** | ⚠️ **FAIBLESSES** |
|---|---|
| Solution unifiée : 8 fonctionnalités dans une seule interface | Absence de support commercial et de SLA |
| Stack technique moderne et éprouvé (Python/FastAPI/REST) | Scalabilité à valider sur de grands réseaux |
| Open-source : accessible sans licence commerciale | Maintenance dépendante de l'équipe fondatrice |
| Alignement direct avec les exigences NIS2 | Pas de détection avancée par IA/ML (v1) |
| Interface web : accessible sans expertise CLI | Absence de certification de sécurité (ex. SecNumCloud) |
| Exportation JSON/CSV : intégration facile dans les workflows d'audit | |

| 🚀 **OPPORTUNITÉS** | 🔴 **MENACES** |
|---|---|
| NIS2 : 15 000 entités en France à conformer d'ici 2027 | Concurrence des outils open-source bien établis (Wazuh, Suricata) |
| Marché supervision réseau : 4 Md$ en croissance à +10%/an | Évolution rapide des menaces (IA offensive, nouveaux protocoles) |
| Gap concurrentiel clair entre outils CLI et solutions enterprise | Complexité croissante des réseaux (IoT, cloud hybride) |
| Demande forte des PME pour des outils accessibles et abordables | Risque de faux positifs nuisant à la crédibilité |
| Expansion possible vers une offre SaaS, MSSP ou cloud | Consolidation du marché (Cisco-Splunk) augmentant la puissance des acteurs dominants |
| Programme France 2030 Cyber PME : 100 M€ d'enveloppe | Retard de transposition de NIS2 en France ralentissant la demande |

---

## 8. Recommandations Stratégiques

### 8.1 Positionnement recommandé

Sur la base de l'analyse de marché, le positionnement optimal de la solution est le suivant :

| Axe | Détail |
|---|---|
| **Cible principale** | PME (10–250 employés), structures éducatives, prestataires IT gérant des PME |
| **Différenciateur clé** | Outil tout-en-un avec interface web simple, sans configuration complexe, conforme NIS2 |
| **Proposition de valeur** | Visibilité réseau complète, alertes en temps réel, rapports exportables : *Splunk pour les PME, sans le prix de Splunk* |
| **Compétiteurs directs** | Aucun sur le périmètre exact (gap de marché confirmé) |

### 8.2 Fonctionnalités à prioriser pour maximiser la valeur

| Priorité | Fonctionnalité | Justification marché |
|---|---|---|
| **P1 – Critique** | Interface web unifiée avec tableau de bord temps réel | Principale barrière à l'adoption des outils CLI actuels |
| **P1 – Critique** | Scan de plages IP et découverte d'équipements | Fonctionnalité #1 attendue pour inventaire NIS2 |
| **P1 – Critique** | Détection de ports ouverts et services | Base de toute supervision réseau, exigence NIS2 |
| **P2 – Important** | Capture et analyse du trafic réseau | Différenciateur vs outils de scan seuls |
| **P2 – Important** | Système d'alertes configurables | Demande prioritaire des PME et SOC |
| **P2 – Important** | Export JSON et CSV des rapports | Exigence explicite NIS2 pour documentation d'audit |
| **P3 – Valeur ajoutée** | Détection de comportements suspects (règles) | Transforme l'outil en IDS léger, fort différenciateur |
| **P3 – Valeur ajoutée** | Cartographie visuelle du réseau | Forte valeur pour la présentation et les audits |

### 8.3 Pistes d'évolution post-v1

- Intégration avec Suricata pour la détection d'intrusion avancée via son API JSON
- Module d'export vers des formats SIEM standard (CEF, LEEF) pour intégration dans les écosystèmes existants
- Tableau de bord conformité NIS2 avec indicateurs de maturité (piliers Gouvernance / Protection / Défense / Résilience du ReCyF ANSSI)
- Scoring de risque par équipement basé sur les ports ouverts, services exposés et historique des alertes
- API REST documentée pour intégration avec d'autres outils ou dashboards

> 📝 **Note :** Un PESTEL est à ajouter dans cette section.

---

## 9. Conclusion

Cette étude de marché confirme que la solution de supervision et d'analyse réseau que nous développons s'inscrit dans une fenêtre d'opportunité unique et bien documentée. Trois convergences la placent en position favorable :

**Un marché en forte croissance.**
Le segment supervision réseau croît à +10%/an, tiré par NIS2, la numérisation des PME et l'explosion des cybermenaces. Plus de 4 000 incidents ont été traités par l'ANSSI en 2024, en hausse de 15 %.

**Un gap concurrentiel clair.**
Aucun outil open-source n'unifie aujourd'hui, dans une interface web accessible, les 8 fonctionnalités requises. La solution la plus complète (Splunk) est hors de portée des PME et des établissements à budget contraint.

**Un timing réglementaire idéal.**
NIS2 impose à 15 000 entités françaises de se conformer d'ici 2027, avec supervision réseau obligatoire. Le programme France 2030 Cyber PME alloue 100 millions d'euros pour accélérer cette mise en conformité.

Notre solution répond à un besoin réel, mesurable, documenté, et urgent. Elle se positionne au cœur d'un des secteurs les plus stratégiques de l'économie numérique, avec une compréhension fine des enjeux opérationnels et réglementaires actuels de la cybersécurité.

---

*Étude réalisée en avril 2026 — Sources : ANSSI, Mordor Intelligence, PAC, Cybermalveillance.gouv.fr, Jedha, Xerfi, Numeum, Fortune Business Insights, Precedence Research*
