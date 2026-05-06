# Références — Business Plan BigBrowser

> *Sources et références utilisées pour l'élaboration du Business Plan*

---

## 1. Documents Internes du Projet

| Document | Chemin | Date |
|---|---|---|
| Business Model | `documents/03_business_model/rendu_principal.md` | Avril 2026 |
| Étude de marché | `documents/02_etude_de_marche/rendu_principal.md` | Avril 2026 |
| Feuille de cadrage | `documents/05_feuille_de_cadrage/rendu_principal.md` | Avril 2026 |
| Cahier des charges | `documents/06_cahier_des_charges/rendu_principal.md` | Avril 2026 |
| Architecture technique | `documents/08_architecture/rendu_principal.md` | Avril 2026 |

---

## 2. Sources Institutionnelles et Réglementaires

### 2.1. ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information)

- **Panorama de la Cybermenace 2024**
  - 4 386 événements traités (+15 % vs 2023)
  - 1 361 incidents confirmés
  - 144 compromissions ransomware documentées
  - Score d'intensité 2026 : 1 114,8 (niveau Élevé)

- **Directive NIS2 (2022/2555)**
  - Entrée en vigueur : 18 octobre 2024
  - Transposition France : 2027
  - 18 secteurs d'activité (vs 7 pour NIS1)
  - 10 000–15 000 entités françaises concernées
  - Supervision continue obligatoire des SI
  - Sanctions : jusqu'à 2 % du CA mondial (essentielles), 1,4 % (importantes)
  - Responsabilité personnelle des dirigeants

- **ReCyF (Référentiel Cyber pour les Fournisseurs)**
  - Piliers : Gouvernance / Protection / Défense / Résilience
  - Tableau de bord conformité NIS2 (v2+)

### 2.2. Cybermalveillance.gouv.fr

- **Baromètre national 2025**
  - 16 % des entreprises : incident cyber (12 derniers mois)
  - 3/4 des PME : <2 000 € d'investissement cyber/an
  - 75 % des attaques visent les PME
  - 6 PME sur 10 ne sauraient pas évaluer les conséquences d'une attaque
  - 93 % des dirigeants se sentent protégés (paradoxe)

### 2.3. Réglementation et Aides

- **DORA (Digital Operational Resilience Act)**
  - Entrée en vigueur : janvier 2025
  - Secteur financier : obligations supervision continues

- **France 2030 Cyber PME**
  - Enveloppe : 100 millions d'euros
  - Objectif : accélérer mise en conformité NIS2 PME

---

## 3. Études de Marché et Analyse Sectorielle

### 3.1. Cabinet PAC (Pierre Audoin Consultants)

- **Marché cybersécurité France**
  - 2025 : 6,4 Md€ (+10 %/an)
  - 2029 : 11,36 Md€ (projection)
  - Part cybersécurité dans dépenses IT : 6 % (2014) → 11,6 % (2025)

- **Segments France 2025**
  - SIEM / SOC / Gouvernance : 441 M€ (+16 %)
  - Sécurité périmétrique (EDR, XDR, MDR) : 790 M€ (+11 %)
  - Gestion identités et accès : 209 M€ (+13,1 %)
  - Chiffrement : 65 M€ (+13,7 %)
  - Services managés (MSSP) : part majeure des 4,96 Md€ (+14 %)

### 3.2. Gartner

- **Dépenses mondiales cybersécurité**
  - Croissance 2024 : +13,4 %
  - Prévision 2025 : +15,1 %
  - Marché 2025 : >250 Md$
  - Projection 2029 : >350 Md$

### 3.3. Mordor Intelligence

- **Network Monitoring**
  - Marché 2024-2025 : 2,88–4,13 Md$
  - Projection 2030-34 : 5–9,5 Md$
  - TCAC : 9–11 %

- **SIEM Global**
  - 2021 : 4,8 Md$
  - 2026 : 11,3 Md$ (TCAC 14,5 %)

- **Bénéfices IA/ML** : réduction de 60 % du temps d'investigation manuelle

### 3.4. Fortune Business Insights

- **Monitoring Tools (incl. sécurité)** : 36,6 Md$ → 185 Md$ (2034, TCAC 17,6 %)

### 3.5. Precedence Research

- **Network Monitoring & Management** : 12,5 Md$ → 25,5 Md$ (2033, TCAC 9,2 %)

### 3.6. Future Market Report

- **Logiciels supervision réseau** : 8,7 Md$ → 15,5 Md$ (2032, TCAC 7,25 %)

---

## 4. Sources PME et Formation

### 4.1. OPIIEC

- **Formation cybersécurité France**
  - >900 formations référencées
  - 45 000 professionnels en 2023
  - Besoin 2028 : 70 000 professionnels
  - 3 % des postes Tech = cybersécurité

### 4.2. Numeum

- Syndicat professionnel numérique France
- Données croissance secteur cyber

### 4.3. Xerfi

- Études sectorielles cybersécurité
- Analyse maturité cyber PME

### 4.4. Jedha

- **Statistiques PME 2025**
  - 60 % des PME ferment après attaque sérieuse (6 mois)
  - 94 % grandes entreprises ont assurance cyber vs 3,5 % PME

### 4.5. Diginamic

- **Attaques réussies PME 2023** : 330 000+

### 4.6. CSB School

- **Perte action grands comptes** après attaque : -19,5 % (1 an)

---

## 5. Standards Techniques et Sécurité

### 5.1. OWASP

- **OWASP ASVS (Application Security Verification Standard)**
  - Référentiel sécurisation applicative
  - Base des exigences de sécurité (SEC-001 à SEC-008)

### 5.2. Standards et Protocoles

- **Pydantic** : validation des données d'entrée
- **Regex** : validation stricte des champs IP, filtres
- **JSON/CSV** : formats d'export standard pour audit NIS2
- **REST API** : contrat API MVP (/auth, /scan, /assets, /alerts, /exports)

### 5.3. Stack Technique

- **Backend** : Python / FastAPI
- **Frontend** : HTML / CSS / JavaScript
- **Déploiement** : On-premise (sans cloud)
- **Architecture** : Modules fonctionnels (scan, capture, détection, reporting, worker asynchrone)

---

## 6. Analyse Concurrentielle

| Outil | Fonction principale | Licence | Limite clé | Positionnement |
|---|---|---|---|---|
| **BigBrowser** | Supervision unifiée web | Open-source | Pas d'IA/ML v1 | PME, NIS2 |
| Splunk (Cisco) | SIEM full-stack | Propriétaire | >10k$/an, complexe | Enterprise uniquement |
| Microsoft Sentinel | SIEM cloud Azure | Propriétaire | Usage-based élevé | Enterprise |
| Wazuh | SIEM/HIDS open-source | GPLv2 | Orienté hôte, pas scan IP | Concurrence indirecte |
| Nmap | Scan ports/réseau | GPLv2 | CLI uniquement | Outil technique |
| Wireshark | Analyse paquets | GPLv2 | Desktop, pas d'alertes | Pédagogique |
| Suricata | IDS/IPS DPI | GPLv2 | Pas d'interface unifiée | Technique |
| Zeek (ex-Bro) | Analyse comportementale | BSD | Complexe, pas UI web | Expert |
| PRTG | Supervision réseau | Propriétaire | Freemium limité | PME (partiel) |

**Gap concurrentiel :** Aucun outil open-source n'unifie les 8 fonctionnalités dans une interface web.

---

## 7. Modélisation Économique et Financière

### 7.1. TAM / SAM / SOM

| Niveau | Définition | Valeur | Méthode |
|---|---|---|---|
| **TAM** | Marché mondial cybersécurité | >250 Md$ | Gartner |
| **SAM** | PME/ETI France, BE, CH NIS2 | 195,2 M€ | Bottom-up |
| **SOM** | Parts atteignable 24-36 mois | 4,2 M€ | Business plan |

### 7.2. Hypothèses Business Plan

| Hypothèse | Valeur | Source |
|---|---|---|
| Taux conversion open-source → services | 3 à 5 % | Benchmark SaaS open-source |
| Panier moyen support | 280 €/mois | Analyse concurrentielle |
| Panier moyen audit NIS2 | 3 000 €/mission | Prix journée audit |
| Panier moyen formation | 2 500 €/groupe | Marché formation |
| Nombre déploiements cible An 1 | 500 | Objectif GitHub + MSP |
| Objectif clients support An 1 | 15 | Conversion 3 % |
| Croissance CA An 1 → An 2 | +302 % | Projection |
| Croissance CA An 2 → An 3 | +161 % | Projection |

### 7.3. Compte de Résultat Projections

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

### 7.4. Seuils de Rentabilité

- **Point mort quantitatif** : ~300 déploiements avec 3 % de conversion
- **Rentabilité** : Atteinte dès l'Année 1 (marge positive 16,7 %)
- **Objectif An 3** : Positionnement leader PME cyber France

---

## 8. Stratégie Go-to-Market

### 8.1. Phase 1 — Lancement & Traction (M1–M6)

- **Publication GitHub** : v1.0, README, documentation
- **Cible** : 500 déploiements, 2 MSP partenaires
- **Actions** : FIC, Les Assises, 5–10 PME pilotes, référencement ANSSI

### 8.2. Phase 2 — Monétisation (M6–M18)

- **Cible** : 15 clients support, 10 missions audit, CA 84 k€
- **Actions** : Support Essentiel, audit NIS2, formations, certification MSP

### 8.3. Phase 3 — Industrialisation (M18–M36)

- **Cible** : CA 881 k€, 20+ MSP, 5 000 déploiements
- **Actions** : Modules IA/ML, dashboard NIS2, SaaS, France 2030

---

## 9. Équipe et Organisation

| Rôle | Compétences | Disponibilité | Statut |
|---|---|---|---|
| Chef de projet / PO | Gestion projet, vision produit, cyber | Temps plein | À recruter |
| Développeur senior | Python, FastAPI, sécurité réseau | Temps plein | À recruter |
| Expert cyber | NIS2, audit, IDS/IPS, Wireshark, Nmap | Partiel / prestation | À recruter |
| Commercial / BizDev | Vente B2B, partenariats, PME/MSP | Partiel (Phase 1) | À recruter |

---

## 10. Risques et Mitigation

| # | Risque | Probabilité | Impact | Criticité | Mitigation |
|---|---|---|---|---|---|
| R1 | Adoption open-source insuffisante | Élevée | Élevé | **16** | Stratégie contenu, FIC, ANSSI |
| R2 | Concurrence (Wazuh, PRTG) | Moyenne | Moyen | **9** | Différenciation UX, interface unifiée |
| R3 | Retard transposition NIS2 | Moyenne | Moyen | **9** | Valeur opérationnelle indépendante |
| R4 | Difficulté recrutement cyber | Élevée | Élevé | **16** | Partenariats écoles, alternances |
| R5 | Faux positifs nuisant crédibilité | Moyenne | Moyen | **9** | Investissement QA, bêta-test |
| R6 | Consolidation marché (Cisco-Splunk) | Faible | Faible | **4** | Positionnement prix et open-source |

---

## 11. Financement et Investissement

| Source | Montant envisagé | Statut |
|---|---|---|
| Fonds propres | 20 000 € | À confirmer |
| France 2030 Cyber PME | 50 000–100 000 € | Dossier à déposer (M18) |
| Prêt bancaire | 30 000 € | Sous réserve garanties |
| Business Angels | 50 000 € | Prospection Phase 2 |
| **TOTAL** | **150 000–200 000 €** | |

### Utilisation des fonds

- Recrutement équipe (M1–M12) : 80 000 €
- Infrastructure & outils : 15 000 €
- Marketing & salons : 25 000 €
- Frais juridiques : 10 000 €
- Trésorerie précaution : 20 000 €

---

## 12. Indicateurs de Performance (KPI)

### 12.1. KPI Produit & Technique

| KPI | An 1 | An 2 | An 3 |
|---|---|---|---|
| Déploiements actifs | 500 | 2 000 | 5 000 |
| Stars GitHub | 100 | 500 | 1 500 |
| Forks GitHub | 20 | 100 | 300 |
| Contributeurs actifs | 5 | 20 | 50 |

### 12.2. KPI Commercial & Financier

| KPI | An 1 | An 2 | An 3 |
|---|---|---|---|
| Clients support | 15 | 60 | 150 |
| Missions d'audit | 10 | 35 | 80 |
| Partenaires MSP | 2 | 10 | 20+ |
| CA | 84 k€ | 338 k€ | 881 k€ |
| Marge d'exploitation | 16,7 % | 29,0 % | 34,2 % |

---

## 13. Jalons et Calendrier

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

---

*Document de références établi en mai 2026 — Sources : ANSSI, PAC, Gartner, Mordor Intelligence, Cybermalveillance.gouv.fr, OPIIEC, Numeum, Xerfi, Fortune Business Insights, Precedence Research*
