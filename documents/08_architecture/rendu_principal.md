# Architecture définitive — Outil de Supervision et d'Analyse Réseau (BigBrowser)

## 1. Statut du document

Ce document fixe l'architecture de référence du produit BigBrowser. Il traduit les exigences du cahier des charges en choix techniques, composants, flux, responsabilités et contraintes de démonstration.

Sauf décision explicite ultérieure, cette architecture est considérée comme l'architecture définitive de départ pour le développement de l'application.

Le document distingue volontairement deux niveaux :

- l'architecture produit cible ;
- l'architecture de démonstration Docker retenue pour le MVP et la validation produit.

Cette distinction est importante : l'architecture de démonstration simplifie le packaging afin de faciliter la validation, tandis que l'architecture logique conserve une séparation claire des responsabilités pour préparer les évolutions ultérieures.

## 2. Objectif

Ce document définit l'architecture cible du produit BigBrowser.

L'objectif est de concevoir un outil open-source de supervision et d'analyse réseau, accessible via une interface web, capable de :

- recevoir de la télémétrie depuis des agents (heartbeat & events) ;
- persister un inventaire d'actifs réseau et les événements collectés ;
- détecter des comportements suspects sur les endpoints supervisés ;
- générer des alertes actionnables depuis des règles de détection ;
- exposer une interface web d'analyse orientée PME (sans expertise CLI) ;
- produire des exports CSV et JSON exploitables comme preuves de conformité NIS2.

L'architecture doit rester :

- propre et défendable en revue projet ;
- réaliste pour un MVP livrable en Mois 6 ;
- extensible pour les itérations suivantes (IA/ML, SaaS, multi-tenant).

La qualité attendue n'est donc pas seulement technique. L'architecture doit pouvoir être expliquée, justifiée et reliée aux besoins produit : observation réseau, détection, alertes, exports, traçabilité et démonstration reproductible.

## 3. Stack cible

### Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Alembic

### Base de données

- PostgreSQL

### Traitements asynchrones

- Redis
- Celery

### Frontend

- Bootstrap (HTML/CSS/JS)
- Interface web intégrée au même conteneur que le backend pour le MVP
- Interface servie par le serveur SOC et accessible à l'Admin Sys

### Conteneurisation et démo

- Docker Compose
- Topologie de démonstration en 3 zones distinctes

### Topologie Docker retenue

- une zone `Attaquant (Docker)`
- une zone `Endpoints (Docker)`
- un conteneur `Docker Container SOC` (Frontend Bootstrap + Backend FastAPI + PostgreSQL + Celery/Redis)

## 4. Principes d'architecture

Les principes retenus sont les suivants :

- séparation claire entre les zones attaquant, endpoints supervisés et SOC ;
- les endpoints communiquent exclusivement avec le backend via un Agent HeartBeat authentifié ;
- l'Admin Sys accède uniquement au Frontend Bootstrap, sans interaction directe avec la base de données ;
- organisation par domaines fonctionnels côté backend ;
- logique métier centralisée dans le Backend FastAPI ;
- traitements lourds ou différés (scans, détection, exports) délégués à Celery/Redis en dehors du chemin synchrone ;
- traçabilité native des actions sensibles (connexions, exports, changements de statut) ;
- structure adaptée à une démonstration rapide, mais suffisamment propre pour évoluer ;
- simulation contrôlée de comportements suspects par l'Attaquant, sans embarquer de code destructeur réel ;
- interface Bootstrap orientée lisibilité opérationnelle, accessible sans expertise CLI.

## 5. Architecture logicielle

```text
[Attaquant (Docker)] ---------------------> [Endpoints (Docker)]
                                                      |
                                           Agent HeartBeat / Events
                                                      |
                                                      v
[Admin Sys / SOC] ----HTTP---> [Frontend Bootstrap] <-----> [Backend FastAPI]
                                                                    |
                                                    +---------------+---------------+
                                                    |               |               |
                                               [PostgreSQL]   [Celery Worker]  [Redis]
```

## 6. Lecture de l'architecture logicielle

- l'Attaquant génère du trafic ou des comportements suspects à destination des Endpoints Docker ;
- les Endpoints supervisés remontent de la télémétrie (Agent HeartBeat et events) vers le Backend FastAPI ;
- l'Admin Sys accède à l'interface via le Frontend Bootstrap, hébergé dans le Docker Container ;
- le Frontend Bootstrap communique exclusivement avec le Backend FastAPI local ;
- le Backend FastAPI orchestre la persistance (PostgreSQL), la file de tâches (Redis) et l'exécution des traitements asynchrones (Celery Worker) ;
- PostgreSQL, Redis et Celery restent logiquement séparés, mais sont embarqués dans le Docker Container SOC pour la démonstration.

Le choix d'embarquer plusieurs services dans un seul Docker Container est un choix de packaging MVP. Il simplifie la démonstration et la validation, sans remettre en cause la séparation logique entre Frontend, API, base de données, file de tâches et worker. En production, ces services pourraient être séparés dans des conteneurs distincts, mais cette séparation augmenterait inutilement la complexité du MVP.

## 7. Architecture réseau Docker

L'environnement de développement et de démonstration est organisé en trois zones :

1. une zone `Attaquant (Docker)` — génère les scénarios offensifs contrôlés ;
2. une zone `Endpoints (Docker)` — contient les hôtes supervisés (1 ou plusieurs) ;
3. un `Docker Container SOC` — centralise le Frontend Bootstrap, le Backend FastAPI, PostgreSQL, Redis et le Celery Worker.

```text
DOCKER HOST
  réseau interne : BBrowser_net

  [Attaquant (Docker)]
         |
         | trafic réseau / comportements suspects contrôlés
         v
  [Endpoints (Docker)]
    +-----------+  +-----------+
    | Endpoint1 |  | Endpoint2 |  ...
    +-----------+  +-----------+
         |
         | Agent HeartBeat + Events (HTTP / secret agent)
         v
  [Docker Container SOC]
    +---------------------+
    | Frontend Bootstrap  | <--- Admin Sys (HTTP)
    |                     |
    | Backend Fast API    |
    |                     |
    | PostgreSQL          |
    |                     |
    | Celery / Redis      |
    +---------------------+
```

### Rôles des zones de démonstration

#### Zone `Attaquant (Docker)`

Responsabilités :

- produire des scénarios de test offensifs contrôlés ;
- simuler des comportements suspects (scan de ports, tentatives répétées) ;
- générer du trafic observable à destination des Endpoints.

Contraintes :

- pas de charge destructive réelle ;
- pas de code malware réel ;
- scénarios strictement prévisibles, documentés et limités au réseau `BBrowser_net`.

#### Zone `Endpoints (Docker)`

Responsabilités :

- jouer le rôle des hôtes supervisés ;
- observer le trafic réseau sur leur interface Docker ;
- collecter et parser les fichiers log utiles ;
- relever les comportements suspects locaux (scan de ports, tentatives d'accès) ;
- remonter les `heartbeat` et `events` vers le Backend FastAPI.

#### `Docker Container SOC`

Le Docker Container SOC centralise tous les composants applicatifs pour le MVP.

Composants internes embarqués :

- **Frontend Bootstrap** — interface web servie à l'Admin Sys ;
- **Backend FastAPI** — API REST, orchestration des modules, gestion des règles de détection ;
- **PostgreSQL** — persistance de toutes les données fonctionnelles ;
- **Celery** — worker asynchrone pour les traitements différés ;
- **Redis** — broker de messages pour Celery.

## 8. Diagramme de séquence principal

```text
1. Attaquant          -> Endpoints          : trafic / comportements suspects contrôlés
2. Endpoint Agent     -> Backend FastAPI    : POST /telemetry/heartbeat (secret agent)
3. Backend FastAPI    -> PostgreSQL         : persistance du heartbeat
4. Endpoint Agent     -> Backend FastAPI    : POST /telemetry/events
5. Backend FastAPI    -> PostgreSQL         : persistance des événements
6. Backend FastAPI    -> Redis              : mise en file d'une tâche de détection
7. Redis              -> Celery Worker      : dispatch de la tâche
8. Celery Worker      -> PostgreSQL         : application des règles / création des alertes
9. Admin Sys          -> Frontend Bootstrap : navigation (HTTP)
10. Frontend Bootstrap -> Backend FastAPI   : requêtes REST (actifs, alertes, exports)
11. Backend FastAPI   -> PostgreSQL         : lecture des données
12. Backend FastAPI   -> Frontend Bootstrap : réponse JSON
```

## 9. Composants principaux

### 9.1 Agent de collecte (Endpoints)

Rôle :

- collecter des `heartbeat` à intervalles réguliers ;
- observer le trafic réseau sur l'interface du conteneur ;
- analyser des fichiers log ;
- relever des comportements suspects (tentatives de connexion, scans de ports) ;
- pousser les données vers le Backend FastAPI.

Contraintes :

- simple et robuste ;
- peu couplé au reste du système ;
- authentifié auprès de l'API par un secret d'agent dédié ;
- les droits réseau nécessaires (`NET_RAW`, `NET_ADMIN`) doivent être explicitement bornés au conteneur et documentés dans la configuration Docker.

### 9.2 Backend FastAPI

Rôle :

- authentifier les utilisateurs (Admin Sys) ;
- authentifier les agents de collecte (Endpoints) ;
- recevoir et valider les données agent (heartbeat, events) ;
- exposer les endpoints métiers (actifs, alertes, exports, audit) ;
- valider et normaliser les payloads via Pydantic ;
- appliquer les règles de détection ;
- piloter le worker Celery via Redis ;
- retourner les données au Frontend Bootstrap.

Les routes d'ingestion agent doivent être séparées des routes utilisateur. Elles acceptent uniquement des agents connus, via un secret ou une clé API stockée côté serveur. Cette séparation limite les confusions entre actions humaines et remontées automatiques, facilite l'audit et prépare un durcissement ultérieur.

### 9.3 Frontend Bootstrap

Rôle :

- exposer une interface web accessible à l'Admin Sys sans expertise CLI ;
- afficher un tableau de bord de supervision ;
- permettre la consultation des actifs, événements et alertes ;
- permettre la qualification et le changement de statut des alertes ;
- permettre la génération d'exports CSV et JSON ;
- afficher les journaux d'audit (profil `admin` uniquement).

Le Frontend Bootstrap est intégré dans le Docker Container SOC pour le MVP et ne communique qu'avec le Backend FastAPI local.

Le choix de Bootstrap garantit :

- une compatibilité maximale sans dépendance à un framework JS lourd ;
- une interface lisible et démontrable en conditions réalistes ;
- une facilité de maintenance pour l'équipe projet.

### 9.4 PostgreSQL

Rôle :

- stocker les utilisateurs et leurs rôles ;
- stocker les actifs réseau découverts ;
- stocker les événements remontés par les agents ;
- stocker les alertes générées ;
- stocker les journaux d'audit ;
- stocker les métadonnées d'exports.

PostgreSQL est la source de vérité fonctionnelle, embarquée dans le Docker Container SOC pour la phase MVP.

### 9.5 Redis + Worker Celery

Rôle :

- sortir du chemin synchrone les traitements non immédiats ;
- exécuter les règles de détection sur les événements entrants ;
- générer des alertes depuis les règles ;
- produire des exports CSV et JSON différés ;
- recalculer les indicateurs du tableau de bord.

Redis joue le rôle de broker de messages entre le Backend FastAPI et le Celery Worker. Ce découplage garantit que les scans, détections et exports n'impactent pas la réactivité de l'interface web.

Redis et Celery sont embarqués dans le Docker Container SOC pour la phase MVP.

## 10. Capacités fonctionnelles réseau imposées par le projet

L'architecture doit couvrir explicitement les capacités demandées :

- détection des équipements connectés sur la plage supervisée ;
- scan de plage IP ;
- identification des ports ouverts ;
- récupération d'informations sur les services réseau ;
- observation du trafic réseau depuis les Endpoints ;
- détection de comportements suspects (scan de ports, répétitions, tentatives d'accès) ;
- génération d'alertes actionnables depuis des règles simples.

Ces capacités seront portées principalement par les agents (Endpoints) et par les modules backend associés à la télémétrie, aux actifs et aux alertes.

Dans l'environnement Docker de démonstration, les scans et observations doivent rester limités au réseau `BBrowser_net`. Les capacités Linux nécessaires (`NET_RAW` ou `NET_ADMIN`) doivent être explicitement documentées dans la configuration Docker.

## 11. Découpage fonctionnel du backend

Le backend est organisé par domaines métier pour garantir la maintenabilité et la testabilité.

Modules recommandés :

- `auth`
- `telemetry`
- `discovery`
- `assets`
- `alerts`
- `reports`
- `audit`
- `core`

### `auth`

Responsabilités :

- login de l'Admin Sys ;
- génération et validation des tokens JWT ;
- endpoint `/me` ;
- gestion des rôles `admin` et `analyst`.

### `telemetry`

Responsabilités :

- réception des `heartbeat` depuis les agents Endpoints ;
- réception des `events` ;
- validation des payloads (Pydantic + regex sur les IPs) ;
- normalisation minimale avant persistance.

### `discovery`

Responsabilités :

- scan de plages IP configurées ;
- identification des ports ouverts ;
- récupération d'informations de services réseau ;
- collecte d'observations liées au trafic réseau ;
- transmission des résultats au module `assets` et au module `alerts`.

### `assets`

Responsabilités :

- création et mise à jour de l'inventaire d'actifs ;
- enrichissement de base des actifs (IP, ports, services, statut) ;
- consultation des actifs par le Frontend.

### `alerts`

Responsabilités :

- création d'alertes depuis les règles de détection ;
- consultation et détail des alertes ;
- gestion du cycle de vie des statuts (`nouvelle`, `en cours`, `clôturée`) ;
- qualification par l'Admin Sys.

### `reports`

Responsabilités :

- synthèse des indicateurs clés ;
- génération d'exports CSV ;
- génération d'exports JSON ;
- production de preuves exploitables pour la conformité NIS2.

### `audit`

Responsabilités :

- journalisation des actions sensibles (connexion, export, changement de statut, administration) ;
- conservation des traces ;
- consultation restreinte au profil `admin`.

### `core`

Responsabilités :

- configuration applicative ;
- sécurité transverse (middlewares, gestion des secrets) ;
- dépendances communes ;
- utilitaires partagés.

## 12. Structure logique FastAPI recommandée

```text
app/
  main.py
  core/
  auth/
  telemetry/
  discovery/
  assets/
  alerts/
  reports/
  audit/
```

Chaque module devrait à terme contenir :

- routes FastAPI ;
- schémas Pydantic ;
- services métier ;
- accès aux données (SQLAlchemy) ;
- tests associés.

## 13. Contrat API MVP

| Méthode | Endpoint | Usage | Accès |
|---|---|---|---|
| `POST` | `/auth/login` | Authentification Admin Sys | Public |
| `GET` | `/auth/me` | Informations utilisateur courant | `admin`, `analyst` |
| `GET` | `/health` | Santé applicative | Public |
| `POST` | `/telemetry/heartbeat` | Réception heartbeat agent | Agent authentifié |
| `POST` | `/telemetry/events` | Réception events agent | Agent authentifié |
| `POST` | `/scan` | Lancement d'un scan réseau | `admin` |
| `GET` | `/assets` | Liste des actifs | `admin`, `analyst` |
| `GET` | `/assets/{id}` | Détail d'un actif | `admin`, `analyst` |
| `GET` | `/alerts` | Liste des alertes | `admin`, `analyst` |
| `GET` | `/alerts/{id}` | Détail d'une alerte | `admin`, `analyst` |
| `PATCH` | `/alerts/{id}` | Qualification / changement de statut | `admin`, `analyst` |
| `POST` | `/exports` | Génération d'un export CSV/JSON | `admin`, `analyst` |
| `GET` | `/audit-logs` | Consultation des journaux d'audit | `admin` |

## 14. Flux de test en environnement Docker

Scénario de démonstration recommandé :

1. le Docker Container SOC, les Endpoints et l'Attaquant démarrent sur le réseau `BBrowser_net` ;
2. les Endpoints s'authentifient auprès du Backend FastAPI et émettent un `heartbeat` initial ;
3. les Endpoints exécutent une phase de découverte réseau initiale (scan IP, ports, services) ;
4. l'Attaquant déclenche un scénario contrôlé (scan de ports, tentatives répétées) ;
5. les Endpoints observent le trafic et les comportements attendus, puis remontent des `events` ;
6. le Backend FastAPI persiste les événements dans PostgreSQL ;
7. le Backend FastAPI pousse une tâche de détection dans Redis ;
8. le Celery Worker applique les règles de détection et crée les alertes dans PostgreSQL ;
9. l'Admin Sys se connecte via le Frontend Bootstrap et visualise les actifs, alertes et événements ;
10. l'Admin Sys génère un export CSV ou JSON comme preuve de conformité NIS2.

## 15. Modèle de données fonctionnel

Entités principales à prévoir :

- `users`
- `roles`
- `assets`
- `events`
- `network_findings`
- `alerts`
- `audit_logs`
- `exports`

Relations principales :

- un événement peut être lié à un actif ;
- un résultat de scan ou d'observation réseau peut être lié à un actif ;
- une alerte peut être liée à un actif et à un ou plusieurs événements ;
- une action utilisateur sensible doit produire une entrée d'audit.

### Champs minimaux

| Entité | Champs minimaux MVP |
|---|---|
| `users` | `id`, `username`, `password_hash`, `role`, `created_at`, `is_active` |
| `assets` | `id`, `ip_address`, `hostname`, `first_seen_at`, `last_seen_at`, `status` |
| `events` | `id`, `source_ip`, `target_ip`, `event_type`, `severity`, `message`, `created_at`, `asset_id` |
| `network_findings` | `id`, `asset_id`, `port`, `protocol`, `service_name`, `observed_at` |
| `alerts` | `id`, `title`, `severity`, `status`, `source_ip`, `description`, `created_at`, `updated_at` |
| `audit_logs` | `id`, `user_id`, `role`, `action`, `target_type`, `result`, `created_at` |
| `exports` | `id`, `format`, `requested_by`, `scope`, `file_path`, `created_at`, `row_count` |

## 16. Exigences non fonctionnelles

### Sécurité

- authentification obligatoire pour l'Admin Sys (JWT) ;
- séparation des rôles `admin` / `analyst` ;
- authentification obligatoire pour les agents Endpoints (secret d'agent) ;
- routes d'ingestion agent séparées des routes utilisateur ;
- validation stricte des entrées via Pydantic et regex (protection injection de commandes via champs IP) ;
- secrets non versionnés dans le dépôt GitHub ;
- journalisation des opérations critiques.

### Qualité

- structure modulaire par domaines fonctionnels ;
- validation stricte des données d'entrée ;
- logique métier testable ;
- conventions de nommage homogènes entre documentation, code et schéma SQL.

### Performance

- tableau de bord et vues principales : réponse en moins de 2 secondes sur jeu de données MVP ;
- scans et traitements lourds délégués au Celery Worker (interface non bloquée) ;
- export CSV ou JSON de 100 lignes généré en moins de 5 secondes.

### Observabilité

- endpoint de santé (`GET /health`) vérifiant API, base de données et worker ;
- logs applicatifs structurés pour les erreurs, ingestions, exports et actions sensibles ;
- métriques minimales exposées dans le tableau de bord : heartbeats reçus, événements ingérés, alertes générées, état du worker, volume d'exports.

### Déploiement

- environnement local reproductible via Docker Compose ;
- séparation nette entre configuration et code (variables d'environnement) ;
- capacité à démontrer l'application en conditions réalistes depuis un `docker compose up` ;
- réseau Docker dédié `BBrowser_net`, sans accès inutile hors du lab.

## 17. Interface web Bootstrap cible

L'interface web cible doit être accessible, lisible et orientée Admin Sys sans expertise CLI.

Elle doit privilégier la clarté opérationnelle : état du réseau supervisé, alertes récentes, actifs concernés et preuves disponibles.

Capacités attendues :

- tableau de bord synthétique avec métriques clés ;
- liste et détail des actifs réseau découverts ;
- liste et détail des alertes (avec filtres par statut et sévérité) ;
- qualification des alertes et changement de statut ;
- consultation des événements collectés ;
- génération d'exports CSV et JSON ;
- consultation des journaux d'audit (Admin uniquement).

## 18. MVP recommandé

Le premier incrément produit devrait couvrir :

1. authentification Admin Sys (JWT) ;
2. ingestion `heartbeat` depuis les Endpoints ;
3. ingestion `events` depuis les Endpoints ;
4. scan IP et identification des ports et services réseau ;
5. persistance PostgreSQL (actifs, events, alertes, audit) ;
6. inventaire d'actifs simple ;
7. règles de détection minimales (via Celery Worker) ;
8. liste et détail d'alertes avec cycle de vie ;
9. exports CSV et JSON ;
10. audit minimal (connexions, exports, changements de statut) ;
11. tableau de bord Bootstrap avec métriques et historique ;
12. lab Docker de démonstration : Attaquant + Endpoints + Docker Container SOC.

## 19. Architecture Docker retenue pour la démonstration

Architecture retenue :

| Zone | Contenu | Rôle |
|---|---|---|
| `Attaquant (Docker)` | Machine Docker offensive | Génère les scénarios de test contrôlés vers les Endpoints |
| `Endpoints (Docker)` | 1 ou plusieurs hôtes Docker | Supervisés, remontent heartbeat & events vers le Backend |
| `Docker Container SOC` | Frontend Bootstrap + Backend FastAPI + PostgreSQL + Celery + Redis | Centralise l'application, la base et les traitements |
| `Admin Sys (SOC)` | Poste administrateur | Accède au Frontend Bootstrap via HTTP |

Cette architecture est retenue comme architecture de test officielle du projet pour les phases de développement, de démonstration et de validation fonctionnelle.

## 20. Pourquoi cette architecture est adaptée au sujet

Cette architecture est adaptée parce qu'elle :

- correspond directement aux attendus du projet BigBrowser (supervision réseau PME, conformité NIS2) ;
- est cohérente avec la stack imposée Python / FastAPI / Bootstrap ;
- sépare correctement les responsabilités : attaquant, endpoints supervisés, SOC applicatif ;
- permet une démonstration claire et reproductible en validation produit ;
- reste assez simple pour un MVP livrable en Mois 6 ;
- prépare une montée en qualité sans complexité excessive (séparation logique des composants) ;
- couvre explicitement les besoins de scan, ports, services, trafic, détection et export NIS2 ;
- rend visible toute la chaîne : observation → heartbeat → détection → alerte → export de preuve.

## 21. Références documentaires

Cette architecture s'appuie sur les documents suivants :

- Feuille de cadrage projet (BigBrowser, v1.0, Avril 2026)
- Business Model (Open-Source + Services, Avril 2026)
- Cahier des charges BigBrowser (v1.0)
- Matrice de gestion des risques
- Étude de marché (Avril 2026)
- OWASP ASVS — Application Security Verification Standard
- Directive NIS2 (2022/2555)

## 22. Conclusion

L'architecture définitive retenue pour BigBrowser est une architecture web modulaire organisée en trois zones Docker (Attaquant, Endpoints, Docker Container SOC), centrée sur FastAPI, PostgreSQL, Redis et un worker Celery asynchrone, avec un frontend Bootstrap accessible à l'Admin Sys sans expertise CLI.

Elle traduit fidèlement le diagramme d'infrastructure retenu par l'équipe : l'Attaquant génère des scénarios contrôlés vers les Endpoints, les Endpoints remontent de la télémétrie (Agent HeartBeat & events) vers le Backend FastAPI, et l'Admin Sys accède à l'application via le Frontend Bootstrap hébergé dans le Docker Container SOC.

Elle est adaptée au sujet, défendable techniquement, exploitable opérationnellement et suffisamment propre pour servir de base définitive au développement du produit. Elle matérialise le compromis central du projet : produire une supervision réseau simple à déployer pour les PME, tout en conservant une conception rigoureuse pouvant être présentée dans un contexte professionnel ou de conformité NIS2.