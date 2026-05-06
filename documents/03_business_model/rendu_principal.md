# Business Model — BigBrowser

> **Modèle Open-Source + Services**
>
> *Avril 2026*

---

## Table des matières

1. [Résumé Exécutif](#1-résumé-exécutif)
2. [Proposition de Valeur](#2-proposition-de-valeur)
3. [Segments de Clientèle](#3-segments-de-clientèle)
4. [Canaux de Distribution](#4-canaux-de-distribution)
5. [Relations Client](#5-relations-client)
6. [Flux de Revenus](#6-flux-de-revenus)
7. [Ressources Clés](#7-ressources-clés)
8. [Activités Clés](#8-activités-clés)
9. [Partenariats Clés](#9-partenariats-clés)
10. [Structure de Coûts](#10-structure-de-coûts)
11. [Analyse du Modèle](#11-analyse-du-modèle)
12. [Projections Financières](#12-projections-financières)

---

## 1. Résumé Exécutif

BigBrowser adopte un modèle **open-core hybride** : le cœur fonctionnel (8 fonctionnalités clés) est distribué gratuitement sous licence open-source, tandis que la monétisation repose sur des services à haute valeur ajoutée.

| Élément | Détail |
|---|---|
| **Modèle économique** | Open-core + Services (Support, Audit, Formation) |
| **Cible principale** | PME françaises (10–250 employés) soumises à NIS2 |
| **Valeur offerte** | Supervision réseau complète, interface web unifiée, conformité NIS2 |
| **Différenciateur** | 8 fonctionnalités dans une seule interface web — Splunk pour les PME, sans le prix |
| **Licence** | GPLv2 ou Apache 2.0 (arbitrage juridique en cours) |

---

## 2. Proposition de Valeur

### 2.1. Produit Core (Gratuit — Open-Source)

- **Scan de plages IP** et découverte d'équipements
- **Détection de ports ouverts** et services réseau
- **Capture et analyse** du trafic réseau
- **Détection de comportements suspects** (règles)
- **Système d'alertes** configurables
- **Interface web unifiée** (tableau de bord)
- **Exports JSON et CSV** pour audit et conformité
- **Déployable on-premise** (sans cloud)

### 2.2. Services Premium (Payants)

| Service | Description | Tarif indicatif |
|---|---|---|
| **Support Essentiel** | Accès support prioritaire, mises à jour, corrections | 280 €/mois |
| **Audit NIS2** | Mission de conformité, rapport d'analyse, préconisations | 3 000 €/mission |
| **Formation** | Inter-entreprises ou sur site, TP avec BigBrowser | 2 500 €/groupe |
| **Partenariat MSP** | Licence revendeur, formation technique, support dédié | 400 €/mois/MSP |

---

## 3. Segments de Clientèle

| Segment | Profil | Besoin spécifique | Disposition à payer | Potentiel |
|---|---|---|---|---|
| **PME / ETI** | 50–500 employés, DSI limitée | Visibilité réseau simple, alertes claires, conformité NIS2 | Faible (<2000€/an) | Très fort |
| **Secteur public** | Collectivités, hôpitaux (NIS2) | Conformité réglementaire, rapports auditeurs | Moyen (budget public) | Fort |
| **Formation / Éducation** | Écoles d'ingénieurs, BTS, IUT | Outil opérationnel pour TP et démonstrations | Faible (gratuit) | Fort (volume) |
| **MSP / SSII** | Prestataires IT gérant des PME | Outil de diagnostic pour audits clients | Moyen | Fort |
| **Admins réseau** | Consultants, freelances cyber | Toolbox complète, exportable pour rapports | Moyen | Moyen |

---

## 4. Canaux de Distribution

| Canal | Description | Priorité |
|---|---|---|
| **GitHub** | Dépôt public, README, documentation d'installation | Critique (P1) |
| **Site web** | Landing page, téléchargement, contact | Critique (P1) |
| **Partenaires MSP** | Canal indirect, revendeurs, intégrateurs | Fort (P2) |
| **Salons & Événements** | FIC, Les Assises de la Sécurité | Moyen (P2) |
| **Référencement ANSSI** | Liste d'outils recommandés | Moyen (P2) |
| **Cybermalveillance.gouv.fr** | Plateforme étatique de sensibilisation | Moyen (P2) |

---

## 5. Relations Client

| Type de relation | Description | Canal |
|---|---|---|
| **Self-service** | Documentation en ligne, GitHub issues, communauté | GitHub, site web |
| **Support payant** | Support prioritaire, tickets, accès direct | Email, portail client |
| **Accompagnement** | Audit sur site ou distanciel, formation | Direct, MSP partenaires |
| **Communauté** | Contributions open-source, feedback utilisateurs | GitHub, forums |

---

## 6. Flux de Revenus

### 6.1. Structure des revenus (Projections)

| Source de revenus | Année 1 | Année 2 | Année 3 |
|---|---|---|---|
| **Support & maintenance** | ~32 000 € | ~145 000 € | ~380 000 € |
| **Audits & conformité NIS2** | ~30 000 € | ~105 000 € | ~280 000 € |
| **Formations** | ~12 500 € | ~50 000 € | ~125 000 € |
| **Canal MSP (licences)** | ~9 600 € | ~38 400 € | ~96 000 € |
| **TOTAL CA ESTIMÉ** | **~84 000 €** | **~338 000 €** | **~881 000 €** |

### 6.2. Hypothèses de conversion

| Hypothèse | Valeur | Justification |
|---|---|---|
| Taux de conversion open-source → services | 3 à 5 % | Benchmark SaaS open-source |
| Panier moyen support | 280 €/mois | Prix compétitif pour PME |
| Panier moyen audit | 3 000 € | Prix journée audit NIS2 |
| Panier moyen formation | 2 500 €/groupe | Formation inter-entreprises |
| Nombre de déploiements cible An 1 | 500 | Objectif GitHub + MSP |
| Objectif clients support An 1 | 15 | Conversion 3 % |

---

## 7. Ressources Clés

| Ressource | Description | Nature |
|---|---|---|
| **Équipe technique** | Développeur senior (Python/FastAPI), Expert cyber | Humaine |
| **Code source** | Outil open-source, stack Python/FastAPI/HTML/CSS/JS | Intellectuelle |
| **Marque & Communauté** | Présence GitHub, notoriété, contributeurs | Intangible |
| **Documentation** | Guides d'installation, cas d'usage NIS2 | Intellectuelle |
| **Infrastructure** | Serveurs CI/CD, hébergement site web | Matérielle |

---

## 8. Activités Clés

| Activité | Description | Priorité |
|---|---|---|
| **Développement produit** | Maintien du code, nouvelles fonctionnalités, corrections | Critique (P1) |
| **Support client** | Assistance technique, résolution incidents | Critique (P1) |
| **Audit NIS2** | Missions de conformité chez les clients | Fort (P2) |
| **Formation** | Organisation sessions, supports pédagogiques | Fort (P2) |
| **Marketing & Communication** | Salons, référencements, contenu GitHub | Moyen (P2) |
| **Gestion partenaires** | Recrutement MSP, certification, support dédié | Moyen (P2) |

---

## 9. Partenariats Clés

| Partenaire | Rôle | Valeur apportée |
|---|---|---|
| **MSP / SSII** | Canal de distribution indirect | Diffusion à grande échelle, réseau client |
| **ANSSI** | Institutionnel, réglementaire | Crédibilité, référencement NIS2 |
| **Écoles & Formation** | Utilisateurs, ambassadeurs | Volume, marque employeur |
| **Prestataires Cloud** | Hébergement site web (future offre SaaS v2) | Infrastructure scalable |

---

## 10. Structure de Coûts

| Poste de charge | Nature | Niveau estimé | % du CA |
|---|---|---|---|
| **Salaires & charges équipe** | Fixe | Majeur (>60% des charges) | ~60-70% |
| **Infrastructure & CI/CD** | Variable | Faible à moyen | ~5-10% |
| **Outils dev & licences** | Fixe | Faible | ~2-5% |
| **Marketing & Salons** | Ponctuel | Moyen (Phase 1) | ~10-15% |
| **Frais juridiques** | Ponctuel | Faible | ~2-5% |

---

## 11. Analyse du Modèle

### 11.1. Forces du modèle

- **Barrière à l'entrée faible** : open-source permet adoption massive sans friction financière
- **Scalabilité** : services récurrents (support, MSP) générant revenus prévisibles
- **Alignement réglementaire** : NIS2 crée un marché captif de 15 000 entités en France
- **Coûts maîtrisés** : pas de frais de licence tierce, infrastructure légère on-premise

### 11.2. Risques du modèle

| Risque | Impact | Mitigation |
|---|---|---|
| Adoption open-source insuffisante | Élevé | Stratégie de contenu, présence FIC, partenariat ANSSI |
| Concurrence (Wazuh, PRTG) | Moyen | Différenciation interface web unifiée, UX, conformité NIS2 |
| Difficulté recrutement cyber | Élevé | Partenariats écoles, alternances, marque employeur |

---

## 12. Projections Financières

### 12.1. Compte de résultat simplifié (Année 1)

| Poste | Montant |
|---|---|
| **Chiffre d'Affaires** | **84 000 €** |
| Support (15 clients × 280€ × 8 mois) | 33 600 € |
| Audits (10 missions × 3 000€) | 30 000 € |
| Formations (5 groupes × 2 500€) | 12 500 € |
| MSP (2 partenaires × 400€ × 12 mois) | 9 600 € |
| **Charges d'exploitation** | **~70 000 €** |
| Salaires & charges (1 ETP + expert) | ~55 000 € |
| Infrastructure & outils | ~5 000 € |
| Marketing & salons | ~10 000 € |
| **Résultat d'exploitation** | **~14 000 €** |

### 12.2. Seuils de rentabilité

- **Point mort (break-even)** : ~300 déploiements actifs avec 3 % de conversion
- **Croissance** : +300 % de CA entre An 1 et An 2 (84k → 338k)
- **Objectif An 3** : 881 000 € (positionnement leader PME cyber France)

---

## 13. Conclusion

Le modèle open-core de BigBrowser répond à un gap de marché documenté :

1. **Un besoin urgent** : 15 000 entités françaises doivent se conformer à NIS2 d'ici 2027
2. **Un produit différencié** : aucun outil open-source n'unifie les 8 fonctionnalités dans une interface web
3. **Une monétisation pragmatique** : services de support, audit et formation adossés à un produit gratuit

La stratégie de **croissance par l'open-source** suivie d'une **monétisation par services** permet de constructed un modèle économique durable, scalable et aligné avec les contraintes budgétaires des PME françaises.

---

*Document établi en avril 2026 — Sources : Étude de marché, Feuille de cadrage, Cahier des charges*
