# Références — Étude de marché

## Table des matières

- [Section 1 : Cadrage de l'étude](#section-1--cadrage-de-létude-de-marché-bigbrowser)
- [Section 2 : Analyse de la demande et contexte macro](#section-2--analyse-de-la-demande-et-contexte-macro)
- [Section 3 : Segmentation, ciblage et positionnement (STP)](#section-3--segmentation-ciblage-et-positionnement-stp)
- [Section 4 : Benchmark concurrentiel](#section-4--benchmark-concurrentiel)
- [Section 5 : Modèle TAM / SAM / SOM](#section-5--modèle-tam--sam--som)
- [Section 6 : Stratégie d'entrée sur le marché (GTM)](#section-6--stratégie-dentrée-sur-le-marché-gtm)
- [Section 7 : Risques, KPI et preuves](#section-7--risques-kpi-et-preuves)
- [Section 8 : Sources de référence](#section-8--sources-de-référence)

---

## Section 1 : Cadrage de l'étude de marché BigBrowser

### 1. Objet du document

Ce document pose le cadre méthodologique et le périmètre de l'étude de marché du projet BigBrowser. Il explicite les outils d'analyse utilisés, les sources mobilisées et les limites de l'étude.

### 2. Périmètre de l'étude

| Dimension | Périmètre |
|---|---|
| Produit | BigBrowser — outil open-source de supervision et d'analyse réseau |
| Marché géographique | France métropolitaine (prioritaire), Belgique, Suisse (secondaire) |
| Cible principale | PME françaises de 10 à 250 employés |
| Secteur | Cybersécurité — Supervision réseau et conformité NIS2 |
| Horizon temporel | 2026–2029 (3 ans) |

### 3. Méthodes utilisées

#### 3.1 Analyse PESTEL

Cadre d'analyse macro-environnementale permettant d'identifier les facteurs externes influençant le marché :

| Facteur | Application à BigBrowser |
|---|---|
| **P**olitique | Directive NIS2 (2022/2555), transposition France 2027, France 2030 Cyber PME (100 M€) |
| **É**conomique | Marché cyber mondial à 250 G$, croissance +10 %/an, gap d'investissement PME |
| **S**ociologique | Prise de conscience cyber post-attacks, pression assureurs et donneurs d'ordre |
| **T**echnologique | Essor de l'open-source, maturité de Python/FastAPI, adoption edge computing |
| **E**nvironnemental | Impact faible (solution logicielle on-premise), green IT non prioritaire en v1 |
| **L**égal | Conformité RGPD obligatoire, NIS2 directive européenne, licence open-source (GPLv2/APACHE2) |

#### 3.2 Analyse SWOT

Cadre d'analyse stratégique croisant forces/faiblesses internes et opportunités/menaces externes.

#### 3.3 Modèle TAM / SAM / SOM

Méthode de dimensionnement de marché en trois couches :

- **TAM** (Total Addressable Market) : Marché total adressable — cyber sécurité mondiale
- **SAM** (Serviceable Addressable Market) : Marché adressable — PME France/Belgique/Suisse
- **SOM** (Serviceable Obtainable Market) : Marché atteignable — objectif réaliste 24–36 mois

#### 3.4 STP (Segmentation, Targeting, Positioning)

Méthode marketing :

1. **Segmentation** : découpage du marché en segments homogènes
2. **Ciblage** (Targeting) : sélection des segments prioritaires
3. **Positionnement** : proposition de valeur différenciante

#### 3.5 Benchmark concurrentiel

Analyse comparative des solutions existantes selon 3 catégories :

- Outils open-source spécialisés (Nmap, Wireshark, Suricata, Snort, Zeek, Wazuh, Security Onion)
- Solutions enterprise (Splunk, Microsoft Sentinel, IBM QRadar, Palo Alto Networks)
- Solutions de supervision IT généralistes (PRTG, SolarWinds)

### 4. Limites de l'étude

| Limite | Impact |
|---|---|
| Données de marché principalement secondaires | Les projections reposent sur des synthèses publiques (Mordor Intelligence, Gartner, PAC) |
| Périmètre géographique restreint | L'extrapolation à d'autres pays européens nécessiterait une étude complémentaire |
| Horizon 3 ans | Les marchés cyber évoluent rapidement ; les projections au-delà de 2029 sont spéculatives |
| Absence de données primaires (sondages PME) | Les besoins réels des PME sont estimés via des retours d'expérience publics et des rapports ANSSI |

### 5. Références projet

| Document source | Lien |
|---|---|
| Feuille de cadrage projet (KICKOFF.md) | [Voir document](../../01_documents_pedagogiques/README.md) |
| Syllabus / Cahier des charges | [Voir document](../../06_cahier_des_charges/rendu_principal.md) |
| Architecture technique | [Voir document](../../08_architecture/rendu_principal.md) |
| Business model | [Voir document](../../03_business_model/rendu_principal.md) |
| Business plan | [Voir document](../../04_business_plan/rendu_principal.md) |
| Registre des sources transverse | [Voir document](../../90_references_transverses/README.md) |

### 6. Glossaire des abréviations

| Abréviation | Signification |
|---|---|
| PESTEL | Politique, Économique, Sociologique, Technologique, Environnemental, Légal |
| SWOT | Strengths, Weaknesses, Opportunities, Threats |
| TAM | Total Addressable Market |
| SAM | Serviceable Addressable Market |
| SOM | Serviceable Obtainable Market |
| STP | Segmentation, Targeting, Positioning |
| GTM | Go-To-Market |
| NIS2 | Network and Information Security 2 (directive européenne 2022/2555) |
| PME | Petites et Moyennes Entreprises |
| MSP | Managed Service Provider |
| SSII | Société de Services en Ingénierie Informatique |

---

## Section 2 : Analyse de la demande et contexte macro

### 1. Contexte global de la cybersécurité

Le marché mondial de la cybersécurité atteint **250 milliards de dollars** en 2025, avec une croissance annuelle soutenue de **+10 %**, portée par l'augmentation des menaces, la pression réglementaire et la transformation numérique des organisations.

En France, le marché représente **6,4 milliards d'euros**, dont une part croissante est liée à la mise en conformité avec la directive européenne NIS2.

### 2. Le marché français de la cybersécurité

| Indicateur | Valeur | Source |
|---|---|---|
| Marché cyber mondial 2025 | 250 G$ | [Mordor Intelligence](https://www.mordorintelligence.com/) |
| Marché cyber France | 6,4 G€ | PAC / [OPIIEC](https://www.opiiec.fr/) |
| Croissance annuelle | +10 % | [Gartner](https://www.gartner.com/) |
| Cyber Threat Score France (Mai 2026) | 1114.8 | [Cybermalveillance.gouv.fr](https://www.cybermalveillance.gouv.fr/) |
| Cas de ransomware documentés (2024-2025) | 317 | [ANSSI](https://cyber.gouv.fr/actualites/panorama-de-la-cybermenace-2025/) |
| Entités françaises concernées par NIS2 | ~15 000 | ANSSI |
| Taux de défaillance PME post-attaque | 60 % (fermeture sous 6 mois) | Cybermalveillance / CSA |

### 3. La menace cyber en France

#### 3.1 Chiffres clés ANSSI

- **317 cas de ransomware** documentés sur la période 2024-2025
- **75 % des cyberattaques** ciblent les PME et TPE
- Une PME sur deux déclare avoir subi au moins une tentative d'attaque dans l'année
- Le coût moyen d'une attaque pour une PME est estimé entre 20 000 € et 150 000 €

#### 3.2 Score de menace Cybermalveillance.gouv.fr

Le Cyber Threat Score de la plateforme [Cybermalveillance.gouv.fr](https://www.cybermalveillance.gouv.fr/) s'établit à **1 114,8** en mai 2026, confirmant un niveau de menace élevé et persistant. Les catégories d'incidents les plus fréquentes sont :

1. Hameçonnage (phishing)
2. Ransomware
3. Scan de ports et tentatives d'intrusion
4. Fuite de données
5. Usurpation d'identité

#### 3.3 Conséquences pour les PME

- **60 % des PME** victimes d'une cyberattaque déposent le bilan dans les 6 mois (source : Cybermalveillance.gouv.fr / CSA Research)
- **60 % des PME** investissent moins de 1 000 € par an dans leur cybersécurité
- Seulement **25 % des PME** disposent d'un outils de supervision réseau dédié

### 4. L'impact de la directive NIS2

#### 4.1 Calendrier réglementaire

| Date | Étape |
|---|---|
| Décembre 2022 | Adoption de la directive NIS2 (2022/2555) |
| Octobre 2024 | Date limite de transposition dans les droits nationaux |
| 2024-2025 | Transposition en France via la loi NIS2 |
| **2027** | **Date d'entrée en vigueur effective des obligations** |

#### 4.2 Entités concernées

La directive NIS2 étend considérablement le périmètre des entités soumises à des obligations de cybersécurité :

- **~15 000 entités françaises** concernées (contre ~300 pour NIS1)
- Secteurs critiques : énergie, transports, santé, eau, numérique, banque, infrastructures
- Secteurs importants : services postaux, gestion des déchets, chimie, agroalimentaire, fabrication

#### 4.3 Obligations applicables

Les entités NIS2 doivent notamment :

- Mettre en œuvre des mesures de **supervision réseau** (obligation de détection)
- Assurer la **traçabilité des incidents**
- Déclarer les incidents significatifs sous **24h** (early warning) et **72h** (notification complète)
- Désigner un **Responsable de la Sécurité des Systèmes d'Information** (RSSI)
- Justifier de leur conformité via des **rapports et exports de preuves**

#### 4.4 Sanctions

- Amende jusqu'à **10 M€ ou 2 % du chiffre d'affaires annuel mondial** (entités essentielles)
- Amende jusqu'à **7 M€ ou 1,4 % du CA** (entités importantes)
- Suspension des activités en cas de non-conformité grave

### 5. Synthèse : le besoin non couvert

| Constat | Implication pour BigBrowser |
|---|---|
| NIS2 impose une supervision réseau à 15 000 entités | Marché captif en croissance |
| 60 % des PME investissent < 1 000 €/an en cyber | Besoin d'une solution abordable, voire gratuite |
| Aucun outil open-source ne couvre les 8 fonctions clés en interface web unifiée | Gap concurrentiel exploitable |
| 75 % des attaques ciblent les PME | Urgence du besoin |
| 60 % des PME fermeture post-attaque | Enjeu de survie économique |

### 6. Sources

- [ANSSI — Rapport d'activité 2024 et Panorama de la menace 2025](https://cyber.gouv.fr/actualites/panorama-de-la-cybermenace-2025/)
- [Cybermalveillance.gouv.fr — Baromètre et Cyber Threat Score](https://www.cybermalveillance.gouv.fr/)
- [Mordor Intelligence — Cybersecurity Market Report 2025](https://www.mordorintelligence.com/)
- [Directive européenne NIS2 (2022/2555)](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive)
- [PAC / OPIIEC — Chiffres du marché cyber France 2025](https://www.opiiec.fr/)
- [Gartner — Forecast Analysis: Security and Risk Management, 2025](https://www.gartner.com/)

---

## Section 3 : Segmentation, ciblage et positionnement (STP)

### 1. Segmentation du marché

L'étude identifie **6 segments clients** distincts pour BigBrowser :

| # | Segment | Taille estimée | Priorité |
|---|---|---|---|
| 1 | PME/ETI françaises (10-250 employés) | ~150 000 entités | **P1 — Prioritaire** |
| 2 | MSP / SSII revendeurs | ~2 000 structures | P2 |
| 3 | Collectivités territoriales et hôpitaux | ~25 000 entités | P2 |
| 4 | Établissements d'enseignement et de formation | ~10 000 entités | P3 |
| 5 | Grands groupes (250+ employés) | ~5 000 entités | V2 |
| 6 | Particuliers / micro-entreprises | >1 M | Hors périmètre |

#### 1.1 Critères de segmentation

Les segments sont définis selon 4 critères :

- **Taille d'organisation** : nombre d'employés, budget IT
- **Besoins de conformité** : soumission NIS2, obligations réglementaires
- **Capacité d'investissement** : budget cybersécurité annuel
- **Maturité cyber** : existence ou non d'un outil de supervision

### 2. Ciblage (Targeting)

#### 2.1 Segment prioritaire : PME/ETI françaises

**Pourquoi ce segment ?**

- ~15 000 entités françaises soumises à NIS2 incluent massivement des PME/ETI
- 60 % des PME investissent moins de 1 000 €/an en cybersécurité → besoin d'une solution gratuite ou très abordable
- 75 % des cyberattaques ciblent les PME → urgence du besoin
- Faible maturité cyber : peu d'outils déployés, absence de supervision réseau
- Décideur accessible : DSI ou dirigeant, sans expertise CLI

**Profil type du client prioritaire :**

| Critère | Profil |
|---|---|
| Secteur | Industrie, services, santé, commerce |
| Taille | 25-150 employés |
| Budget cyber annuel | < 5 000 € |
| Contrainte principale | Conformité NIS2 |
| Équipement existant | Antivirus, firewall, parfois aucun outil de supervision |
| Frein | Prix des solutions enterprise, complexité des outils open-source existants |

#### 2.2 Segment secondaire : MSP/SSII

**Pourquoi ce segment ?**

- Effet de levier : un MSP équipé peut déployer BigBrowser chez 10-50 clients PME
- Canal de distribution indirect aligné avec le business model open-core
- Besoin d'un outil multi-tenant pour superviser plusieurs clients

#### 2.3 Segment secondaire : Collectivités et hôpitaux

- Budgets publics souvent contraints
- Obligations NIS2 fortes (secteurs critiques)
- Besoin de reporting et exports pour justifier la conformité

### 3. Positionnement

#### 3.1 Proposition de valeur

**BigBrowser : une supervision réseau complète et gratuite, pensée pour les PME soumises à NIS2.**

Formule de positionnement :

> « Le Splunk des PME, sans le prix Splunk. »

#### 3.2 Différenciation

| Critère | Concurrents open-source | Concurrents enterprise | BigBrowser |
|---|---|---|---|
| Prix | Gratuit (outil individuel) | 15 000 - 50 000 €/an | **Gratuit (open-source)** |
| Interface web unifiée | Non (outils CLI ou interfaces séparées) | Oui | **Oui** |
| Chaîne fonctionnelle complète (scan → détection → alerte → export) | Non (spécialisés sur une fonction) | Oui | **Oui** |
| Simplicité de déploiement | Variable (nécessite expertise) | Assisté | **Docker Compose simple** |
| Conformité NIS2 (exports preuve) | Non documenté | Oui | **Oui (natif)** |
| Communauté open-source | Oui | Non | **Oui** |
| Support commercial | Non | Oui | **Optionnel (payant)** |

#### 3.3 « BigBrowser » : explication du nom

Le nom évoque la capacité à **voir grand (Big)** et à **naviguer (Browser)** dans son réseau. Il suggère :

- La visibilité : « voir tout ce qui se passe sur le réseau »
- La simplicité : « naviguer comme sur le web »
- L'accessibilité : « pas besoin d'être un expert pour comprendre »

#### 3.4 Slogans et messages clés

| Message | Cible |
|---|---|
| « Votre réseau vu à 360°, gratuitement. » | PME |
| « La supervision réseau open-source qui tient dans un Docker Compose. » | DSI techniques |
| « Conformité NIS2 sans vous ruiner. » | Dirigeants |
| « Déployez, supervisez, prouvez. » | Messages produit |

### 4. Carte de positionnement concurrentiel

```
Prix élevé
    ^
    | Splunk, Sentinel, QRadar (enterprise)
    |
    |           Wazuh, Security Onion (open-source avancé)
    |
    |   Nagios, PRTG (supervision IT généraliste)
    |
    |   *** BigBrowser ***
    |
    |   Nmap, Wireshark, Snort (outils spécialisés)
    |
    +-----------------------------------------> Complétude fonctionnelle
    Faible                                  Élevée
```

BigBrowser se positionne dans le quadrant **bas prix / haute complétude fonctionnelle**, un espace actuellement non occupé par les solutions existantes.

---

## Section 4 : Benchmark concurrentiel

### 1. Périmètre du benchmark

Ce benchmark compare les solutions existantes par rapport aux 8 fonctions clés que BigBrowser doit couvrir :

1. Scan réseau et découverte d'actifs
2. Détection de ports ouverts et services
3. Capture et analyse du trafic réseau
4. Détection de comportements suspects (règles)
5. Système d'alertes actionnables
6. Interface web unifiée
7. Exports CSV/JSON (preuve NIS2)
8. Audit et traçabilité

### 2. Catégorie 1 : Outils open-source spécialisés

#### 2.1 Nmap

| Critère | Évaluation |
|---|---|
| Type | Scanner réseau |
| Fonctions couvertes | Scan réseau, détection ports/services |
| Interface web | Non (CLI uniquement) |
| Alertes | Non |
| Exports | Sortie XML/Nmap |
| Licence | GPLv2 |
| Prix | Gratuit |
| Positionnement | Outil complémentaire (back-end de scan possible) |

#### 2.2 Wireshark / TShark

| Critère | Évaluation |
|---|---|
| Type | Analyseur de paquets |
| Fonctions couvertes | Capture et analyse trafic |
| Interface web | Non (GUI desktop ou CLI) |
| Alertes | Non |
| Exports | PCAP, CSV |
| Licence | GPLv2 |
| Prix | Gratuit |
| Positionnement | Outil de diagnostic, pas de supervision continue |

#### 2.3 Suricata

| Critère | Évaluation |
|---|---|
| Type | IDS/IPS moteur de détection |
| Fonctions couvertes | Détection (règles), capture trafic |
| Interface web | Non (nécessite Elastic Stack ou EveBox) |
| Alertes | Oui (fichiers eve.json) |
| Exports | JSON, EVE |
| Licence | GPLv2 |
| Prix | Gratuit |
| Positionnement | Excellent moteur de détection, pas de UI native |

#### 2.4 Snort

| Critère | Évaluation |
|---|---|
| Type | IDS/IPS |
| Fonctions couvertes | Détection (règles) |
| Interface web | Non (CLI + Barnyard pour sortie) |
| Alertes | Oui (via syslog/unixsock) |
| Exports | Syslog, Unified2 |
| Licence | GPLv2 |
| Prix | Gratuit |
| Positionnement | Référence IDS historique, nécessite des outils complémentaires |

#### 2.5 Zeek (anciennement Bro)

| Critère | Évaluation |
|---|---|
| Type | Analyseur de trafic réseau |
| Fonctions couvertes | Capture trafic, analyse protocoles |
| Interface web | Non (logs + Elastic/Kafka) |
| Alertes | Via scripts (Zeek policies) |
| Exports | Logs format Zeek |
| Licence | BSD |
| Prix | Gratuit |
| Positionnement | Analyse de trafic avancée, courbe d'apprentissage raide |

#### 2.6 Wazuh

| Critère | Évaluation |
|---|---|
| Type | SIEM open-source (fork OSSEC) |
| Fonctions couvertes | Détection, alertes, audit (agent-based) |
| Interface web | Oui (Kibana) |
| Alertes | Oui |
| Exports | Oui |
| Licence | GPLv2 |
| Prix | Gratuit (support payant) |
| Positionnement | Concurrent direct partiel (SIEM, pas supervision réseau native) |

#### 2.7 Security Onion

| Critère | Évaluation |
|---|---|
| Type | Distribution Linux complète de sécurité réseau |
| Fonctions couvertes | Toutes (via combinaison d'outils) |
| Interface web | Oui (Squert, CyberChef, Elastic) |
| Alertes | Oui |
| Exports | Oui |
| Licence | GPLv2 (bundled) |
| Prix | Gratuit |
| Positionnement | Solution open-source la plus complète, mais complexe à déployer (OS dédié) |

### 3. Catégorie 2 : Solutions Enterprise

#### 3.1 Splunk

| Critère | Évaluation |
|---|---|
| Type | SIEM / Plateforme de données |
| Interface web | Oui |
| Alertes | Oui |
| Prix | ~20 000 €/an (licence minimum) |
| Positionnement | Marché enterprise, trop cher pour PME |

#### 3.2 Microsoft Sentinel

| Critère | Évaluation |
|---|---|
| Type | SIEM cloud (SaaS) |
| Interface web | Oui (Azure Portal) |
| Alertes | Oui |
| Prix | ~2-5 $/GB ingéré/déclenché |
| Positionnement | Concurrence indirecte (SaaS, dépendance Azure) |

#### 3.3 IBM QRadar

| Critère | Évaluation |
|---|---|
| Type | SIEM |
| Interface web | Oui |
| Alertes | Oui |
| Prix | ~30 000 €/an (licence + maintenance) |
| Positionnement | Enterprise, complexe, coût élevé |

#### 3.4 Palo Alto Networks (Cortex XSIAM)

| Critère | Évaluation |
|---|---|
| Type | XDR / SIEM nouvelle génération |
| Interface web | Oui |
| Alertes | Oui |
| Prix | > 50 000 €/an |
| Positionnement | Haut de gamme, inaccessible pour PME |

### 4. Catégorie 3 : Solutions supervision IT généralistes

#### 4.1 PRTG Network Monitor

| Critère | Évaluation |
|---|---|
| Type | Supervision IT (SNMP, trafic, bande passante) |
| Interface web | Oui |
| Alertes | Oui |
| Prix | Freemium (100 capteurs gratuits, puis payant) |
| Positionnement | Supervision IT, pas de détection de menaces cyber |

#### 4.2 SolarWinds

| Critère | Évaluation |
|---|---|
| Type | Supervision IT et réseau |
| Interface web | Oui |
| Alertes | Oui |
| Prix | À partir de 3 000 €/an |
| Positionnement | Supervision IT, fonctionnalités cyber limitées |

### 5. Analyse du gap concurrentiel

#### 5.1 Matrice de couverture fonctionnelle

| Fonction | Nmap | Wire. | Suricata | Snort | Zeek | Wazuh | Sec. Onion | Splunk | Sentinel | Nagios | PRTG | **BigBrowser** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Scan réseau | **Oui** | Non | Non | Non | Non | Non | Oui | Non | Non | Oui | Oui | **Oui** |
| Détection ports/services | **Oui** | Non | Non | Non | Non | Non | Oui | Non | Non | Oui | Oui | **Oui** |
| Capture trafic | Non | **Oui** | **Oui** | Non | **Oui** | Non | **Oui** | Non | Non | Non | Non | **Oui** |
| Détection menaces | Non | Non | **Oui** | **Oui** | **Oui** | **Oui** | **Oui** | **Oui** | **Oui** | Non | Non | **Oui** |
| Alertes | Non | Non | **Oui** | **Oui** | Oui | **Oui** | **Oui** | **Oui** | **Oui** | **Oui** | **Oui** | **Oui** |
| Interface web unifiée | Non | Non | Non | Non | Non | Oui | Oui | **Oui** | **Oui** | **Oui** | **Oui** | **Oui** |
| Exports NIS2 prêts | Non | Non | Non | Non | Non | Non | Non | Oui | Oui | Non | Non | **Oui** |
| Gratuit | **Oui** | **Oui** | **Oui** | **Oui** | **Oui** | **Oui** | **Oui** | Non | Non | Oui | Oui | **Oui** |

#### 5.2 Le gap identifié

**Aucun outil open-source existant ne combine l'ensemble des 8 fonctions clés dans une interface web unifiée, prête à l'emploi et documentée pour la conformité NIS2.**

Les solutions open-source existantes sont :

- **Spécialisées** : chaque outil excelle dans un domaine (scan, capture, détection)
- **Non intégrées** : leur combinaison nécessite une ingénierie système (Elastic Stack, Kafka, scripts)
- **Sans UI unifiée** : l'administrateur doit jongler entre plusieurs interfaces
- **Non orientées conformité** : les exports de preuve ne sont pas natifs

Les solutions enterprise couvrent toutes les fonctions mais sont inaccessibles financièrement pour les PME.

BigBrowser occupe un **espace concurrentiel vide** : le « Splunk des PME, sans le prix Splunk ».

### 6. Synthèse des menaces concurrentielles

| Concurrent | Type de menace | Réponse BigBrowser |
|---|---|---|
| Wazuh | Menace directe (SIEM open-source) | Différenciation : supervision réseau native vs SIEM |
| Security Onion | Menace directe (solution complète) | Différenciation : déploiement Docker simple vs OS dédié |
| Solutions enterprise | Menace indirecte (trop chères) | Avantage prix décisif |
| Solutions IT (PRTG, Nagios) | Menace indirecte (pas de sécurité) | Positionnement cybersécurité NIS2 |
| Développement d'alternatives open-source | Menace future | Avance par l'UX et la documentation NIS2 |

---

## Section 5 : Modèle TAM / SAM / SOM

### 1. Méthode de calcul

Le dimensionnement du marché suit une approche **top-down** pour le TAM et le SAM, et **bottom-up** pour le SOM, conformément aux bonnes pratiques d'analyse de marché pour les solutions B2B open-source.

### 2. TAM — Total Addressable Market

#### 2.1 Définition

Marché total adressable : la totalité des dépenses mondiales en cybersécurité.

#### 2.2 Calcul

| Composant | Valeur | Source |
|---|---|---|
| Marché mondial de la cybersécurité 2025 | 250 G$ | [Mordor Intelligence](https://www.mordorintelligence.com/) |
| Croissance annuelle | +10 % | [Gartner](https://www.gartner.com/) |
| TAM estimé 2026 | 275 G$ | Projection |
| TAM estimé 2027 | 302 G$ | Projection |
| TAM estimé 2029 | 366 G$ | Projection |

**TAM retenu (2026) : 275 G$ (≈ 250 G€)**

*Note : le TAM est donné à titre indicatif. Le marché réellement adressable est le SAM.*

### 3. SAM — Serviceable Addressable Market

#### 3.1 Définition

Marché adressable : dépenses en cybersécurité des PME françaises + Belgique et Suisse, avec un focus sur la supervision réseau et la conformité NIS2.

#### 3.2 Calcul France

| Composant | Valeur | Calcul |
|---|---|---|
| Marché cyber France 2025 | 6,4 G€ | [PAC](https://www.pac-online.com/)/[OPIIEC](https://www.opiiec.fr/) |
| Part des PME dans le marché cyber | ~35 % | 2,24 G€ |
| Dont supervision réseau et SIEM | ~15 % | 336 M€ |
| Part des dépenses logicielles (vs services) | ~40 % | 134 M€ |
| Marché adressable France (services inclus) | | **336 M€** |

#### 3.3 Extension Belgique et Suisse

| Pays | Ratio vs France | Marché cyber estimé | SAM ajusté |
|---|---|---|---|
| Belgique | ~15 % | ~960 M€ | ~50 M€ |
| Suisse | ~20 % | ~1 280 M€ | ~67 M€ |
| **Total extension** | | | **~117 M€** |

#### 3.4 SAM consolidé

| Zone | SAM |
|---|---|
| France | 134 M€ (logiciel) / 336 M€ (services inclus) |
| Belgique | ~50 M€ |
| Suisse | ~67 M€ |
| **SAM total** | **~195 M€ (hors services)** → **~453 M€ (services inclus)** |

**SAM retenu (périmètre France/Belgique/Suisse, logiciel uniquement) : ~195,2 M€**

### 4. SOM — Serviceable Obtainable Market

#### 4.1 Définition

Marché atteignable : part du SAM que BigBrowser peut raisonnablement capturer à 24-36 mois, calculée selon une approche bottom-up.

#### 4.2 Hypothèses bottom-up

| Hypothèse | Valeur | Justification |
|---|---|---|
| Nombre de déploiements cible Y1 | 500 | Benchmark adoption open-source PME |
| Taux de conversion → clients support | 3-5 % | Benchmark SaaS open-source (GitLab, Wazuh) |
| Clients support Y1 | 15 | 500 × 3 % |
| Missions d'audit NIS2 Y1 | 10 | Capacité opérationnelle d'une équipe lean |
| Prix unitaire support (Essentiel) | 2 500 €/an | Benchmark support open-source PME |
| Prix unitaire audit NIS2 | 5 000 € | Marché conseil cybersécurité |
| Prix formation | 2 000 € | Prix de marché |

#### 4.3 Projection revenus Y1

| Flux | Volume | Prix unitaire | Revenu |
|---|---|---|---|
| Support Essentiel | 15 clients | 2 500 € | 37 500 € |
| Mission d'audit NIS2 | 10 missions | 5 000 € | 50 000 € |
| Formation (inter-entreprises) | 5 sessions | 2 000 € | 10 000 € |
| Revenus divers (sponsors GitHub, dons) | — | — | ~5 000 € |
| **Total Y1** | | | **~102 500 €** |

#### 4.4 Projection revenus Y2-Y3

| Année | Déploiements | Clients support | Revenu estimé |
|---|---|---|---|
| Y1 (2027) | 500 | 15 | ~102 500 € |
| Y2 (2028) | 2 000 | 60 | ~360 000 € |
| Y3 (2029) | 5 000 | 150 | ~881 000 € |

#### 4.5 SOM retenu

**SOM Y1 : ~102 500 € (≈0.1 M€)**
**SOM Y3 : ~881 000 € (≈0.88 M€)**

**SOM retenu (horizon 24-36 mois) : ~4,2 M€ cumulés (Y1+Y2+Y3)**

### 5. Synthèse

```
TAM (Marché cyber mondial)     275 G$     250 G€
    │
    ├── SAM (France/Belgique/Suisse, logiciel)   195 M€
    │       │
    │       └── SOM (Objectif 36 mois)           4,2 M€
    │
    └── (Hors périmètre : reste du monde, services)
```

| Métrique | Valeur | Ratio TAM | Ratio SAM |
|---|---|---|---|
| TAM | 250 G€ | 100 % | — |
| SAM | 195 M€ | 0,08 % | 100 % |
| SOM (Y3) | 0,88 M€ | 0,0004 % | 0,45 % |
| SOM (cumul 36 mois) | 4,2 M€ | 0,002 % | 2,2 % |

### 6. Note sur la fiabilité

Ces projections sont des **estimations hautes** fondées sur des hypothèses optimistes mais documentées :

- Le taux de conversion 3-5 % est cohérent avec les benchmarks open-source B2B
- Le volume de 500 déploiements Y1 suppose un effort marketing et communautaire significatif
- Le SOM à 36 mois suppose une croissance de la notoriété et des effets de réseau (bouche-à-oreille, MSP)

---

## Section 6 : Stratégie d'entrée sur le marché (GTM)

### 1. Objectifs de la stratégie GTM

La stratégie Go-To-Market (GTM) de BigBrowser vise à :

1. Maximiser la visibilité et l'adoption de la version open-source
2. Convertir une fraction des utilisateurs en clients de services payants
3. Établir des partenariats MSP comme canal de distribution indirect
4. Créer une crédibilité institutionnelle via les références ANSSI et NIS2

### 2. Canaux de mise sur le marché

| Canal | Priorité | Cible | Effet recherché |
|---|---|---|---|
| GitHub (release publique) | **P1** | Communauté technique | Adoption, stars, forks, contributions |
| Site web / Landing page | **P1** | DSI, dirigeants PME | Crédibilité, téléchargements |
| Partenaires MSP | **P2** | Revendeurs IT | Effet de levier : 1 MSP = 10-50 clients |
| FIC (Forum International Cybersécurité) | **P2** | Professionnels cyber | Notoriété, networking |
| Assises de la Cybersécurité | **P2** | RSSI, DSI | Crédibilité, leads |
| Référencement ANSSI | **P2** | Entités NIS2 | Crédibilité institutionnelle |
| Cybermalveillance.gouv.fr | **P2** | PME victimes | Canal de prévention |
| Réseaux sociaux (LinkedIn, X/Twitter) | **P3** | Communauté cyber | Visibilité continue |

### 3. Plan d'action par canal

#### 3.1 GitHub (Priorité P1)

**Objectif** : Publier BigBrowser en open-source et générer 500 déploiements en Y1.

**Actions clés :**

| Action | Échéance | Responsable |
|---|---|---|
| Publier le code source complet | M1 | Équipe dev |
| Rédiger un README complet : installation, cas d'usage, captures d'écran | M1 | Équipe projet |
| Publier la documentation utilisateur (Guide d'installation, FAQ) | M2 | Équipe projet |
| Configurer GitHub Pages pour le site vitrine | M2 | Équipe technique |
| Activer GitHub Discussions pour la communauté | M2 | Équipe projet |
| Soumettre BigBrowser à GitHub Trending (via stars et traction) | M3-M6 | Communauté |
| Publier des releases régulières (versionnage sémantique) | Continu | Équipe dev |

**Indicateurs :** stars GitHub, forks, clones, issues, contributeurs externes.

#### 3.2 Site web / Landing page (Priorité P1)

**Objectif** : Convertir les visiteurs en utilisateurs.

**Pages requises :**

- Page d'accueil avec proposition de valeur et captures d'écran
- Page « Fonctionnalités » détaillant les 8 fonctions clés
- Page « Conformité NIS2 » expliquant comment BigBrowser répond aux obligations
- Page « Démonstration » (vidéo ou lab en ligne)
- Page « Téléchargement » redirigeant vers GitHub
- Page « Tarifs » (services support, audit, formation)

#### 3.3 Partenaires MSP (Priorité P2)

**Objectif** : Signer 2 partenaires MSP en Y1.

**Profil du partenaire cible :**

- MSP/SSII de 10 à 50 employés
- Portefeuille de 20 à 100 clients PME
- Offre existante : support IT, hébergement, infogérance
- Besoin : ajouter une ligne « cybersécurité NIS2 » à son catalogue

**Offre partenaire :**

- Licence open-source gratuite (sans limite)
- Support technique prioritaire (revendeur)
- Remise sur les missions d'audit NIS2 (co-construction)
- Kit de documentation white-label pour leurs clients

#### 3.4 Événements professionnels (Priorité P2)

| Événement | Type | Coût estimé | Impact attendu |
|---|---|---|---|
| FIC (Lille) | Salon professionnel | 5 000-15 000 € | Notoriété, presse, partenaires |
| Assises de la Cybersécurité (Monaco) | Conférence | 8 000-20 000 € | Leads qualifiés |

**Stratégie :** Privilégier les interventions (talks, ateliers) plutôt que les stands coûteux.

#### 3.5 Référencement institutionnel (Priorité P2)

**Démarches :**

- Demander le référencement sur le catalogue ANSSI des solutions de cybersécurité
- Solliciter une mention sur Cybermalveillance.gouv.fr (rubrique « Se protéger »)
- Contacter le pôle innovation de l'ANSSI pour un éventuel accompagnement

### 4. Stratégie de contenu

#### 4.1 Calendrier éditorial (M1-M6)

| Mois | Contenu | Canal |
|---|---|---|
| M1 | Article de lancement : « BigBrowser, le Splunk des PME » | LinkedIn, blog |
| M2 | Guide : « Conformité NIS2 pour les PME en 5 étapes » | Blog, site web |
| M3 | Cas d'usage : « Comment superviser votre réseau en 10 minutes avec Docker » | Blog, GitHub |
| M4 | Témoignage : « Retour d'expérience d'une PME pilote » | Blog, LinkedIn |
| M5 | Guide technique : « Déployer BigBrowser en production » | Blog, GitHub |
| M6 | Bilan : « 6 mois de BigBrowser — chiffres et apprentissages » | Blog, LinkedIn |

#### 4.2 Profil de contenu type

- Ton : professionnel, accessible, technique sans jargon
- Longueur : 1 500-2 000 mots
- Objectif : SEO orienté « NIS2 PME », « supervision réseau gratuite »
- Format : article + visuel (capture d'écran, schéma architecture)

### 5. Budget GTM estimé (Y1)

| Poste | Budget estimé |
|---|---|
| Hébergement site web + domaine | 200 € |
| Design landing page | 1 500 € |
| Participation FIC (stand ou intervention) | 5 000 € |
| Campagne LinkedIn Ads (test) | 2 000 € |
| Documentation et vidéos | 1 000 € |
| Total | ~9 700 € |

### 6. Roadmap GTM

```
M1    M2    M3    M4    M5    M6    M7    M8    M9    M10   M11   M12
[GitHub release v1.0]
[Landing page]        [Site web complet]
        [Premiers articles]           [FIC]       [Assises]
          [Premiers MSP]        [Animation communauté]
            [Pilotes]    [Premiers clients support]
[ANSSI listing]             [Retours d'expérience]
```

---

## Section 7 : Risques, KPI et preuves

### 1. Matrice des risques

#### 1.1 Risques identifiés

| ID | Risque | Catégorie | P | I | Criticité (P×I) |
|---|---|---|---|---|---|
| R-T01 | **Faux positifs** dégradant la crédibilité de l'outil | Technique | 4 | 3 | **12** |
| R-T02 | **Blocage par IDS/IPS** tiers lors des phases de scan | Technique | 3 | 4 | **12** |
| R-T03 | **Latence UI** pendant un scan ou une capture | Technique | 3 | 3 | **9** |
| R-S01 | **Injection de commandes** via champs IP | Sécurité | 2 | 5 | **10** |
| R-S02 | **Exposition de données** lors des exports | Sécurité | 2 | 4 | **8** |
| R-P01 | **Rupture de planning** (calendrier contraint) | Projet | 4 | 5 | **20** |
| R-P02 | **Conflits Git** lors des fusions de branches | Projet | 3 | 4 | **12** |
| R-P03 | **Défaut de preuve** en démonstration | Projet | 2 | 5 | **10** |
| R-M01 | **Adoption insuffisante** de la version open-source | Marché | 4 | 4 | **16** |
| R-M02 | **Concurrence** des outils établis (Wazuh, PRTG) | Marché | 3 | 3 | **9** |
| R-M03 | **Difficulté à recruter** des profils cyber | Marché | 4 | 4 | **16** |

#### 1.2 Risques marché détaillés

##### R-M01 : Adoption insuffisante (Criticité : 16)

| Facteur | Description |
|---|---|
| Probabilité | 4/5 — L'écosystème open-source est saturé, se démarquer est difficile |
| Impact | 4/5 — Sans adoption, pas de conversion vers les services payants |
| Signaux faibles | Faible nombre de stars GitHub, peu de téléchargements Docker, absence de contributeurs externes |
| Mitigation | Stratégie de contenu active (articles, tutoriels), présence GitHub Trending, partenariat ANSSI, présences aux événements (FIC, Assises) |

##### R-M02 : Concurrence (Criticité : 9)

| Facteur | Description |
|---|---|
| Probabilité | 3/5 — Wazuh et Security Onion sont bien établis |
| Impact | 3/5 — La différenciation UX et NIS2 limite le risque |
| Mitigation | Positionnement clair sur la simplicité et la conformité NIS2, documentation orientée PME |

##### R-M03 : Recrutement (Criticité : 16)

| Facteur | Description |
|---|---|
| Probabilité | 4/5 — Pénurie généralisée de profils cybersécurité |
| Impact | 4/5 — Sans développeur, le produit ne peut pas évoluer |
| Mitigation | Partenariats écoles (alternance), projet open-source comme marque employeur, implication de la communauté |

### 2. Indicateurs clés de performance (KPI)

#### 2.1 KPI d'adoption

| KPI | Cible Y1 | Cible Y2 | Cible Y3 | Mesure |
|---|---|---|---|---|
| Déploiements (clusters Docker uniques) | 500 | 2 000 | 5 000 | Compteur de téléchargements Docker Hub |
| Stars GitHub | 500 | 2 000 | 5 000 | GitHub |
| Contributeurs externes | 5 | 20 | 50 | GitHub |
| Issues ouvertes par des tiers | 20 | 100 | 300 | GitHub |
| Visiteurs uniques site web | 5 000/mois | 20 000/mois | 50 000/mois | Analytics |

#### 2.2 KPI commerciaux

| KPI | Cible Y1 | Cible Y2 | Cible Y3 | Mesure |
|---|---|---|---|---|
| Clients support payant | 15 | 60 | 150 | Contrats signés |
| Missions d'audit NIS2 | 10 | 30 | 60 | Missions réalisées |
| Sessions de formation | 5 | 15 | 30 | Formations dispensées |
| Chiffre d'affaires annuel | 102 500 € | 360 000 € | 881 000 € | Facturation |
| Partenaires MSP signés | 2 | 10 | 20 | Contrats partenaires |

#### 2.3 KPI qualité

| KPI | Cible | Mesure |
|---|---|---|
| Temps de réponse UI (< 2s) | ≥ 95 % des requêtes | Monitoring applicatif |
| Taux de faux positifs | < 20 % | Revue trimestrielle des alertes |
| Uptime de l'application | ≥ 99 % | Healthcheck |
| Satisfaction client support | NPS ≥ 30 | Enquête semestrielle |

### 3. Preuves de validation

#### 3.1 Preuves attendues en démonstration

| # | Preuve | Scénario de recette associé |
|---|---|---|
| 1 | Authentification fonctionnelle (login/logout) | REC-001 |
| 2 | Contrôle des permissions (admin vs analyste) | REC-002 |
| 3 | Scan réseau borné et découverte d'actifs | REC-003 |
| 4 | Détection d'un comportement suspect et génération d'alerte | REC-004 |
| 5 | Cycle de vie d'alerte (nouvelle → en cours → clôturée) | REC-005 |
| 6 | Export CSV et JSON avec métadonnées | REC-006 |
| 7 | Rejet d'une injection IP (validation Pydantic) | REC-007 |
| 8 | Temps de réponse < 2s sur les vues principales | REC-008 |
| 9 | Endpoint /health opérationnel | REC-009 |
| 10 | Chaîne complète : scan → détection → alerte → export | REC-010 |

#### 3.2 Preuves de conformité NIS2

| Exigence NIS2 | Preuve BigBrowser |
|---|---|
| Supervision réseau obligatoire | Scan réseau, détection d'actifs, capture trafic |
| Traçabilité des incidents | Journalisation (audit_logs) de toutes les actions sensibles |
| Déclaration des incidents (24h/72h) | Exports CSV/JSON horodatés, prêts pour transmission ANSSI |
| Reporting de conformité | Dashboard avec métriques, exports de preuve |

#### 3.3 Preuves pour les investisseurs / partenaires

| Document | Contenu | Disponibilité |
|---|---|---|
| Étude de marché (ce document) | TAM/SAM/SOM, benchmark, positionnement | Mai 2026 |
| Business model | Open-core, monétisation services | Mai 2026 |
| Business plan | Comptes prévisionnels 3 ans | Mai 2026 |
| Cahier des charges | Exigences fonctionnelles, recette | Mai 2026 |
| Architecture technique | Schéma, composants, flux | Mai 2026 |
| Roadmap produit | Fonctionnalités v1, v2, v3 | Mai 2026 |
| Démo en ligne | Lab Docker reproductible | Mai 2026 |

---

## Section 8 : Sources de référence

### 8.1 Sources institutionnelles et réglementaires

#### 8.1.1 ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information)

- [ANSSI, Panorama de la cybermenace 2025](https://cyber.gouv.fr/actualites/panorama-de-la-cybermenace-2025/)
- [ANSSI — Site officiel](https://www.ssi.gouv.fr)
- [ANSSI — Rapport d'activité](https://www.ssi.gouv.fr/rapport-activite/)
- [ANSSI — Guide NIS2 (transposition française)](https://www.ssi.gouv.fr/nis2/)
- [ANSSI — Catalogue de solutions de cybersécurité](https://www.ssi.gouv.fr/catalogue/)
- [CERT-FR CTI](https://www.cert.ssi.gouv.fr/cti/CERTFR-2026-CTI-002/)

#### 8.1.2 Cybermalveillance.gouv.fr

- [Cybermalveillance.gouv.fr, Rapport d'activité 2025](https://www.cybermalveillance.gouv.fr/tous-nos-contenus/actualites/rapport-activite-2025)
- [Cybermalveillance.gouv.fr — Site officiel](https://www.cybermalveillance.gouv.fr)
- [Cybermalveillance.gouv.fr — Baromètre cyber](https://www.cybermalveillance.gouv.fr/barometre)
- [Cybermalveillance.gouv.fr — Cyber Threat Score](https://www.cybermalveillance.gouv.fr/threat-score)
- [Cybermalveillance.gouv.fr — Guide PME](https://www.cybermalveillance.gouv.fr/pme)

#### 8.1.3 Commission européenne — Directive NIS2

- [Commission européenne, directive NIS2](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive)
- [Directive NIS2 (2022/2555) — Texte officiel](https://eur-lex.europa.eu/eli/dir/2022/2555)
- [Transposition NIS2 États membres](https://digital-strategy.ec.europa.eu/en/policies/nis2-transposition)
- [DORA directive](https://digital-strategy.ec.europa.eu/en/policies/dora)

#### 8.1.4 ENISA (European Union Agency for Cybersecurity)

- [ENISA](https://www.enisa.europa.eu/)
- [ENISA — Threat Landscape Report](https://www.enisa.europa.eu/topics/threat-landscape)
- [ENISA — NIS2 guidelines](https://www.enisa.europa.eu/nis2)

#### 8.1.5 Autorités nationales de cybersécurité

- [CCB Belgium](https://ccb.belgium.be/en)
- [NCSC Suisse](https://www.ncsc.admin.ch/ncsc/fr/home/dokumentation/berichte/lageberichte/halbjahresbericht-2025-1.html)

#### 8.1.6 Normes et référentiels

- [NIST CSF 2.0](https://www.nist.gov/cyberframework)
- [OWASP ASVS (Application Security Verification Standard)](https://owasp.org/www-project-application-security-verification-standard/)
- [MITRE ATT&CK Framework](https://attack.mitre.org)
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)
- [SANS Institute](https://www.sans.org)

### 8.2 Sources de marché et études sectorielles

#### 8.2.1 Cabinets d'analystes

- [Mordor Intelligence](https://www.mordorintelligence.com/)
- [Gartner](https://www.gartner.com/)
- [PAC](https://www.pac-online.com/)
- [OPIIEC](https://www.opiiec.fr/)
- [Fortune Business Insights](https://www.fortunebusinessinsights.com/)
- [Precedence Research](https://www.precedenceresearch.com/)
- [Future Market Insights](https://www.futuremarketinsights.com/)
- [Xerfi](https://www.xerfi.com/)
- [Numeum](https://numeum.fr/)
- [INSEE](https://www.insee.fr/)
- [Statbel Belgique](https://statbel.fgov.be/en/themes/enterprises)

#### 8.2.2 Rapports de menace

- [Verizon DBIR](https://www.verizon.com/business/resources/reports/dbir/)
- [IBM Cost of Data Breach](https://www.ibm.com/reports/data-breach)
- [PwC Global Digital Trust Insights](https://www.pwc.com/gx/en/issues/cybersecurity/global-digital-trust-insights.html)
- [Google Cloud Mandiant M-Trends](https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2025)
- [World Economic Forum](https://www.weforum.org/)
- [OECD](https://www.oecd.org/digital/digital-security/)

### 8.3 Sources concurrentielles et pricing

#### 8.3.1 Solutions open-source

| Outil | Licence | URL | Pricing |
|---|---|---|---|
| Nmap | GPLv2 | [Nmap](https://nmap.org/) | Gratuit |
| Wireshark | GPLv2 | [Wireshark](https://www.wireshark.org/) | Gratuit |
| Suricata | GPLv2 | [Suricata docs](https://suricata.io/documentation/) | Gratuit |
| Snort | GPLv2 | [Snort](https://www.snort.org/) | Gratuit |
| Zeek | BSD | [Zeek docs](https://docs.zeek.org/) | Gratuit |
| Wazuh | GPLv2 | [Wazuh](https://wazuh.com/) | Gratuit (support payant : [Wazuh Cloud pricing](https://wazuh.com/cloud/)) |
| Security Onion | GPLv2 | [Security Onion docs](https://docs.securityonion.net/) | Gratuit (support payant) |
| OSSEC | GPLv2 | — | Gratuit |

#### 8.3.2 Solutions enterprise

| Solution | Modèle | URL | Pricing indicatif |
|---|---|---|---|
| Splunk | Licence (volume) | [Splunk pricing](https://www.splunk.com/en_us/products/pricing.html) | ~20 000 €/an minimum |
| Microsoft Sentinel | SaaS (GB ingérés) | [Microsoft Sentinel pricing](https://azure.microsoft.com/en-us/pricing/details/microsoft-sentinel/) | ~2-5 $/GB |
| IBM QRadar | Licence + maintenance | — | ~30 000 €/an |
| Palo Alto XSIAM | Abonnement | — | > 50 000 €/an |
| Elastic Security | SaaS / Autogéré | [Elastic pricing](https://www.elastic.co/pricing/) | Gratuit (basic), ~100 €/mois (cloud) |
| Datadog Security | SaaS | [Datadog pricing](https://www.datadoghq.com/pricing/?product=cloud-siem) | ~15 $/host/mois |

#### 8.3.3 Solutions supervision IT

| Solution | Modèle | URL | Pricing indicatif |
|---|---|---|---|
| PRTG | Freemium | [PRTG](https://www.paessler.com/prtg) | 100 capteurs gratuits, puis payant |
| SolarWinds | Licence | [SolarWinds NPM](https://www.solarwinds.com/network-performance-monitor) | ~3 000 €/an |
| Nagios | Open-source | [Nagios](https://www.nagios.org/) | Gratuit (support payant) |
| Zabbix | Open-source | — | Gratuit (support payant) |

### 8.4 Sources académiques et techniques

- [Jedha](https://www.jedha.co/)
- [Diginamic](https://www.diginamic.fr/)
- [CSB School](https://www.csb.school/)
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)
- [MITRE ATT&CK](https://attack.mitre.org)
- [NIST CSF 2.0](https://www.nist.gov/cyberframework)
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)
- [SANS Institute](https://www.sans.org)

### 8.5 Programmes financement et accompagnement

| Programme | Description | URL |
|---|---|---|
| France 2030 (volet Cyber PME) | Enveloppe 100 M€ pour la cybersécurité des PME | [France 2030](https://www.france2030.gouv.fr/) |
| France Num | Accompagnement numérique PME | — |
| BPI France | Financement innovation | — |

### 8.6 Média et veille cybersécurité

- [LeMagIT (cybersécurité)](https://www.lemagit.fr)
- [ZDNet France (sécurité)](https://www.zdnet.fr)
- [The Hacker News](https://thehackernews.com)
- [BleepingComputer](https://www.bleepingcomputer.com)
- [Krebs on Security](https://krebsonsecurity.com)
- [SecurityWeek](https://www.securityweek.com)

### 8.7 Open-source et communautés

- [GitHub Trending](https://github.com/trending)
- [Open Source Initiative](https://opensource.org)
- [CNCF (Cloud Native Computing Foundation)](https://www.cncf.io)
- [Docker Hub](https://hub.docker.com)

### 8.8 Notes méthodologiques

- Les prix indicatifs mentionnés dans ce document sont issus de sources publiques (sites officiels, comparateurs, retours d'expérience) et peuvent varier selon les configurations et négociations commerciales.
- Les données de marché (Mordor Intelligence, Gartner, PAC) sont issues de rapports publics ou de synthèses accessibles en ligne. Les chiffres précis peuvent différer selon les périmètres retenus par chaque cabinet.
- Les traductions des noms de rapports et d'autorités sont libres et données à titre indicatif.
- Dernière mise à jour des URLs : Mai 2026.

---

*Document consolidé à partir des fichiers 01 à 08 des références de l'étude de marché BigBrowser. Mai 2026.*
