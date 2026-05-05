# Cahier des charges — Outil de Supervision et d'Analyse Réseau (BigBrowser)

## 1. Objet du document

Le présent cahier des charges formalise les besoins, le périmètre, les contraintes, les exigences fonctionnelles et non fonctionnelles ainsi que les critères de validation du projet BigBrowser.

Il a une fonction contractuelle au sein du projet : il transforme les orientations de cadrage en exigences vérifiables, suffisamment précises pour guider le développement et suffisamment lisibles pour être défendues lors d'une revue projet. Il constitue également une base de dialogue entre les dimensions produit, projet et technique.

Ce document s'appuie sur :

- la feuille de cadrage projet (BigBrowser, v1.0, Avril 2026) ;
- le business model (Modèle Open-Source + Services, Avril 2026) ;
- la matrice de gestion des risques ;
- les tâches identifiées : étude de marché, business model, business plan, gestion de projet, stratégie de lancement.

### 1.1. Contexte quantifié (Mai 2026)

Les données collectées valident les exigences du cahier des charges :

- **250 milliards de dollars** — marché mondial de la cybersécurité en 2025, dont **6,4 milliards d'euros** en France.
- **75 % des cyberattaques françaises** ciblent des PME, alors que **60 % investissent moins de 1 000 €/an** en cybersécurité.
- **15 000 entités françaises** à mettre en conformité avec la directive NIS2 d'ici 2027 (supervision réseau obligatoire).
- **Aucun outil open-source** ne couvre les 8 fonctionnalités clés dans une interface web unifiée → gap concurrentiel structurel.
- **100 millions d'euros** disponibles via le programme France 2030 Cyber PME.

Ces chiffres justifient le périmètre MVP, la stratégie de lancement et les fonctionnalités demandées.

---

## 2. Fiche documentaire

| Élément | Valeur |
|---|---|
| Projet | Outil de Supervision et d'Analyse Réseau |
| Code projet | BigBrowser |
| Document | Cahier des charges fonctionnel et technique |
| Version | 1.0 |
| Statut | Version initiale — en cours de validation |
| Périmètre | Produit MVP open-source déployable on-premise |
| Public visé | Équipe projet, parties prenantes, contributeurs techniques, responsables de validation |
| Date de création | Avril 2026 |
| Sources | Feuille de cadrage, Business Model, Gestion des risques, Étude de marché |

### Historique des versions

| Version | Objet | Statut |
|---|---|---|
| 1.0 | Formalisation initiale du périmètre, des exigences et des critères d'acceptation | Référence initiale |

---

## 3. Résumé exécutif

BigBrowser est un outil open-source de supervision et d'analyse réseau, accessible via une interface web unifiée, ciblant prioritairement les PME françaises soumises à la directive NIS2.

Le produit adopte un modèle dit « open-core » : le cœur fonctionnel (8 fonctionnalités clés) est distribué gratuitement sous licence open-source, tandis que la valeur commerciale est créée autour de services à forte valeur ajoutée — support, audit de conformité NIS2, intégration et formation.

Le cahier des charges retient une logique de MVP démontrable. L'objectif n'est pas de reproduire la complexité d'un SIEM enterprise, mais de prouver une chaîne fonctionnelle complète : scan réseau, détection de comportements suspects, génération d'alertes, tableau de bord, historisation et export de preuve.

La réussite du produit sera évaluée sur sa capacité à être déployé on-premise, à produire des résultats observables et exploitables, et à démontrer une valeur immédiate pour une équipe IT sans expertise CLI.

---

## 4. Contexte et problématique

Le projet répond à deux niveaux d'attente :

- un besoin de démonstration produit, défini par le périmètre MVP et les critères de validation ;
- un besoin de valorisation commerciale, défini par le business model, le positionnement retenu et l'opportunité identifiée sur le marché.

Les organisations ciblées doivent pouvoir :

- découvrir et cartographier les équipements présents sur leur réseau ;
- observer le trafic et détecter les comportements suspects ;
- générer des alertes actionnables sans expertise CLI ;
- prouver leur conformité NIS2 via des rapports exportables ;
- déployer la solution on-premise, sans dépendance cloud.

La problématique peut être formulée ainsi : comment produire une visibilité cyber suffisamment riche pour être utile aux PME, tout en conservant une architecture simple, accessible et conforme aux exigences réglementaires NIS2 ?

---

## 5. Objectifs du produit

### Objectif général

Concevoir et distribuer un outil web de supervision réseau open-source capable de démontrer une chaîne fonctionnelle complète, depuis la découverte du réseau jusqu'à la production de preuves exportables, déployable on-premise sans expertise en ligne de commande.

### Objectifs opérationnels

| ID | Objectif | Indicateur | Cible An 1 |
|---|---|---|---|
| OBJ-001 | Publier la v1.0 open-source sur GitHub | Release GitHub live | Mois 6 |
| OBJ-002 | Générer des déploiements de l'outil | Nombre de déploiements | 500 |
| OBJ-003 | Convertir des utilisateurs en clients de support | Clients actifs | 15 |
| OBJ-004 | Réaliser les premières missions d'audit NIS2 | Missions réalisées | 10 |
| OBJ-005 | Atteindre le premier chiffre d'affaires consolidé | CA total An 1 | ~84 000 € |
| OBJ-006 | Activer les premiers partenariats MSP/SSII | Partenaires signés | 2 MSP actifs |

---

## 6. Périmètre du MVP

### 6.1. Fonctions incluses

- authentification utilisateur ;
- gestion des rôles ;
- scan de plages IP et découverte d'équipements réseau ;
- détection de ports ouverts et services réseau ;
- capture et analyse du trafic réseau ;
- détection de comportements suspects (règles) ;
- système d'alertes configurables ;
- interface web unifiée (tableau de bord) ;
- historisation et journalisation des événements ;
- exports JSON et CSV des rapports ;
- métriques de supervision.

### 6.2. Fonctions hors périmètre initial

- modules IA/ML de détection comportementale (v2+) ;
- offre SaaS cloud hébergée (v2+) ;
- dashboard conformité NIS2 dédié (v2+) ;
- intégration native SIEM (CEF/LEEF) (v2+) ;
- certification SecNumCloud ;
- internationalisation (Belgique, Luxembourg) ;
- API REST documentée complète (v2+) ;
- module scoring de risque IA (v2+).

Cette exclusion constitue un choix de maîtrise. Le périmètre initial se concentre sur les fonctionnalités qui démontrent le mieux la valeur du projet dans le temps disponible.

### 6.3. Règles de priorisation

| Priorité | Signification | Règle de décision |
|---|---|---|
| P1 | Indispensable MVP | Doit être livré pour considérer la chaîne produit conforme |
| P2 | Fortement souhaitable | Peut être livré si les fonctions P1 sont stables, sans bloquer la conformité MVP |
| P3 | Extension | Peut être reporté sans remettre en cause la conformité MVP |

---

## 7. Parties prenantes et utilisateurs

### 7.1. Parties prenantes

| Partie prenante | Rôle dans le projet | Attentes principales |
|---|---|---|
| Équipe projet | Conception, développement, documentation et démonstration | Périmètre clair, architecture défendable, livrables cohérents |
| Responsables de validation | Évaluation de la conformité du produit aux exigences | Traçabilité, cohérence, résultats observables |
| PME françaises (10–250 emp.) | Client cible prioritaire | Conformité NIS2, visibilité réseau, simplicité de déploiement |
| MSP / SSII partenaires | Canal de distribution indirect | Différenciation offre, upsell, intégration dans leur offre |
| ANSSI | Institutionnel | Conformité réglementaire NIS2 |
| Collectivités & hôpitaux | Client secondaire | Conformité NIS2, budget public |
| Communauté GitHub | Contributeurs open-source | Amélioration du code, notoriété |

### 7.2. Utilisateurs cibles

| Profil | Description | Besoins principaux |
|---|---|---|
| Administrateur | Responsable de la configuration et des accès | Authentifier, gérer les rôles, consulter l'état du système |
| Analyste / Admin réseau | Chargé de la supervision et de la qualification des alertes | Voir les équipements, événements, alertes et exports |
| DSI / Responsable IT PME | Décideur sans expertise CLI | Tableau de bord lisible, rapports exportables, preuve de conformité NIS2 |
| MSP partenaire | Gère plusieurs clients PME en multi-tenant | Supervision centralisée, rapports clients, revente de services |

### 7.3. Matrice des permissions MVP

| Fonction | `admin` | `analyst` | Non authentifié |
|---|---:|---:|---:|
| Se connecter à l'interface | Oui | Oui | Non |
| Consulter le tableau de bord | Oui | Oui | Non |
| Lancer un scan réseau | Oui | Non | Non |
| Consulter les équipements et alertes | Oui | Oui | Non |
| Qualifier une alerte ou changer son statut | Oui | Oui | Non |
| Générer un export CSV/JSON | Oui | Oui | Non |
| Consulter les journaux d'audit | Oui | Non | Non |
| Administrer les utilisateurs ou rôles | Oui | Non | Non |

Toute route non explicitement publique doit refuser les accès non authentifiés.

---

## 8. Glossaire

| Terme | Définition |
|---|---|
| Actif | Équipement, hôte ou ressource réseau observable par le système |
| Alerte | Signal produit par une règle de détection ou par une corrélation |
| Audit log | Journal retraçant une action sensible ou significative |
| MVP | Minimum Viable Product, version minimale démontrable du produit |
| NIS2 | Directive européenne sur la sécurité des réseaux et des systèmes d'information |
| On-premise | Déploiement local sans dépendance à une infrastructure cloud |
| Open-core | Modèle où le cœur fonctionnel est open-source et les revenus sont générés par des services |
| MSP | Managed Service Provider, prestataire gérant l'informatique de plusieurs clients PME |
| SIEM | Security Information and Event Management |
| Faux positif | Alerte générée à tort sur un comportement légitime |
| Port ouvert | Port réseau accessible et exposé sur un équipement |
| Trafic réseau | Ensemble des communications transitant sur le réseau supervisé |

---

## 9. Hypothèses, contraintes et dépendances

### 9.1. Hypothèses

- Le marché PME cyber croît à +10 %/an, avec un catalyseur réglementaire NIS2 fort.
- Le taux de conversion open-source → services est estimé à 3–5 % (benchmark SaaS open-source).
- Les PME cibles disposent d'une infrastructure on-premise et ne souhaitent pas de dépendance cloud en v1.
- La stack technique Python / FastAPI / HTML/CSS/JS est imposée par les contraintes projet.
- Les scénarios de détection sont basés sur des règles simples (pas d'IA/ML en v1).

### 9.2. Contraintes

- backend Python / FastAPI imposé ;
- frontend web cohérent avec la démonstration ;
- dépôt GitHub structuré et documenté ;
- architecture défendable techniquement ;
- déploiement on-premise (sans obligation de cloud) ;
- conformité RGPD obligatoire pour les données collectées ;
- licence open-source : GPLv2 ou Apache 2.0 (arbitrage juridique requis) ;
- livrables exploitables en revue projet ;
- respect d'un calendrier de 9 jours pour les 15 tâches MVP (contrainte forte — risque rupture de planning).

### 9.3. Dépendances documentaires

- Feuille de cadrage projet (BigBrowser, v1.0)
- Business Model (Open-Source + Services, Avril 2026)
- Matrice de gestion des risques
- Étude de marché (Avril 2026)
- Business plan

---

## 10. Exigences fonctionnelles

Les exigences fonctionnelles décrivent ce que le produit doit faire. Elles sont numérotées afin de faciliter la traçabilité avec les critères d'acceptation et les scénarios de recette.

### 10.1. Règles métier MVP

| ID | Règle | Description | Critère de vérification |
|---|---|---|---|
| RM-001 | Authentification utilisateur | Un utilisateur doit disposer d'un identifiant, d'un mot de passe stocké sous forme hachée et d'un rôle. | Un accès sans session valide est refusé. |
| RM-002 | Scan borné | Tout scan réseau doit être limité à la plage IP configurée. | Un scan hors plage autorisée est refusé ou ignoré. |
| RM-003 | Détection de ports | Les ports ouverts détectés sur un équipement doivent être associés à l'actif correspondant. | Le résultat de scan est consultable dans le détail de l'actif. |
| RM-004 | Détection de comportements suspects | Au moins trois tentatives similaires depuis une même IP doivent produire une alerte. | Le scénario de test contrôlé génère une alerte. |
| RM-005 | Statuts d'alerte | Une alerte doit au minimum supporter les statuts `nouvelle`, `en cours` et `clôturée`. | Le statut est visible et modifiable par un utilisateur autorisé. |
| RM-006 | Preuve exportable | Un export doit contenir les données du scénario, une date de génération, un format et un identifiant de demande. | Le fichier CSV/JSON permet de retrouver le scénario joué. |
| RM-007 | Audit obligatoire | Connexion, export, changement de statut d'alerte et action d'administration doivent produire une entrée d'audit. | Chaque action sensible apparaît dans les journaux d'audit. |
| RM-008 | Validation des entrées | Tout champ de saisie (plage IP, filtre, formulaire) doit être validé strictement côté serveur via Pydantic et regex. | Un payload invalide est rejeté proprement, sans erreur non contrôlée. |

### 10.2. Authentification et contrôle d'accès

| ID | Exigence | Priorité | Critère d'acceptation |
|---|---|---|---|
| F-AUTH-001 | Le système doit permettre l'authentification sécurisée des utilisateurs. | P1 | Un utilisateur valide accède au tableau de bord après connexion. |
| F-AUTH-002 | Le système doit distinguer les rôles `admin` et `analyst`. | P1 | Les permissions diffèrent selon le rôle. |
| F-AUTH-003 | Le système doit restreindre les actions sensibles selon le rôle. | P1 | Un analyste ne peut pas exécuter une action réservée à l'administration. |

### 10.3. Découverte réseau et inventaire des actifs

| ID | Exigence | Priorité | Critère d'acceptation |
|---|---|---|---|
| F-DISC-001 | Le système doit scanner une plage IP définie par l'utilisateur. | P1 | Une plage IP configurée est analysée et les actifs créés ou mis à jour. |
| F-DISC-002 | Le système doit identifier les équipements observables. | P1 | Au moins un actif est créé avec son adresse IP et son statut. |
| F-DISC-003 | Le système doit détecter les ports ouverts. | P1 | Les ports détectés sont associés à l'actif correspondant. |
| F-DISC-004 | Le système doit récupérer des informations de services quand elles sont disponibles. | P2 | Les services observés apparaissent dans le détail d'un actif. |
| F-ASSET-001 | Le système doit maintenir un inventaire d'actifs consultable. | P1 | L'interface affiche la liste et le détail des actifs connus. |

### 10.4. Capture et analyse du trafic réseau

| ID | Exigence | Priorité | Critère d'acceptation |
|---|---|---|---|
| F-TRAF-001 | Le système doit capturer des flux réseau sur l'interface configurée. | P1 | Des captures de trafic sont disponibles dans l'interface. |
| F-TRAF-002 | Le système doit permettre le filtrage du trafic capturé. | P2 | L'utilisateur peut filtrer par IP, port ou protocole. |

### 10.5. Détection et alerting

| ID | Exigence | Priorité | Critère d'acceptation |
|---|---|---|---|
| F-ALERT-001 | Le système doit produire des alertes issues de règles simples. | P1 | Un comportement suspect génère une alerte. |
| F-ALERT-002 | Le système doit proposer une vue de liste des alertes. | P1 | Les alertes sont consultables dans l'interface. |
| F-ALERT-003 | Le système doit proposer une vue de détail d'une alerte. | P1 | Une alerte affiche son contexte, sa source et son horodatage. |
| F-ALERT-004 | Le système doit gérer un cycle de vie minimal des alertes. | P1 | Une alerte peut changer de statut ou être qualifiée. |
| F-ALERT-005 | Le système doit permettre la configuration des règles d'alerte. | P2 | Un administrateur peut ajuster les seuils de détection. |

### 10.6. Interface web

| ID | Exigence | Priorité | Critère d'acceptation |
|---|---|---|---|
| F-UI-001 | L'interface doit proposer un tableau de bord de synthèse. | P1 | Le tableau de bord affiche les métriques clés. |
| F-UI-002 | L'interface doit permettre la consultation des actifs. | P1 | La liste et le détail des actifs sont accessibles. |
| F-UI-003 | L'interface doit permettre la consultation des alertes. | P1 | Les alertes générées sont visibles et filtrables. |
| F-UI-004 | L'interface doit permettre la consultation du trafic capturé. | P1 | Les flux réseau capturés sont visualisables. |
| F-UI-005 | L'interface doit permettre la consultation des journaux d'audit. | P2 | Les actions sensibles journalisées sont consultables par `admin`. |

### 10.7. Reporting et exports

| ID | Exigence | Priorité | Critère d'acceptation |
|---|---|---|---|
| F-EXP-001 | Le système doit produire un export CSV. | P1 | Un fichier CSV est généré avec les colonnes obligatoires définies en section 13. |
| F-EXP-002 | Le système doit produire un export JSON. | P1 | Un fichier JSON est généré avec les métadonnées obligatoires. |
| F-EXP-003 | Les exports doivent servir de preuve opérationnelle de conformité NIS2. | P1 | L'export contient des données cohérentes avec le scénario joué. |
| F-EXP-004 | Les exports doivent être accessibles uniquement aux utilisateurs autorisés. | P1 | Un utilisateur non autorisé ne peut pas générer ou consulter un export. |

### 10.8. Audit et journalisation

| ID | Exigence | Priorité | Critère d'acceptation |
|---|---|---|---|
| F-AUD-001 | Le système doit journaliser les authentifications. | P1 | Une connexion génère une entrée d'audit. |
| F-AUD-002 | Le système doit journaliser les exports. | P1 | Un export génère une entrée d'audit. |
| F-AUD-003 | Le système doit journaliser les actions sensibles d'administration. | P1 | Une action sensible est traçable. |
| F-AUD-004 | Les journaux doivent être consultables par un profil autorisé. | P2 | Un administrateur consulte les journaux d'audit. |

---

## 11. Exigences non fonctionnelles

| ID | Catégorie | Exigence | Priorité | Critère d'acceptation |
|---|---|---|---|---|
| NF-QUAL-001 | Qualité | Le code doit être structuré par domaines fonctionnels. | P1 | La structure suit les modules définis dans l'architecture. |
| NF-QUAL-002 | Qualité | Les données d'entrée doivent être validées via Pydantic et regex. | P1 | Un payload invalide est rejeté proprement sans erreur non contrôlée. |
| NF-PERF-001 | Performance | Le tableau de bord et les vues principales doivent répondre en moins de 2 secondes. | P1 | Mesuré sur un jeu de données MVP représentatif. |
| NF-PERF-002 | Performance | Les traitements lourds (scan, capture) doivent être différés et asynchrones. | P1 | L'interface reste disponible pendant un scan en cours. |
| NF-PERF-003 | Performance | Un export CSV ou JSON de 100 lignes doit être généré en moins de 5 secondes. | P1 | Mesuré pendant la démonstration. |
| NF-OBS-001 | Observabilité | Le système doit exposer un endpoint de santé. | P1 | `GET /health` retourne un statut API et base de données consultable. |
| NF-OBS-002 | Observabilité | Le système doit produire des logs applicatifs exploitables. | P1 | Les erreurs, scans, exports et actions sensibles sont visibles dans les logs. |
| NF-DEP-001 | Déployabilité | Le projet doit être déployable on-premise sans infrastructure cloud. | P1 | La documentation d'installation permet un déploiement autonome. |
| NF-DEP-002 | Déployabilité | Le projet doit être disponible sur GitHub avec README et documentation d'installation. | P1 | Le dépôt est public, documenté et reproductible. |
| NF-MAINT-001 | Maintenabilité | Les conventions de nommage doivent rester cohérentes. | P1 | Les noms de modules, entités et endpoints sont homogènes. |
| NF-TEST-001 | Testabilité | Chaque exigence P1 doit être reliée à au moins un scénario de recette. | P1 | La matrice de traçabilité couvre les exigences P1. |

---

## 12. Exigences de sécurité

Les exigences de sécurité s'inspirent de bonnes pratiques applicatives (OWASP ASVS) et intègrent les risques identifiés dans la matrice de gestion des risques.

| ID | Exigence | Priorité | Critère d'acceptation |
|---|---|---|---|
| SEC-001 | L'accès à l'interface doit nécessiter une authentification. | P1 | Une page protégée n'est pas accessible sans session valide. |
| SEC-002 | Les actions sensibles doivent être contrôlées par rôle. | P1 | Un `analyst` ne peut pas effectuer une action réservée à `admin`. |
| SEC-003 | Les champs de saisie (plage IP, filtres) doivent être validés strictement via Pydantic et regex. | P1 | Une injection de commande dans un champ IP est bloquée. |
| SEC-004 | Les exports doivent être chiffrés ou contrôlés en accès local. | P1 | Un utilisateur non autorisé ne peut pas accéder aux fichiers exportés. |
| SEC-005 | Les secrets ne doivent pas être exposés dans le dépôt. | P1 | Aucun secret réel n'est versionné dans le dépôt GitHub. |
| SEC-006 | Les actions sensibles doivent produire une entrée d'audit. | P1 | Les connexions, exports et actions d'administration sont tracés. |
| SEC-007 | Les scans doivent être limités à la plage IP configurée par l'administrateur. | P1 | Aucun scan ne cible une IP hors de la plage autorisée. |
| SEC-008 | Les requêtes réseau de scan doivent inclure des délais pour éviter le bannissement IDS. | P2 | Des délais inter-requêtes sont configurables (scans furtifs). |

---

## 13. Données manipulées

| Donnée | Description | Source | Usage | Sensibilité |
|---|---|---|---|---|
| `users` | Comptes utilisateurs de l'application | Interface / initialisation | Authentification et contrôle d'accès | Élevée |
| `roles` | Rôles applicatifs (`admin`, `analyst`) | Configuration applicative | Autorisations | Élevée |
| `assets` | Actifs réseau découverts | Scan réseau | Inventaire et analyse | Moyenne |
| `ports` | Ports ouverts détectés sur les actifs | Scan réseau | Inventaire et détection | Moyenne |
| `services` | Services réseau identifiés | Scan réseau | Inventaire actifs | Moyenne |
| `traffic_captures` | Flux réseau capturés | Module capture trafic | Analyse et détection | Moyenne |
| `alerts` | Alertes générées par règles | Backend | Investigation analyste | Moyenne |
| `audit_logs` | Traces d'actions sensibles | API | Traçabilité et preuve | Élevée |
| `exports` | Fichiers ou métadonnées d'exports | Module reporting | Preuve et conformité NIS2 | Moyenne |

### 13.1. Champs minimaux attendus

| Entité | Champs minimaux MVP |
|---|---|
| `users` | `id`, `username`, `password_hash`, `role`, `created_at`, `is_active` |
| `assets` | `id`, `ip_address`, `hostname`, `first_seen_at`, `last_seen_at`, `status` |
| `ports` | `id`, `asset_id`, `port`, `protocol`, `state`, `observed_at` |
| `alerts` | `id`, `title`, `severity`, `status`, `source_ip`, `description`, `created_at`, `updated_at` |
| `audit_logs` | `id`, `user_id`, `role`, `action`, `target_type`, `result`, `created_at` |
| `exports` | `id`, `format`, `requested_by`, `scope`, `file_path`, `created_at`, `row_count` |

### 13.2. Formats de données MVP

#### Export CSV minimal

Colonnes obligatoires : `export_id`, `generated_at`, `type`, `id`, `source_ip`, `severity`, `status`, `created_at`, `description`.

#### Export JSON minimal

```json
{
  "export_id": "exp_001",
  "generated_at": "2026-04-01T10:05:00Z",
  "format": "json",
  "scope": "alerts",
  "items": []
}
```

---

## 14. Interfaces, API et flux

### 14.1. Flux principaux

| Flux | Source | Destination | Description |
|---|---|---|---|
| FLUX-001 | Module scan | Réseau supervisé | Scan de plage IP, détection d'actifs et ports |
| FLUX-002 | Module capture | Interface réseau | Capture et analyse du trafic |
| FLUX-003 | Interface web | API FastAPI | Consultation des actifs, alertes, exports |
| FLUX-004 | API FastAPI | Base de données | Persistance et lecture des données |
| FLUX-005 | API FastAPI | Worker asynchrone | Planification des scans et traitements différés |
| FLUX-006 | Worker | Base de données | Création ou mise à jour des alertes et actifs |

### 14.2. Contrat API MVP

| Méthode | Endpoint MVP | Usage | Accès | Priorité |
|---|---|---|---|---|
| `POST` | `/auth/login` | Authentification utilisateur | Public | P1 |
| `GET` | `/auth/me` | Informations utilisateur courant | `admin`, `analyst` | P1 |
| `GET` | `/health` | Santé applicative | Public | P1 |
| `POST` | `/scan` | Lancement d'un scan réseau | `admin` | P1 |
| `GET` | `/assets` | Liste des actifs | `admin`, `analyst` | P1 |
| `GET` | `/assets/{id}` | Détail d'un actif | `admin`, `analyst` | P1 |
| `GET` | `/alerts` | Liste des alertes | `admin`, `analyst` | P1 |
| `GET` | `/alerts/{id}` | Détail d'une alerte | `admin`, `analyst` | P1 |
| `PATCH` | `/alerts/{id}` | Qualification ou changement de statut | `admin`, `analyst` | P2 |
| `GET` | `/traffic` | Consultation du trafic capturé | `admin`, `analyst` | P1 |
| `POST` | `/exports` | Génération d'un export CSV/JSON | `admin`, `analyst` | P1 |
| `GET` | `/audit-logs` | Consultation des journaux d'audit | `admin` | P2 |

---

## 15. Architecture de démonstration retenue

La stack technique retenue est Python / FastAPI / HTML/CSS/JS, déployable on-premise, sans infrastructure cloud obligatoire. L'architecture est organisée autour de modules fonctionnels indépendants communicant via l'API.

### 15.1. CompBigBrowser l'architecture MVP

| CompBigBrowserôle |
|---|---|
| Frontend web | Interface utilisateur (tableau de bord, alertes, actifs, exports) |
| Backend FastAPI | API REST, gestion des routes, orchestration des modules |
| Module scan réseau | Scan IP, détection d'actifs, ports et services |
| Module capture trafic | Capture et analyse des flux réseau |
| Module détection | Règles de détection, génération d'alertes |
| Module reporting | Génération d'exports CSV et JSON |
| Base de données | Persistance des actifs, alertes, journaux et exports |
| Worker asynchrone | Traitements différés (scans, exports, détection) |

### 15.2. Conditions minimales de lancement

| Élément | Condition attendue |
|---|---|
| Backend FastAPI | API démarrée et `GET /health` opérationnel |
| Base de données | Connectée et schéma initialisé |
| Worker asynchrone | Démarré et capable de traiter des tâches de scan |
| Compte admin | Compte administrateur créé à l'initialisation |
| Réseau cible | Plage IP configurée et accessible depuis le serveur |

### 15.3. Limites de sécurité

- les scans doivent rester limités à la plage IP configurée par l'administrateur ;
- aucun exploit actif, malware ou trafic destructeur ne doit être intégré ;
- les secrets (clés API, mots de passe) ne doivent pas être versionnés dans le dépôt GitHub ;
- la conformité RGPD est obligatoire pour les données collectées sur les réseaux clients.

---

## 16. Scénarios de recette et critères d'acceptation

### 16.1. Critères d'acceptation globaux

Le produit sera considéré comme conforme si les points suivants sont démontrés :

1. un utilisateur peut s'authentifier avec son rôle et accéder aux fonctions correspondantes ;
2. le système découvre des actifs et ports sur une plage IP configurée ;
3. des comportements suspects génèrent des alertes consultables dans l'interface ;
4. le cycle de vie d'une alerte peut être géré (statut, qualification) ;
5. un export CSV et JSON exploitable est généré depuis l'interface ;
6. les actions sensibles sont journalisées et consultables ;
7. la démonstration est reproductible depuis la documentation d'installation.

### 16.2. Scénarios de recette

| ID | Scénario | Préconditions | Étapes | Résultat attendu | Preuve attendue |
|---|---|---|---|---|---|
| REC-001 | Connexion utilisateur | Compte `admin` et compte `analyst` créés | Se connecter avec un compte valide, puis tenter d'accéder sans session | Connexion valide acceptée, accès sans session refusé | Capture tableau de bord, réponse de refus, entrée audit |
| REC-002 | Contrôle des permissions | Compte `analyst` connecté | Tenter d'accéder aux journaux d'audit ou lancer un scan | Accès refusé pour `analyst`, autorisé pour `admin` | Réponse API ou capture interface |
| REC-003 | Scan réseau borné | Plage IP configurée, réseau accessible | Lancer un scan depuis l'interface | Actifs, ports et services détectés dans la plage autorisée | Vue actifs, résultat de scan |
| REC-004 | Détection comportement suspect | Règles de détection actives | Générer trois tentatives similaires depuis une même IP | Événement suspect puis alerte créée | Vue alerte, événement source, log worker |
| REC-005 | Cycle de vie alerte | Alerte existante, utilisateur connecté | Passer l'alerte de `nouvelle` à `en cours`, puis `clôturée` | Statut mis à jour et action auditée | Vue alerte et entrée `audit_logs` |
| REC-006 | Export preuve CSV/JSON | Alertes ou actifs présents | Générer un export CSV puis JSON depuis l'interface ou l'API | Fichier généré avec métadonnées et données cohérentes | Fichier exporté et entrée `audit_logs` |
| REC-007 | Validation injection IP | Interface de scan accessible | Saisir une valeur invalide dans le champ de plage IP | Requête rejetée proprement, aucun scan lancé | Réponse d'erreur contrôlée |
| REC-008 | Latence interface | Données de démonstration chargées | Naviguer entre les vues tableau de bord, actifs et alertes | Chaque vue répond en moins de 2 secondes | Mesure de temps de réponse |
| REC-009 | Santé et déployabilité | Application démarrée | Vérifier les compBigBrowserppeler `GET /health`, rejouer le scénario complet | API, base et worker opérationnels | Réponse `/health`, démonstration complète |
| REC-010 | Démonstration complète | REC-001 à REC-009 réalisables | Jouer scan → détection → alerte → export | Chaîne complète visible et explicable | Captures, logs, export CSV/JSON |

---

## 17. Priorisation

### Priorité 1 — indispensable

- authentification et gestion des rôles ;
- scan réseau et découverte des actifs ;
- détection de comportements suspects et génération d'alertes ;
- cycle de vie des alertes ;
- export CSV et JSON ;
- audit minimal (connexions, exports, actions sensibles) ;
- tableau de bord et vues principales.

### Priorité 2 — fortement souhaitable

- configuration des règles d'alerte et des seuils ;
- capture et filtrage du trafic réseau ;
- consultation des journaux d'audit par l'administrateur ;
- scans furtifs avec délais inter-requêtes.

### Priorité 3 — extension si temps disponible

- dashboard conformité NIS2 dédié ;
- modules IA/ML de détection comportementale ;
- offre SaaS hébergée ;
- API REST documentée complète (v2) ;
- internationalisation.

---

## 18. Gestion des risques

La matrice ci-dessous reprend les risques identifiés et leur niveau de criticité (Probabilité × Impact, échelle 1–5).

| ID | Risque | P | I | Criticité | Stratégie de mitigation |
|---|---|---|---|---|---|
| R-T01 | **Faux positifs** dégradant la crédibilité | 4 | 3 | **12** | Ajustement fin des seuils de détection, bêta-test sur réseaux variés, feedback utilisateur intégré |
| R-T02 | **Blocage par IDS** tiers lors du scan | 3 | 4 | **12** | Délais inter-requêtes configurables, scans furtifs (SYN scans) |
| R-T03 | **Latence UI** bloquant l'interface pendant un scan | 3 | 3 | **9** | Traitement asynchrone des tâches via worker FastAPI |
| R-S01 | **Injection de commandes** via les champs de scan IP | 2 | 5 | **10** | Validation stricte Pydantic + regex sur toutes les entrées |
| R-S02 | **Exposition de données** lors des exports | 2 | 4 | **8** | Chiffrement des exports, contrôle d'accès local |
| R-P01 | **Rupture de planning** (9 jours, 15 tâches) | 4 | 5 | **20** | Priorisation stricte MVP, travail parallèle Front/Back, suivi quotidien |
| R-P02 | **Conflits Git** lors des fusions de branches | 3 | 4 | **12** | Workflow Git Flow (branches par fonctionnalité) et Pull Requests |
| R-P03 | **Défaut de preuve** en démonstration | 2 | 5 | **10** | Environnement de test virtualisé (Docker) garantissant la reproductibilité |
| R-M01 | **Adoption insuffisante** de la version open-source | 4 | 4 | **16** | Stratégie de contenu active, présence GitHub Trending, partenariat ANSSI, FIC |
| R-M02 | **Concurrence** des outils établis (Wazuh, PRTG) | 3 | 3 | **9** | Différenciation sur la complétude UX et l'interface web unifiée |
| R-M03 | **Difficulté à recruter** des profils cyber expérimentés | 4 | 4 | **16** | Partenariats écoles, alternances, projet open-source comme marque employeur |

---

## 19. Matrice de traçabilité

| Besoin initial | Exigences associées | Recette | Preuve attendue |
|---|---|---|---|
| Sécuriser l'accès | F-AUTH-001, F-AUTH-002, F-AUTH-003, SEC-001, SEC-002 | REC-001, REC-002 | Test connexion, refus d'accès, audit log |
| Découvrir les équipements réseau | F-DISC-001, F-DISC-002, F-DISC-003, F-ASSET-001 | REC-003 | Vue actifs, résultat de scan |
| Détecter des comportements suspects | F-ALERT-001, F-ALERT-002, F-ALERT-003 | REC-004 | Vue alerte, événement source |
| Qualifier les alertes | F-ALERT-004, F-AUD-003 | REC-005 | Statut alerte et audit log |
| Produire des preuves NIS2 | F-EXP-001, F-EXP-002, F-EXP-003, F-AUD-002 | REC-006 | Fichier CSV/JSON, métadonnées export, audit log |
| Sécuriser les entrées | SEC-003, RM-008 | REC-007 | Réponse d'erreur contrôlée |
| Garantir la performance | NF-PERF-001, NF-PERF-003 | REC-008 | Mesure de temps de réponse |
| Démontrer le produit | NF-DEP-001, NF-DEP-002, NF-OBS-001 | REC-009, REC-010 | `/health`, chaîne complète, déploiement documenté |

---

## 20. Livrables attendus

| Livrable | Description | Critère de validation |
|---|---|---|
| Application BigBrowser MVP | Outil web de supervision réseau open-source | Chaîne fonctionnelle démontrable |
| Dépôt GitHub public v1.0 | Code source, README, documentation d'installation | Dépôt propre, documenté et reproductible |
| Documentation utilisateur | Guide d'installation, cas d'usage NIS2 | Permet un déploiement autonome |
| Catalogue de services | Offres support, audit NIS2, formation, MSP | Prêt pour la phase de monétisation (Mois 6) |
| Site web & landing page | Présentation, téléchargement, contact | En ligne pour le lancement GitHub |
| Exports de preuve | Fichiers CSV et JSON de démonstration | Exploitables en revue produit |
| Rapports PME pilotes | REX documentés de 5 à 10 PME pilotes | Validés et signés par les pilotes |
| Premiers contrats signés | Support, audit et/ou formation | À partir du Mois 9 |

---

## 21. Stratégie de lancement (Go-to-Market)

La stratégie de lancement est organisée en trois phases, alignées avec le business model retenu.

### Phase 1 — Lancement & Traction (Mois 1–6)

- Publication sur GitHub avec README complet, documentation d'installation et cas d'usage NIS2.
- Référencement sur les plateformes communautaires : ANSSI, Cybermalveillance.gouv.fr, forums SSI.
- Participation au FIC (Forum International de la Cybersécurité) et aux Assises de la Sécurité.
- Démarche auprès de 5 à 10 PME pilotes pour déploiement gratuit contre retour d'expérience documenté.
- Activation de 2 premiers partenaires MSP pour tests d'intégration dans leur offre.

**Jalons** : Release v1.0 sur GitHub — 500 déploiements visés — 2 MSP partenaires.

### Phase 2 — Monétisation (Mois 6–18)

- Lancement de l'offre de support (pack Essentiel en priorité) auprès des pilotes convertis.
- Premières missions d'audit NIS2 sur la base du réseau MSP partenaires.
- Mise en place d'un programme de certification partenaires (MSP labellisés).
- Lancement des premières formations inter-entreprises.

**Jalons** : 15 clients support — 10 missions d'audit — CA An 1 : ~84 000 €.

### Phase 3 — Industrialisation (Mois 18–36)

- Développement de modules premium (IA/ML, scoring, dashboard NIS2 dédié).
- Extension du réseau MSP à 20+ partenaires actifs.
- Exploration d'une offre SaaS hébergée.
- Dépôt de dossier France 2030 Cyber PME (enveloppe de 100 M€ disponible).

**Jalons** : CA An 3 : ~881 000 € — 20+ partenaires MSP — 5 000 déploiements.

---

## 22. Références de cadrage

- Feuille de cadrage projet (BigBrowser, v1.0, Avril 2026)
- Business Model (Open-Source + Services, Avril 2026)
- Matrice de gestion des risques
- Étude de marché (Avril 2026)
- ANSSI — Rapport d'activité 2024
- Directive NIS2 (2022/2555) — Transposition France 2027
- OWASP ASVS — Application Security Verification Standard
- France 2030 Cyber PME — Enveloppe 100 M€
- Mordor Intelligence, PAC, OPIIEC, Gartner — Données marché

---

## 23. Conclusion

Ce cahier des charges fixe un périmètre clair, vérifiable et cohérent avec le positionnement produit, le business model retenu et les exigences réglementaires NIS2.

Il formalise les exigences fonctionnelles et non fonctionnelles du MVP, les critères d'acceptation, les règles métier, les contrats API, les formats de données, la matrice de traçabilité, les scénarios de recette et les exigences de sécurité, adaptés au contexte d'un outil open-source de supervision réseau ciblant les PME françaises.

La version détaillée permet de relier explicitement le besoin initial, la conception technique, la stratégie commerciale et les preuves attendues en validation produit — depuis la publication open-source jusqu'aux premières missions d'audit NIS2 et au chiffre d'affaires cible de 84 000 € à l'issue de la première année.