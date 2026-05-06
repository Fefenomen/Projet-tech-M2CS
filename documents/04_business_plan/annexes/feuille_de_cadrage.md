**FEUILLE DE CADRAGE DE PROJET**

**Outil de Supervision et d'Analyse Réseau**

**1. IDENTIFICATION DU PROJET**

|                            |                                          |
|----------------------------|------------------------------------------|
| **Nom du projet**          | Outil de Supervision et d'Analyse Réseau |
| **Porteur du projet**      | Équipe fondatrice (à préciser)           |
| **Chef de projet**         | À désigner                               |
| **Commanditaire**          | Équipe dirigeante                        |
| **Date de lancement**      | Avril 2026                               |
| **Date de fin visée (v1)** | Octobre 2026 (Phase 1 — 6 mois)          |
| **Budget prévisionnel**    | À valider — CA estimé an 1 : ~84 000 €   |
| **Confidentialité**        | Confidentiel — diffusion restreinte      |

**2. CONTEXTE ET JUSTIFICATION**

Le marché de la cybersécurité est en forte croissance, dépassant 250 milliards de dollars en 2025. En France, la directive NIS2 impose à plus de 15 000 entités la mise en place d'une supervision continue.

Les PME sont particulièrement vulnérables : elles représentent la majorité des victimes de cyberattaques tout en étant sous-équipées en solutions de supervision.

Il existe un écart majeur entre :

des outils open-source puissants mais complexes (CLI, fragmentés)
des solutions enterprise complètes mais inaccessibles financièrement

Ce projet vise à combler cet écart.

Notre solution occupe un espace vide entre les outils CLI gratuits et les solutions enterprise. Le programme France 2030 Cyber PME dispose d'une enveloppe de 100 millions d'euros pour accélérer la mise en conformité. 57 % des PME expriment un besoin d'outils de protection accessibles et intuitifs.

**3. OBJECTIFS DU PROJET**

**3.1 Objectif général**

Développer et commercialiser un outil open-source de supervision et d'analyse réseau, tout-en-un, accessible via une interface web, répondant aux exigences NIS2, et ciblant prioritairement les PME françaises.

**3.2 Objectifs spécifiques (SMART)**

|        |                                                                   |                      |                  |
|--------|-------------------------------------------------------------------|----------------------|------------------|
| **\#** | **Objectif**                                                      | **Indicateur**       | **Cible An 1**   |
| **O1** | Publier la v1.0 open-source sur GitHub avec les 8 fonctionnalités | Release GitHub live  | Mois 6           |
| **O2** | Générer des téléchargements et déploiements de l'outil            | Nbre de déploiements | 500 déploiements |
| **O3** | Convertir des utilisateurs en clients de support payant           | Clients actifs       | 15 clients       |
| **O4** | Réaliser les premières missions d'audit NIS2                      | Missions réalisées   | 10 missions      |
| **O5** | Atteindre le premier chiffre d'affaires consolidé                 | CA total             | ~84 000 €        |
| **O6** | Activer les 2 premiers partenariats MSP/SSII                      | Partenaires signés   | 2 MSP actifs     |

**4. PÉRIMÈTRE DU PROJET**

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>✅ DANS LE PÉRIMÈTRE</strong></td>
<td><strong>❌ HORS PÉRIMÈTRE (v1)</strong></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Scan de plages IP et découverte d'équipements</p></li>
<li><p>Détection de ports ouverts et services réseau</p></li>
<li><p>Capture et analyse du trafic réseau</p></li>
<li><p>Détection de comportements suspects (règles)</p></li>
<li><p>Système d'alertes configurables</p></li>
<li><p>Interface web unifiée (tableau de bord)</p></li>
<li><p>Export JSON et CSV des rapports</p></li>
<li><p>Déployable on-premise (sans cloud)</p></li>
<li><p>Services : support, audit NIS2, formation</p></li>
<li><p>Canal partenaires MSP/SSII</p></li>
</ul></td>
<td><ul>
<li><p>Modules IA/ML de détection comportementale (v2+)</p></li>
<li><p>Offre SaaS cloud hébergée (v2+)</p></li>
<li><p>Dashboard conformité NIS2 dédié (v2+)</p></li>
<li><p>Intégration native SIEM (CEF/LEEF) (v2+)</p></li>
<li><p>Certification SecNumCloud</p></li>
<li><p>Internationalisation (Belgique, Luxembourg)</p></li>
<li><p>API REST documentée complète (v2+)</p></li>
<li><p>Module scoring de risque IA (v2+)</p></li>
</ul></td>
</tr>
</tbody>
</table>

**5. LIVRABLES ATTENDUS**

|        |                               |                                           |              |                 |
|--------|-------------------------------|-------------------------------------------|--------------|-----------------|
| **\#** | **Livrable**                  | **Description**                           | **Échéance** | **Responsable** |
| **L1** | **Dépôt GitHub public v1.0**  | Code source, README, doc installation     | Mois 6       | Équipe dev      |
| **L2** | **Documentation utilisateur** | Guide d'installation, cas d'usage NIS2    | Mois 6       | Équipe dev      |
| **L3** | **Catalogue de services**     | Offres support, audit, formation, MSP     | Mois 4       | Commercial      |
| **L4** | **Site web & landing page**   | Présentation, téléchargement, contact     | Mois 5       | Marketing       |
| **L5** | **Rapports PME pilotes**      | REX documentés de 5 à 10 PME pilotes      | Mois 6       | Chef de projet  |
| **L6** | **Premiers contrats signés**  | Support, audit et/ou formation            | Mois 9       | Commercial      |
| **L7** | **Partenariats MSP signés**   | 2 MSP/SSII intégrés au réseau partenaires | Mois 12      | Commercial      |

**6. PLANNING MACRO**

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 30%" />
<col style="width: 22%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Phase</strong></td>
<td><strong>Activités clés</strong></td>
<td><strong>Période</strong></td>
<td><strong>Jalons</strong></td>
</tr>
<tr class="even">
<td><strong>Phase 1 — Lancement &amp; Traction</strong></td>
<td><ul>
<li><p>Développement et finalisation de la v1.0</p></li>
<li><p>Publication GitHub + documentation</p></li>
<li><p>5 à 10 PME pilotes (gratuit)</p></li>
<li><p>Participation FIC et Les Assises</p></li>
<li><p>Activation 2 premiers partenaires MSP</p></li>
</ul></td>
<td><strong>M1 → M6</strong></td>
<td><ul>
<li><p>Release v1.0 sur GitHub</p></li>
<li><p>500 déploiements visés</p></li>
<li><p>2 MSP partenaires</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Phase 2 — Monétisation</strong></td>
<td><ul>
<li><p>Lancement offre de support (Essentiel)</p></li>
<li><p>Premières missions d'audit NIS2</p></li>
<li><p>Programme certification partenaires MSP</p></li>
<li><p>Formation inter-entreprises</p></li>
<li><p>Catalogue achats publics</p></li>
</ul></td>
<td><strong>M6 → M18</strong></td>
<td><ul>
<li><p>15 clients support</p></li>
<li><p>10 missions d'audit</p></li>
<li><p>CA An 1 : ~84 000 €</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Phase 3 — Industrialisation</strong></td>
<td><ul>
<li><p>Modules premium (IA/ML, NIS2 dashboard)</p></li>
<li><p>Extension réseau MSP (20+ partenaires)</p></li>
<li><p>Exploration offre SaaS hébergée</p></li>
<li><p>Dossier France 2030 Cyber PME</p></li>
<li><p>Réflexion internationalisation (BE, LU)</p></li>
</ul></td>
<td><strong>M18 → M36</strong></td>
<td><ul>
<li><p>CA An 3 : ~881 000 €</p></li>
<li><p>20+ partenaires MSP</p></li>
<li><p>5 000 déploiements</p></li>
</ul></td>
</tr>
</tbody>
</table>

**7. ÉQUIPE PROJET ET PARTIES PRENANTES**

**7.1 Équipe cœur**

|                                         |                                       |                      |            |
|-----------------------------------------|---------------------------------------|----------------------|------------|
| **Rôle**                                | **Compétences requises**              | **Disponibilité**    | **Statut** |
| **Chef de projet / Product Owner**      | Gestion projet, vision produit, cyber | Temps plein          | À recruter |
| **Développeur senior (Python/FastAPI)** | Python, FastAPI, sécurité réseau      | Temps plein          | À recruter |
| **Expert cybersécurité réseau**         | NIS2, audit, IDS/IPS, Wireshark, Nmap | Partiel / prestation | À recruter |
| **Commercial / Business Developer**     | Vente B2B, partenariats, PME/MSP      | Partiel (Phase 1)    | À recruter |

**7.2 Parties prenantes**

|                              |                           |                                    |                          |
|------------------------------|---------------------------|------------------------------------|--------------------------|
| **Partie prenante**          | **Type**                  | **Intérêt**                        | **Niveau d'implication** |
| PME françaises (10–250 emp.) | Client cible prioritaire  | Conformité NIS2, visibilité réseau | Fort                     |
| MSP / SSII partenaires       | Canal indirect            | Différenciation offre, upsell      | Fort                     |
| ANSSI                        | Institutionnel            | Conformité réglementaire NIS2      | Moyen                    |
| Collectivités & hôpitaux     | Client secondaire         | Conformité NIS2, budget public     | Moyen                    |
| Établissements de formation  | Client tertiaire          | Outil pédagogique, TP cyber        | Moyen                    |
| Communauté GitHub            | Contributeurs open-source | Amélioration du code, notoriété    | Faible (Phase 1)         |

**8. BUDGET ET RESSOURCES**

**8.1 Structure de coûts**

|                                       |            |                            |
|---------------------------------------|------------|----------------------------|
| **Poste de charge**                   | **Nature** | **Niveau estimé**          |
| **Salaires & charges équipe**         | Fixe       | Majeur (\>60% des charges) |
| Infrastructure hébergement & CI/CD    | Variable   | Faible à moyen             |
| Outils dev & licences tierces         | Fixe       | Faible                     |
| Marketing, salons (FIC, Les Assises)  | Ponctuel   | Moyen (Phase 1)            |
| Frais juridiques (CGV, RGPD, licence) | Ponctuel   | Faible                     |

**8.2 Projections de revenus**

|                          |               |                |                |
|--------------------------|---------------|----------------|----------------|
| **Source de revenus**    | **An 1**      | **An 2**       | **An 3**       |
| Support & maintenance    | ~32 000 €     | ~145 000 €     | ~380 000 €     |
| Audits & conformité NIS2 | ~30 000 €     | ~105 000 €     | ~280 000 €     |
| Formations               | ~12 500 €     | ~50 000 €      | ~125 000 €     |
| Canal MSP (licences)     | ~9 600 €      | ~38 400 €      | ~96 000 €      |
| **TOTAL CA ESTIMÉ**      | **~84 000 €** | **~338 000 €** | **~881 000 €** |

**9. RISQUES ET PLAN DE MITIGATION**

|        |                                                      |                 |            |                                                                                                  |
|--------|------------------------------------------------------|-----------------|------------|--------------------------------------------------------------------------------------------------|
| **\#** | **Risque**                                           | **Probabilité** | **Impact** | **Mitigation**                                                                                   |
| **R1** | Adoption insuffisante de la version open-source      | **Élevée**      | **Élevé**  | Stratégie de contenu active, présence GitHub Trending, partenariat ANSSI, présence FIC           |
| **R2** | Concurrence des outils établis (Wazuh, PRTG)         | **Moyenne**     | **Moyen**  | Différenciation sur la complétude et l'UX — interface web unifiée couvrant des gaps non couverts |
| **R3** | Retard de transposition NIS2 en France               | **Moyenne**     | **Moyen**  | Réorienter le discours sur la valeur opérationnelle indépendamment de la réglementation          |
| **R4** | Difficulté à recruter des profils cyber expérimentés | **Élevée**      | **Élevé**  | Partenariats écoles, alternances, valorisation du projet open-source comme marque employeur      |
| **R5** | Faux positifs dégradant la crédibilité               | **Moyenne**     | **Moyen**  | Investissement QA, bêta-test sur réseaux variés, système de feedback utilisateur intégré         |
| **R6** | Consolidation marché (Cisco-Splunk) saturant les PME | **Faible**      | **Faible** | Positionnement prix et open-source structurellement hors de portée des géants — avantage durable |

**10. FACTEURS CRITIQUES DE SUCCÈS**

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>✅ Facteurs internes</strong></td>
<td><strong>🌍 Facteurs externes</strong></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Qualité et fiabilité du produit (zéro faux positif toléré)</p></li>
<li><p>Vitesse d'itération et réactivité aux retours terrain</p></li>
<li><p>Qualité de la documentation et de l'onboarding</p></li>
<li><p>Cohérence et stabilité de l'équipe sur la durée</p></li>
<li><p>Capacité à industrialiser les prestations de services</p></li>
</ul></td>
<td><ul>
<li><p>Maintien de la dynamique réglementaire NIS2</p></li>
<li><p>Croissance du marché PME cyber (+10 %/an)</p></li>
<li><p>Développement du réseau de partenaires MSP</p></li>
<li><p>Notoriété communautaire sur GitHub</p></li>
<li><p>Obtention du financement France 2030 Cyber PME</p></li>
</ul></td>
</tr>
</tbody>
</table>

**11. HYPOTHÈSES ET CONTRAINTES**

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>📋 Hypothèses retenues</strong></td>
<td><strong>⚠️ Contraintes identifiées</strong></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Taux de conversion open-source → services : 3 à 5 % (benchmark SaaS open-source)</p></li>
<li><p>Panier moyen support : 280 €/mois</p></li>
<li><p>Panier moyen audit : 3 000 €</p></li>
<li><p>Panier moyen formation : 2 500 €/groupe</p></li>
<li><p>NIS2 maintient son calendrier de conformité 2027</p></li>
<li><p>Stack technique : Python / FastAPI / HTML/CSS/JS</p></li>
</ul></td>
<td><ul>
<li><p>Licences open-source : GPLv2 ou Apache 2.0 (arbitrage juridique requis)</p></li>
<li><p>Conformité RGPD obligatoire pour les données collectées</p></li>
<li><p>Déploiement sans obligation de cloud (on-premise requis)</p></li>
<li><p>Ressources humaines limitées en phase de lancement</p></li>
<li><p>Absence de certification SecNumCloud en v1</p></li>
</ul></td>
</tr>
</tbody>
</table>

**12. DÉCISION ET VALIDATION**

|                |                           |                           |
|----------------|---------------------------|---------------------------|
| **Signataire** | **Fonction**              | **Visa / Date**           |
|                | Chef de projet            | Date : \_\_\_/\_\_\_/2026 |
|                | Commanditaire / Direction | Date : \_\_\_/\_\_\_/2026 |
|                | Responsable technique     | Date : \_\_\_/\_\_\_/2026 |

*Document vivant — à mettre à jour à chaque jalon de validation du projet. Version initiale : Avril 2026.*
