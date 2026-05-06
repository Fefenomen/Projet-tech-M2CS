# Références — Business Model BigBrowser

> *Sources et références utilisées pour l'élaboration du Business Model*

---

## 1. Documents Internes du Projet

| Document | Chemin | Date |
|---|---|---|
| Étude de marché | `documents/02_etude_de_marche/rendu_principal.md` | Avril 2026 |
| Feuille de cadrage | `documents/05_feuille_de_cadrage/rendu_principal.md` | Avril 2026 |
| Cahier des charges | `documents/06_cahier_des_charges/rendu_principal.md` | Avril 2026 |
| Architecture technique | `documents/08_architecture/rendu_principal.md` | Avril 2026 |

---

## 2. Sources Institutionnelles et Réglementaires

### 2.1. ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information)

- **Panorama de la Cybermenace 2024** — ANSSI
  - 4 386 événements de sécurité traités en 2024 (+15%)
  - 1 361 incidents confirmés
  - 144 compromissions par ransomware

- **Directive NIS2 (2022/2555)**
  - Entrée en vigueur : octobre 2024
  - 18 secteurs d'activité concernés (vs 7 pour NIS1)
  - 15 000 entités françaises à mettre en conformité
  - Sanctions : jusqu'à 2 % du CA mondial

- **ReCyF (Référentiel Cyber pour les Fournisseurs)**
  - Piliers : Gouvernance / Protection / Défense / Résilience

### 2.2. Cybermalveillance.gouv.fr

- **Baromètre national 2025**
  - 16 % des entreprises ont subi un incident cyber (12 derniers mois)
  - 75 % des cyberattaques visent les PME
  - 60 % des PME investissent moins de 1 000 €/an en cyber
  - 57 % expriment un besoin d'outils de protection accessibles

### 2.3. Réglementation Complémentaire

- **DORA (Digital Operational Resilience Act)**
  - Entrée en vigueur : janvier 2025
  - Secteur financier : obligations de supervision continues

- **France 2030 Cyber PME**
  - Enveloppe : 100 millions d'euros
  - Objectif : accélérer la mise en conformité NIS2

---

## 3. Sources de Marché et Études

### 3.1. Cabinet PAC (Pierre Audoin Consultants)

- **Marché cybersécurité France 2025**
  - 6,4 Md€ en France (+10 %/an)
  - SIEM / SOC : 441 M€ (+16 %/an)
  - Sécurité périmétrique : 790 M€ (+11 %/an)
  - Gestion identités : 209 M€ (+13,1 %/an)
  - Projection 2029 : 11,36 Md€

### 3.2. Gartner

- **Dépenses mondiales cybersécurité**
  - Croissance 2024 : +13,4 %
  - Prévision 2025 : +15,1 %
  - Marché mondial 2025 : >250 Md$
  - Projection 2029 : >350 Md$

### 3.3. Mordor Intelligence

- **Network Monitoring & SIEM**
  - Marché supervision réseau : 4,1 Md$ (TCAC 9,5 %)
  - SIEM global : 4,8 Md$ (2021) → 11,3 Md$ (2026)
  - Réduction temps d'investigation de 60 % avec SIEM activé par IA

### 3.4. Fortune Business Insights

- **Logiciels supervision réseau** : 8,7 Md$ → 15,5 Md$ (2032)
- **Monitoring Tools (incl. sécurité)** : 36,6 Md$ → 185 Md$ (2034)

### 3.5. Precedence Research

- **Network Monitoring & Management** : 12,5 Md$ → 25,5 Md$ (2033)
- **TCAC** : 9,2 %

### 3.6. Future Market Report

- **Logiciels supervision réseau** : 8,7 Md$ → 15,5 Md$ (2032, TCAC 7,25 %)

---

## 4. Sources Sectorielles et Formation

### 4.1. OPIIEC

- **Formations cybersécurité France**
  - >900 formations référencées
  - 45 000 professionnels en 2023
  - Besoin estimé : 70 000 d'ici 2028
  - 3 % des postes Tech en France = cybersécurité

### 4.2. Numeum

- Syndicat professionnel du numérique en France
- Données sur la croissance du secteur cyber

### 4.3. Xerfi

- Études sectorielles cybersécurité
- Analyse de la maturité cyber des PME

---

## 5. Sources Complémentaires

### 5.1. Jedha

- **Statistiques PME cyber 2025**
  - 60 % des PME ferment après une attaque sérieuse (6 mois)
  - 94 % des grandes entreprises ont une assurance cyber vs 3,5 % des PME

### 5.2. Diginamic

- **Cyberattaques PME 2023** : 330 000+ attaques réussies

### 5.3. CSB School

- **Perte moyenne d'action** après attaque (grands comptes) : -19,5 % sur 1 an

---

## 6. Standards Techniques et Sécurité

### 6.1. OWASP

- **OWASP ASVS (Application Security Verification Standard)**
  - Référentiel de sécurisation applicative
  - Utilisé pour les exigences de sécurité du cahier des charges

### 6.2. Standards Open-Source

- **Licences** : GPLv2, Apache 2.0
- **Stack technique** : Python / FastAPI / HTML/CSS/JS
- **Outils de référence** : Nmap, Wireshark, Suricata, Zeek, Wazuh

---

## 7. Concurrents et Benchmarks

| Concurrent | Type | Licence | Référence |
|---|---|---|---|
| Splunk (Cisco) | Enterprise SIEM | Propriétaire | Acquisition 28 Md$ (2024) |
| Microsoft Sentinel | Cloud-native SIEM | Propriétaire | Usage-based pricing |
| Wazuh | Open-source SIEM/HIDS | GPLv2 | >1M téléchargements |
| Nmap | Scan réseau | GPLv2 | Référence secteur |
| Wireshark | Analyse paquets | GPLv2 | Standard pédagogique |
| Suricata | IDS/IPS | GPLv2 | Multi-thread, DPI |
| Zeek (ex-Bro) | Analyse comportementale | BSD | Scriptable, forensique |
| PRTG | Supervision réseau | Propriétaire | Freemium (100 capteurs) |

---

## 8. Hypothèses de Business Model

| Hypothèse | Valeur | Source |
|---|---|---|
| Taux de conversion open-source → services | 3 à 5 % | Benchmark SaaS open-source |
| Panier moyen support | 280 €/mois | Analyse concurrentielle |
| Panier moyen audit NIS2 | 3 000 € | Prix journée audit |
| Panier moyen formation | 2 500 €/groupe | Marché formation |
| Croissance marché cyber France | +10 %/an | PAC, Gartner |
| Nombre entités NIS2 France | 15 000 | ANSSI |
| TAM (Total Addressable Market) | >250 Md$ | Marché mondial |
| SAM (France, BE, CH NIS2) | 195,2 M€ | Modélisation bottom-up |
| SOM (24-36 mois) | 4,2 M€ | Parts de marché atteignable |

---

## 9. Modèle de Conversion et Calculs

### 9.1. Calcul du CA Année 1

| Source | Calcul | Montant |
|---|---|---|
| Support (15 clients × 280€ × 8 mois) | 15 × 280 × 8 | 33 600 € |
| Audits (10 missions × 3 000€) | 10 × 3 000 | 30 000 € |
| Formations (5 groupes × 2 500€) | 5 × 2 500 | 12 500 € |
| MSP (2 partenaires × 400€ × 12 mois) | 2 × 400 × 12 | 9 600 € |
| **TOTAL** | | **84 000 €** |

### 9.2. Seuils de Rentabilité

- **Point mort** : ~300 déploiements avec 3 % de conversion
- **Marge d'exploitation An 1** : 16,7 %
- **Projection An 3** : 881 000 € (marge 34,2 %)

---

*Document de références établi en mai 2026*
