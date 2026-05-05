# Architecture Technique — BigBrowser

> Outil de Supervision et d'Analyse Réseau · Avril 2026

---

## Table des matières

**Partie I — Architecture générale**

1. [Statut du document](#1-statut-du-document)
2. [Objectif](#2-objectif)
3. [Stack cible](#3-stack-cible)
4. [Principes d'architecture](#4-principes-darchitecture)
5. [Architecture logicielle](#5-architecture-logicielle)
6. [Lecture de l'architecture logicielle](#6-lecture-de-larchitecture-logicielle)
7. [Architecture réseau Docker](#7-architecture-réseau-docker)
8. [Diagramme de séquence principal](#8-diagramme-de-séquence-principal)
9. [Composants principaux](#9-composants-principaux)
10. [Capacités fonctionnelles réseau imposées par le projet](#10-capacités-fonctionnelles-réseau-imposées-par-le-projet)
11. [Découpage fonctionnel du backend](#11-découpage-fonctionnel-du-backend)

**Partie II — Détail technique**

12. [Structure logique FastAPI recommandée](#12-structure-logique-fastapi-recommandée)
13. [Mécanique de corrélation retenue](#13-mécanique-de-corrélation-retenue)
14. [Flux de test en environnement Docker](#14-flux-de-test-en-environnement-docker)
15. [Modèle de données fonctionnel](#15-modèle-de-données-fonctionnel)
16. [Exigences non fonctionnelles](#16-exigences-non-fonctionnelles)

**Partie III — Démonstration**

17. [Interface web cible](#17-interface-web-cible)
18. [MVP recommandé](#18-mvp-recommandé)
19. [Architecture Docker retenue pour la démonstration](#19-architecture-docker-retenue-pour-la-démonstration)
20. [Pourquoi cette architecture est adaptée au sujet](#20-pourquoi-cette-architecture-est-adaptée-au-sujet)

---

## 1. Statut du document

| Champ | Valeur |
|---|---|
| **Projet** | BigBrowser — Outil de Supervision et d'Analyse Réseau |
| **Version** | 1.0 |
| **Date** | Avril 2026 |
| **Statut** | Document de référence technique — v1 |
| **Audience** | Équipe technique, contributeurs open-source, partenaires MSP/SSII |
| **Confidentialité** | Confidentiel — diffusion restreinte |
| **Licence** | GPLv2 ou Apache 2.0 (arbitrage juridique en cours) |
| **Basé sur** | Feuille de cadrage projet, Business Model, Étude de marché, Schéma d'architecture v1 |

Ce document décrit l'architecture technique complète de BigBrowser pour sa version 1 (v1.0, cible : octobre 2026). Il constitue la référence de conception pour l'équipe de développement et sert de base aux décisions techniques structurantes. Il sera mis à jour à chaque jalon majeur du projet.

---

## 2. Objectif

BigBrowser est une plateforme de **supervision et d'analyse réseau open-source**, conçue pour offrir une visibilité complète sur un réseau d'entreprise via une interface web unifiée.

**Problème adressé :** Il existe un gap structurel entre les outils open-source puissants mais fragmentés et accessibles uniquement en CLI (Nmap, Wireshark, Suricata, Zeek), et les solutions enterprise complètes mais financièrement inaccessibles pour les PME (Splunk, Microsoft Sentinel, Palo Alto). Aucun outil du marché ne couvre les 8 fonctionnalités clés dans une interface web unifiée, déployable on-premise, à coût nul de licence.

**Objectif technique de la v1.0 :**

Livrer une plateforme opérationnelle couvrant les 8 capacités suivantes dans une interface web unique :

1. Scan de plages IP et découverte d'équipements
2. Détection de ports ouverts
3. Identification des services réseau
4. Capture et analyse du trafic réseau
5. Détection de comportements suspects (règles)
6. Système d'alertes configurables
7. Interface web unifiée (tableau de bord)
8. Export JSON et CSV des rapports

**Contexte réglementaire :** La directive NIS2 (en vigueur depuis octobre 2024) impose une supervision continue des systèmes d'information à plus de 15 000 entités françaises d'ici 2027. BigBrowser est conçu pour répondre directement à cette obligation.

---

## 3. Stack cible

| Couche | Technologie | Version cible | Justification |
|---|---|---|---|
| Langage principal | Python | 3.11+ | Écosystème réseau/sécurité riche (Scapy, python-nmap, Celery) |
| Framework web backend | FastAPI | 0.110+ | Asynchrone natif, OpenAPI auto, Pydantic |
| ORM | SQLAlchemy | 2.x | Abstraction BDD, migrations Alembic |
| Validation données | Pydantic | 2.x | Typage strict des modèles API |
| Frontend | Bootstrap | 5.x + JS vanilla | Légèreté, accessibilité, pas de dépendance JS lourde |
| Base de données | PostgreSQL | 15+ | JSONB, robustesse, open-source |
| Queue de tâches | Celery | 5.x | Tâches longues asynchrones (scans, capture) |
| Broker de messages | Redis | 7.x | Broker Celery + cache in-memory |
| Scan réseau | Nmap (subprocess) | 7.94+ | Référence secteur, NSE scripts |
| Capture réseau | Scapy / tcpdump | Latest | Analyse de paquets en Python natif |
| Conteneurisation | Docker + Compose | Latest | Déploiement reproductible on-premise |
| Reverse proxy | Nginx | 1.25+ | Sert le frontend statique, proxy vers FastAPI |
| Tests | pytest + httpx | Latest | Tests unitaires et d'intégration API |
| CI/CD | GitHub Actions | — | Pipeline automatisé : test → build → release |

---

## 4. Principes d'architecture

L'architecture de BigBrowser repose sur **cinq principes directeurs** non négociables pour la v1 :

**1. Déployable on-premise, sans cloud obligatoire**
La solution doit fonctionner sur n'importe quelle machine Linux disposant de Docker, sans dépendance à un service cloud tiers. Ce principe est fondamental pour les PME soucieuses de leur souveraineté des données et pour la conformité RGPD (les données collectées sur le réseau client ne quittent pas leur infrastructure).

**2. Interface web first — zéro CLI pour l'utilisateur final**
L'administrateur réseau d'une PME ne doit pas avoir à ouvrir un terminal pour utiliser BigBrowser. Toutes les opérations (lancement d'un scan, consultation des alertes, export de rapport) sont accessibles depuis le navigateur. La CLI reste disponible pour les contributeurs et les cas avancés, mais n'est jamais imposée à l'utilisateur.

**3. Architecture API-first**
Le backend expose une API REST complète (FastAPI + OpenAPI). Le frontend est un consommateur de cette API comme n'importe quel client externe. Ce principe garantit la séparation des responsabilités, facilite les tests automatisés, et prépare les intégrations futures (SDK, SIEM, portail MSP).

**4. Traitement asynchrone des tâches longues**
Les opérations réseau (scans Nmap, captures de trafic, corrélation d'événements) sont par nature longues et bloquantes. Elles sont systématiquement déléguées à des workers Celery via Redis, laissant FastAPI réactif pour l'interface utilisateur. Aucune opération de plus de 2 secondes ne s'exécute dans le thread principal de FastAPI.

**5. Modèle open-core évolutif**
Le cœur fonctionnel est distribué gratuitement sous licence open-source. L'architecture est conçue pour accueillir des modules premium (IA/ML, dashboard NIS2, multi-tenant MSP) en extension, sans refactoring du cœur. Les frontières entre le noyau open-source et les extensions futures sont explicitement documentées.

---

## 5. Architecture logicielle

L'architecture logicielle de BigBrowser suit le patron **N-tiers avec séparation stricte des couches** :

![Capture d'écran de mon projet](08_architecture/assets/schema_d'architecture.png)

---

## 6. Lecture de l'architecture logicielle

L'architecture se lit en **quatre couches verticales** qui communiquent de manière strictement descendante :

**Couche Présentation (Frontend Bootstrap / Nginx)**
Point d'entrée unique pour l'utilisateur humain. Le frontend est un ensemble de fichiers statiques (HTML/CSS/JS) servis par Nginx. Il ne contient aucune logique métier : il affiche les données reçues de l'API et envoie les actions de l'utilisateur au backend via des requêtes HTTP/JSON. La communication est exclusivement initiée par le navigateur client (architecture pull pour les données, sauf alertes temps réel).

**Couche Application (Backend FastAPI)**
Cerveau de la plateforme. FastAPI reçoit les requêtes du frontend, applique la logique métier (validation, autorisation, orchestration), interroge la base de données via SQLAlchemy, et délègue les tâches longues à Celery. C'est la seule couche autorisée à écrire dans PostgreSQL. Elle expose également les endpoints de réception des HeartBeats des agents.

**Couche Données (PostgreSQL)**
Source de vérité unique de la plateforme. Toutes les données collectées (équipements, ports, trafic, alertes, rapports) sont persistées ici. La base est accessible uniquement par le backend FastAPI et les workers Celery — jamais directement depuis le frontend ou l'extérieur du réseau Docker.

**Couche Traitement Asynchrone (Celery + Redis)**
Moteur d'exécution des opérations longues. Redis joue le rôle de broker (transport des messages entre FastAPI et les workers) et de backend de résultats (stockage temporaire des états de tâches). Les workers Celery s'exécutent dans des processus indépendants et écrivent leurs résultats directement en base PostgreSQL, sans repasser par FastAPI.

**Flux de lecture :** Une requête utilisateur (ex : lancer un scan) entre par le frontend → est reçue par FastAPI → enqueue une tâche Celery via Redis → le worker exécute le scan → persiste les résultats en base → FastAPI les expose à la prochaine requête du frontend.

---

## 7. Architecture réseau Docker

L'ensemble de BigBrowser s'exécute dans un environnement Docker isolé, organisé en deux réseaux logiques distincts :

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         HOST MACHINE (Linux)                                │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                    docker network: bigbrowser_internal               │   │
│  │                    (bridge, non exposé à l'extérieur)                │   │
│  │                                                                      │   │
│  │    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    │   │
│  │    │  backend  │    │    db    │    │  redis   │    │  worker  │    │   │
│  │    │  :8000   │◀──▶│  :5432   │    │  :6379   │◀──▶│ (celery) │    │   │
│  │    └────┬─────┘    └──────────┘    └──────────┘    └──────────┘    │   │
│  │         │                                                            │   │
│  └─────────┼──────────────────────────────────────────────────────────┘   │
│            │                                                                │
│  ┌─────────▼──────────────────────────────────────────────────────────┐    │
│  │                    docker network: bigbrowser_sim                   │    │
│  │                    (réseau de simulation — macvlan ou bridge)       │    │
│  │                                                                     │    │
│  │    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐   │    │
│  │    │ frontend  │    │ endpoint1│    │ endpoint2│    │attaquant │   │    │
│  │    │ nginx:80  │    │ (cible)  │    │ (cible)  │    │          │   │    │
│  │    └──────────┘    └──────────┘    └──────────┘    └──────────┘   │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  Ports exposés à l'hôte :  80 (Nginx/Frontend)  ·  8000 (FastAPI, dev)    │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Réseau `bigbrowser_internal` :** Réseau privé isolé pour la communication entre les services applicatifs (backend, base de données, Redis, workers). Aucun port de ce réseau n'est exposé directement à l'hôte en production.

**Réseau `bigbrowser_sim` :** Réseau de simulation qui contient les endpoints cibles et l'attaquant. Le backend dispose d'une interface sur ce réseau pour effectuer les scans et capturer le trafic. Ce découpage reproduit fidèlement la topologie d'un vrai réseau d'entreprise supervisé.

**Exposition externe :** Seul le port 80 (Nginx) est exposé à l'extérieur. Le port 8000 (FastAPI) peut être exposé en mode développement mais est masqué derrière Nginx en production.

---

## 8. Diagramme de séquence principal

Le diagramme ci-dessous représente le flux complet depuis le déclenchement d'un scan par l'administrateur jusqu'à l'affichage de l'alerte et l'export du rapport.

```
Admin          Frontend        FastAPI         Redis          Celery Worker   PostgreSQL
  │                │               │              │                 │              │
  │──POST /scan───▶│               │              │                 │              │
  │                │──POST /scans──▶│              │                 │              │
  │                │               │─enqueue task─▶│                │              │
  │                │               │◀─task_id──────│                │              │
  │                │◀──202 Accepted─│              │                 │              │
  │                │               │              │─consume task────▶│             │
  │                │               │              │                 │─nmap scan────▶(réseau)
  │                │               │              │                 │◀─résultats───│
  │                │               │              │                 │─write hosts──▶│
  │                │               │              │                 │─write ports──▶│
  │                │               │              │                 │─correlate    │
  │                │               │              │                 │  [si suspect] │
  │                │               │              │                 │─write alert──▶│
  │                │               │              │◀─task done──────│               │
  │                │──GET /scans/{id}▶│            │                │               │
  │                │               │─query──────────────────────────────────────────▶│
  │                │               │◀─results───────────────────────────────────────│
  │                │◀──200 + data───│              │                │               │
  │◀──Dashboard────│               │              │                │               │
  │                │               │              │                │               │
  │──Export CSV────▶│              │              │                │               │
  │                │──POST /reports─▶│            │                │               │
  │                │               │─enqueue──────▶│              │               │
  │                │               │              │─consume────────▶│             │
  │                │               │              │                │─query all────▶│
  │                │               │              │                │◀─data─────────│
  │                │               │              │                │─generate CSV  │
  │                │               │◀─done──────────────────────────│               │
  │                │◀──200 + file───│              │               │               │
  │◀──Téléchargement│              │              │                │               │
```

---

## 9. Composants principaux

### 9.1 Backend — FastAPI

Le backend est le **point d'orchestration central** de BigBrowser. Il reçoit toutes les requêtes du frontend, valide les données entrantes via Pydantic, applique la logique métier, et délègue les opérations lourdes à Celery.

| Responsabilité | Détail |
|---|---|
| API REST | Expose les endpoints HTTP/JSON consommés par le frontend et les agents |
| Scan réseau | Orchestre les scans IP via Nmap (subprocess ou python-nmap) |
| Analyse de ports | Détecte les ports ouverts et services réseau sur chaque hôte |
| Capture trafic | Déclenche et arrête les captures de paquets via Scapy/tcpdump |
| Détection | Applique des règles sur les événements collectés (seuils, patterns) |
| Gestion des alertes | Génère, persiste et expose les alertes |
| Export | Produit les rapports JSON et CSV |
| HeartBeat | Reçoit et enregistre les signaux de vie des agents endpoints |
| Auth | Gère l'authentification des utilisateurs (JWT ou session) |

### 9.2 Frontend — Bootstrap

Interface web accessible depuis n'importe quel navigateur, sans installation côté client. Construit en HTML5/CSS3/JavaScript + Bootstrap 5, servi par Nginx.

| Module UI | Description |
|---|---|
| Tableau de bord | Vue synthétique : équipements actifs, alertes en cours, derniers scans |
| Carte réseau | Visualisation des hôtes découverts et de leurs relations (vis.js ou D3.js) |
| Détail hôte | Ports ouverts, services, historique des scans, statut HeartBeat |
| Alertes | Liste triée par sévérité, filtres, statuts (nouvelle / en cours / résolue) |
| Rapports | Génération et téléchargement JSON/CSV, historique des exports |
| Configuration | Plages IP, planification des scans, règles d'alerte, seuils |

### 9.3 PostgreSQL

Source de vérité unique. Toutes les données collectées sont persistées ici avec horodatage complet pour assurer la traçabilité exigée par NIS2.

### 9.4 Celery + Redis

Moteur de traitement asynchrone. Redis joue le rôle de broker de messages et de backend de résultats. Celery gère les workers qui exécutent les scans, captures et corrélations en arrière-plan.

### 9.5 Agent HeartBeat

Composant léger déployé sur les endpoints supervisés. Envoie un signal HTTP périodique au backend pour signaler que la machine est en ligne. Une absence de signal au-delà d'un seuil configurable déclenche une alerte automatique.

### 9.6 Conteneur Attaquant

Conteneur Docker dédié à la **simulation d'adversaire** en environnement de démonstration et de formation. Génère des comportements réseau suspects (scans de ports, tentatives de brute-force, trafic anormal) pour valider les capacités de détection de BigBrowser.

### 9.7 Nginx

Reverse proxy qui sert les fichiers statiques du frontend et proxyfie les requêtes API vers FastAPI. Point d'entrée unique exposé sur le port 80/443.

---

## 10. Capacités fonctionnelles réseau imposées par le projet

Les 8 fonctionnalités du périmètre v1 imposent des **capacités techniques réseau spécifiques** que l'architecture doit garantir :

| Fonctionnalité | Capacité réseau requise | Composant technique | Contrainte |
|---|---|---|---|
| Scan de plages IP | Émission de paquets ICMP et TCP sur le sous-réseau cible | Nmap (subprocess) | Accès réseau niveau 3, pas de firewall bloquant ICMP |
| Découverte d'équipements | Résolution ARP et DNS inverse | Nmap (`-sn`) | Accès au même segment réseau (L2/L3) |
| Détection de ports ouverts | Scan TCP SYN (half-open) ou TCP connect | Nmap (`-sS` ou `-sT`) | Privileges root pour SYN scan |
| Identification des services | Probe des banners applicatifs | Nmap NSE (`-sV`) | Connexion TCP effective aux ports ouverts |
| Capture de trafic | Mode promiscuous sur l'interface réseau | Scapy / tcpdump | Interface en mode promiscuous, accès raw socket |
| Analyse de trafic | Décodage des protocoles (IP, TCP, UDP, HTTP…) | Scapy | Accès aux paquets bruts |
| Détection de comportements suspects | Corrélation d'événements en temps quasi-réel | Celery worker + règles Python | Flux continu d'événements depuis la capture |
| Export JSON/CSV | Aucune contrainte réseau spécifique | FastAPI + Celery | Accès en lecture à PostgreSQL |

**Note sur les privilèges :** Les opérations de scan SYN et de capture en mode promiscuous nécessitent des **privilèges root** (ou `CAP_NET_RAW` + `CAP_NET_ADMIN` en Docker). Le conteneur backend doit être lancé avec ces capabilities dans le `docker-compose.yml`.

```yaml
# Extrait docker-compose.yml
services:
  backend:
    cap_add:
      - NET_RAW
      - NET_ADMIN
    network_mode: "host"   # ou réseau macvlan selon la configuration
```

---

## 11. Découpage fonctionnel du backend

Le backend FastAPI est organisé en **modules fonctionnels** correspondant aux grandes capacités de la plateforme. Chaque module est autonome et expose ses propres routes, services et modèles.

| Module | Routes API principales | Responsabilité |
|---|---|---|
| `scan` | `POST /scans`, `GET /scans`, `GET /scans/{id}` | Lancement et suivi des scans réseau |
| `hosts` | `GET /hosts`, `GET /hosts/{id}`, `DELETE /hosts/{id}` | Gestion des équipements découverts |
| `ports` | `GET /hosts/{id}/ports`, `GET /ports` | Consultation des ports et services |
| `traffic` | `POST /capture/start`, `POST /capture/stop`, `GET /traffic` | Gestion des captures de trafic |
| `alerts` | `GET /alerts`, `GET /alerts/{id}`, `PATCH /alerts/{id}` | Consultation et gestion des alertes |
| `rules` | `GET /rules`, `POST /rules`, `DELETE /rules/{id}` | Gestion des règles de détection |
| `reports` | `POST /reports`, `GET /reports/{id}`, `GET /reports/{id}/download` | Génération et export des rapports |
| `heartbeat` | `POST /heartbeat` | Réception des signaux d'agents |
| `config` | `GET /config`, `PATCH /config` | Configuration des plages IP et paramètres |
| `auth` | `POST /auth/login`, `POST /auth/logout`, `GET /auth/me` | Authentification et gestion des sessions |

---

## 12. Structure logique FastAPI recommandée

La structure de fichiers recommandée pour le projet suit les conventions FastAPI avec une séparation claire entre routes, services, modèles et tâches :

```
bigbrowser/
├── main.py                          # Point d'entrée FastAPI, enregistrement des routers
├── config.py                        # Variables d'environnement (pydantic-settings)
├── database.py                      # Connexion SQLAlchemy, session factory
│
├── api/                             # Couche API (routes uniquement, pas de logique)
│   ├── __init__.py
│   ├── deps.py                      # Dépendances injectées (auth, db session)
│   └── routers/
│       ├── scans.py
│       ├── hosts.py
│       ├── ports.py
│       ├── traffic.py
│       ├── alerts.py
│       ├── rules.py
│       ├── reports.py
│       ├── heartbeat.py
│       ├── config.py
│       └── auth.py
│
├── services/                        # Logique métier (appelée par les routers)
│   ├── scan_service.py              # Orchestration Nmap, parsing résultats
│   ├── traffic_service.py           # Gestion des captures Scapy/tcpdump
│   ├── detection_service.py         # Application des règles de détection
│   ├── alert_service.py             # Génération et gestion des alertes
│   ├── report_service.py            # Génération JSON/CSV
│   └── heartbeat_service.py         # Traitement des signaux HeartBeat
│
├── tasks/                           # Tâches Celery asynchrones
│   ├── celery_app.py                # Initialisation de l'application Celery
│   ├── scan_tasks.py                # Tâche : exécution Nmap
│   ├── traffic_tasks.py             # Tâche : capture de trafic
│   ├── detection_tasks.py           # Tâche : corrélation et détection
│   └── report_tasks.py              # Tâche : génération de rapports
│
├── models/                          # Modèles SQLAlchemy (ORM)
│   ├── host.py
│   ├── port.py
│   ├── scan.py
│   ├── alert.py
│   ├── traffic_event.py
│   ├── rule.py
│   ├── report.py
│   └── heartbeat.py
│
├── schemas/                         # Modèles Pydantic (validation API)
│   ├── host.py
│   ├── scan.py
│   ├── alert.py
│   ├── report.py
│   └── ...
│
└── core/                            # Utilitaires transversaux
    ├── security.py                  # JWT, hashing
    ├── exceptions.py                # Exceptions HTTP personnalisées
    └── logging.py                   # Configuration des logs
```

**Règles d'organisation :**
- Les **routers** ne contiennent que du code HTTP : validation des entrées, appel au service, formatage de la réponse.
- Les **services** contiennent la logique métier pure, sans dépendance à FastAPI.
- Les **tâches** Celery appellent les services — le code métier n'est jamais dupliqué.
- Les **modèles** SQLAlchemy et les **schemas** Pydantic sont strictement séparés (pas de modèle hybride).

---

## 13. Mécanique de corrélation retenue

La corrélation est le mécanisme qui transforme des **événements réseau bruts** en **alertes significatives**. Pour la v1, une approche par règles explicites est retenue (par opposition à l'IA/ML, prévu en v2).

### 13.1 Types de règles supportées

| Type de règle | Exemple | Sévérité |
|---|---|---|
| **Seuil de fréquence** | Plus de 50 connexions TCP depuis une même IP en 60 s | MEDIUM |
| **Port sensible exposé** | Port 22 (SSH) ou 3389 (RDP) ouvert sur un hôte non autorisé | HIGH |
| **Service inattendu** | Service détecté sur un port non standard (ex : HTTP sur port 4444) | MEDIUM |
| **Nouveau hôte détecté** | Adresse IP inconnue apparaît sur le réseau | LOW |
| **Perte de HeartBeat** | Un endpoint ne répond plus depuis N minutes | HIGH |
| **Scan de ports détecté** | Même IP source a tenté de se connecter à 20+ ports en 30 s | HIGH |
| **Trafic hors plage horaire** | Connexion établie en dehors des horaires configurés | MEDIUM |

### 13.2 Pipeline de corrélation

```
[Événements bruts]
        │
        ▼
[Normalisation]          ← Celery worker : parsing Nmap/Scapy → objets Python structurés
        │
        ▼
[Enrichissement]         ← Résolution DNS inverse, lookup de la table hosts (PostgreSQL)
        │
        ▼
[Évaluation des règles]  ← Parcours séquentiel des règles actives (table rules)
        │
        ├── Règle déclenchée → [Génération d'alerte] → [PostgreSQL : table alerts]
        │                                            → [Notification temps réel]
        │
        └── Aucune règle → [Log événement] → [PostgreSQL : table traffic_events]
```

### 13.3 Stockage des règles

Les règles sont stockées en base PostgreSQL dans la table `rules`, exprimées en JSON structuré. Elles sont chargeables à chaud sans redémarrage du service.

```json
{
  "id": "rule_001",
  "name": "Port scan détecté",
  "enabled": true,
  "conditions": {
    "metric": "distinct_ports_contacted",
    "operator": ">=",
    "threshold": 20,
    "window_seconds": 30,
    "group_by": "src_ip"
  },
  "severity": "HIGH",
  "description": "Une IP a tenté de se connecter à 20+ ports distincts en 30 secondes."
}
```

---

## 14. Flux de test en environnement Docker

L'environnement Docker de BigBrowser permet de **reproduire un scénario d'attaque complet** en local, sans infrastructure physique. Ce flux est utilisé pour les tests automatisés, les démonstrations et les sessions de formation.

### 14.1 Topologie de test

```
[attaquant] ──────────────────────────────────▶ [endpoint_1] (172.20.0.10)
(172.20.0.2)                                    [endpoint_2] (172.20.0.11)
                                                [endpoint_3] (172.20.0.12)
                                                       │
                                               Agent HeartBeat
                                                       │
                                                       ▼
                               [backend FastAPI] ◀──────────── [Admin navigateur]
                                       │
                              [Celery Worker] ──▶ scan + capture
                                       │
                                [PostgreSQL] ──▶ persistance
                                       │
                               [Frontend Nginx] ──▶ affichage alertes
```

### 14.2 Scénario de test type

```bash
# 1. Démarrage de l'environnement complet
docker compose up -d

# 2. Vérification que les endpoints sont actifs (HeartBeat visible dans l'UI)
#    → Tableau de bord : 3 hôtes actifs

# 3. Lancement d'un scan de découverte depuis l'UI
#    → POST /api/scans {"range": "172.20.0.0/24"}
#    → Résultat attendu : 3 hôtes découverts, ports ouverts listés

# 4. Simulation d'une attaque depuis le conteneur attaquant
docker exec -it bigbrowser_attaquant nmap -sS -p 1-1000 172.20.0.10

# 5. Vérification de la détection dans l'UI
#    → Alerte générée : "Port scan détecté depuis 172.20.0.2"
#    → Sévérité : HIGH

# 6. Export du rapport NIS2
#    → POST /api/reports {"format": "csv", "include_alerts": true}
#    → Fichier CSV téléchargeable depuis l'UI
```

### 14.3 Tests automatisés

Les tests s'exécutent dans le pipeline CI/CD GitHub Actions à chaque push :

```
pytest tests/
├── test_api/
│   ├── test_scans.py         # Tests des endpoints API scans
│   ├── test_alerts.py        # Tests des endpoints API alertes
│   └── test_reports.py       # Tests génération rapports
├── test_services/
│   ├── test_detection.py     # Tests des règles de corrélation
│   └── test_scan_service.py  # Tests parsing Nmap
└── test_integration/
    └── test_full_flow.py     # Test du flux complet scan → alerte → export
```

---

## 15. Modèle de données fonctionnel

Le modèle de données est organisé autour de **sept entités principales** :

```
┌────────────┐     ┌────────────┐     ┌──────────────────┐
│    scans   │────▶│   hosts    │────▶│      ports       │
│────────────│     │────────────│     │──────────────────│
│ id (PK)    │     │ id (PK)    │     │ id (PK)          │
│ started_at │     │ ip_address │     │ host_id (FK)     │
│ ended_at   │     │ mac_address│     │ number           │
│ range_cidr │     │ hostname   │     │ protocol         │
│ status     │     │ os_guess   │     │ service          │
│ triggered_by│    │ first_seen │     │ version          │
│ scan_type  │     │ last_seen  │     │ state            │
└────────────┘     │ status     │     │ last_seen        │
                   └─────┬──────┘     └──────────────────┘
                         │
              ┌──────────┼──────────────────┐
              │          │                  │
              ▼          ▼                  ▼
    ┌─────────────┐ ┌──────────────┐ ┌───────────────┐
    │  heartbeats │ │traffic_events│ │    alerts     │
    │─────────────│ │──────────────│ │───────────────│
    │ id (PK)     │ │ id (PK)      │ │ id (PK)       │
    │ host_id (FK)│ │ host_id (FK) │ │ host_id (FK)  │
    │ received_at │ │ src_ip       │ │ rule_id (FK)  │
    │ latency_ms  │ │ dst_ip       │ │ severity      │
    └─────────────┘ │ src_port     │ │ title         │
                    │ dst_port     │ │ description   │
                    │ protocol     │ │ triggered_at  │
                    │ bytes        │ │ status        │
                    │ captured_at  │ │ resolved_at   │
                    └──────────────┘ └───────┬───────┘
                                             │
                                    ┌────────▼──────┐
                                    │    reports    │
                                    │───────────────│
                                    │ id (PK)       │
                                    │ generated_at  │
                                    │ format        │
                                    │ period_start  │
                                    │ period_end    │
                                    │ file_path     │
                                    │ alert_count   │
                                    └───────────────┘
```

**Table `rules` (indépendante) :**

| Colonne | Type | Description |
|---|---|---|
| `id` | UUID | Identifiant unique |
| `name` | VARCHAR | Nom lisible de la règle |
| `enabled` | BOOLEAN | Activation/désactivation à chaud |
| `conditions` | JSONB | Expression JSON de la règle |
| `severity` | ENUM | LOW / MEDIUM / HIGH / CRITICAL |
| `created_at` | TIMESTAMP | Date de création |
| `updated_at` | TIMESTAMP | Dernière modification |

---

## 16. Exigences non fonctionnelles

| Catégorie | Exigence | Cible v1 |
|---|---|---|
| **Performance** | Temps de réponse API (requêtes de lecture) | < 500 ms au P95 |
| **Performance** | Durée maximale d'un scan /24 (256 hôtes) | < 3 minutes |
| **Scalabilité** | Nombre d'hôtes supervisés simultanément | Jusqu'à 500 hôtes |
| **Disponibilité** | Uptime cible en production PME | 99 % (hors maintenance) |
| **Sécurité** | Authentification | JWT avec expiration configurable |
| **Sécurité** | Communications | HTTPS obligatoire en production |
| **Sécurité** | Données au repos | PostgreSQL non exposé hors Docker network |
| **Conformité** | RGPD | Données 100 % on-premise, pas d'envoi externe |
| **Conformité** | NIS2 | Export structuré JSON/CSV, traçabilité complète |
| **Maintenabilité** | Couverture de tests | ≥ 70 % sur les services critiques |
| **Maintenabilité** | Documentation API | OpenAPI auto-générée par FastAPI |
| **Portabilité** | OS cible | Linux (Ubuntu 22.04+), Docker requis |
| **Observabilité** | Logs applicatifs | Structurés en JSON, niveau configurable |
| **Observabilité** | Health check | `GET /health` sur le backend, surveillé par Docker |

---

## 17. Interface web cible

L'interface web de BigBrowser est organisée en **6 vues principales**, accessibles depuis une barre de navigation latérale persistante.

### Vue 1 — Tableau de bord (Dashboard)

Vue d'accueil synthétique. Objectif : donner en 10 secondes une image de la santé du réseau.

Éléments affichés :
- Compteur d'hôtes actifs / inactifs (basé sur les HeartBeats)
- Nombre d'alertes ouvertes, ventilées par sévérité (LOW / MEDIUM / HIGH / CRITICAL)
- Dernier scan : date, plage, nombre d'hôtes découverts
- Graphique d'activité des alertes sur les 7 derniers jours
- Bouton d'action rapide : « Lancer un nouveau scan »

### Vue 2 — Carte réseau

Visualisation graphique des équipements découverts et de leurs connexions. Chaque nœud représente un hôte, coloré selon son statut (actif, inactif, en alerte). Librairie recommandée : **vis.js Network** ou **D3.js force graph**.

### Vue 3 — Équipements

Liste paginée des hôtes avec filtres (IP, statut, système d'exploitation). Clic sur un hôte : vue détaillée avec ports ouverts, services, historique des scans, dernier HeartBeat.

### Vue 4 — Alertes

Liste des alertes triées par sévérité décroissante. Filtres : sévérité, statut (nouvelle / en cours / résolue), plage de dates. Actions disponibles : marquer comme traitée, ajouter une note, lier à un rapport.

### Vue 5 — Rapports

Interface de génération des rapports NIS2. Sélection de la période, du format (JSON ou CSV), des types d'événements à inclure. Historique des rapports générés avec liens de téléchargement.

### Vue 6 — Configuration

Gestion des plages IP à surveiller, planification des scans automatiques (cron), gestion des règles de détection (activation/désactivation, édition des seuils), paramètres d'alerte (email, webhook).

---

## 18. MVP recommandé

Le MVP (Minimum Viable Product) est le sous-ensemble minimal qui permet de **démontrer la valeur du produit** et de collecter les premiers retours terrain auprès des PME pilotes.

### Fonctionnalités incluses dans le MVP

| Priorité | Fonctionnalité | Justification |
|---|---|---|
| P0 — Bloquant | Scan de plages IP + découverte d'hôtes | Capacité fondamentale — sans elle, rien ne fonctionne |
| P0 — Bloquant | Détection de ports ouverts | Directement lié à NIS2 (exposition de services) |
| P0 — Bloquant | Interface web avec tableau de bord | Critère de différenciation principal vs. outils CLI |
| P1 — Important | Identification des services réseau | Enrichit la valeur du scan sans effort supplémentaire |
| P1 — Important | Système d'alertes (règles de base) | Nécessaire pour démontrer la détection de menaces |
| P1 — Important | Export JSON/CSV | Requis pour les audits NIS2 — argument commercial clé |
| P2 — Utile | Capture de trafic réseau | Complexité élevée — peut être simplifiée en v1 |
| P2 — Utile | Agent HeartBeat | Améliore la supervision continue mais non bloquant |

### Ce qui est explicitement exclu du MVP

- Interface de gestion des règles (les règles par défaut suffisent en v1)
- Authentification multi-utilisateurs (un seul utilisateur admin en v1)
- Planification avancée des scans (scans manuels suffisent pour le MVP)
- Notifications email / webhook (les alertes dans l'UI suffisent en MVP)

### Critère de sortie du MVP

Le MVP est considéré livrable quand un administrateur peut, sans ouvrir un terminal :
1. Configurer une plage IP depuis l'interface
2. Lancer un scan et voir les résultats dans le tableau de bord
3. Voir une alerte générée automatiquement en cas de comportement suspect
4. Télécharger un rapport CSV de l'activité

---

## 19. Architecture Docker retenue pour la démonstration

L'environnement de démonstration est défini dans un fichier `docker-compose.demo.yml` distinct du `docker-compose.yml` de production. Il ajoute les conteneurs de simulation (endpoints + attaquant) et préconfigure des données initiales.

```yaml
# docker-compose.demo.yml (simplifié)
version: "3.9"

networks:
  bigbrowser_internal:
    driver: bridge
  bigbrowser_sim:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/24

services:

  # ── Services applicatifs ──────────────────────────────────
  nginx:
    image: nginx:1.25
    ports: ["80:80"]
    networks: [bigbrowser_internal]

  backend:
    build: ./backend
    cap_add: [NET_RAW, NET_ADMIN]
    networks: [bigbrowser_internal, bigbrowser_sim]
    environment:
      DATABASE_URL: postgresql://bigbrowser:secret@db:5432/bigbrowser
      REDIS_URL: redis://redis:6379/0
    depends_on: [db, redis]

  worker:
    build: ./backend
    command: celery -A tasks.celery_app worker --loglevel=info
    cap_add: [NET_RAW, NET_ADMIN]
    networks: [bigbrowser_internal, bigbrowser_sim]
    depends_on: [redis, db]

  beat:
    build: ./backend
    command: celery -A tasks.celery_app beat --loglevel=info
    networks: [bigbrowser_internal]
    depends_on: [redis]

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: bigbrowser
      POSTGRES_USER: bigbrowser
      POSTGRES_PASSWORD: secret
    networks: [bigbrowser_internal]
    volumes: [pgdata:/var/lib/postgresql/data]

  redis:
    image: redis:7
    networks: [bigbrowser_internal]

  # ── Simulation réseau ─────────────────────────────────────
  endpoint_1:
    image: ubuntu:22.04
    command: >
      sh -c "apt-get install -y openssh-server nginx &&
             service ssh start && service nginx start && tail -f /dev/null"
    networks:
      bigbrowser_sim:
        ipv4_address: 172.20.0.10

  endpoint_2:
    image: ubuntu:22.04
    command: ["sh", "-c", "tail -f /dev/null"]
    networks:
      bigbrowser_sim:
        ipv4_address: 172.20.0.11

  endpoint_3:
    image: python:3.11
    command: ["sh", "-c", "python -m http.server 8080"]
    networks:
      bigbrowser_sim:
        ipv4_address: 172.20.0.12

  attaquant:
    image: kalilinux/kali-rolling
    command: ["sh", "-c", "tail -f /dev/null"]
    networks:
      bigbrowser_sim:
        ipv4_address: 172.20.0.2
    cap_add: [NET_RAW, NET_ADMIN]

volumes:
  pgdata:
```

**Démarrage en une commande :**
```bash
docker compose -f docker-compose.demo.yml up -d
# Interface disponible sur http://localhost
```

---

## 20. Pourquoi cette architecture est adaptée au sujet

### 20.1 Adéquation avec le périmètre fonctionnel

Chaque choix technologique répond directement à une contrainte fonctionnelle du projet :

| Contrainte fonctionnelle | Réponse architecturale | Pourquoi c'est juste |
|---|---|---|
| 8 fonctionnalités dans une interface web unifiée | FastAPI + Bootstrap + PostgreSQL | Séparation claire UI/API/données, extensibilité facile |
| Scans réseau longs sans bloquer l'UI | Celery + Redis | Pattern producteur/consommateur éprouvé pour les tâches I/O-bound |
| Déployable on-premise sans cloud | Docker Compose | Un seul fichier YAML, aucune dépendance externe |
| Export JSON/CSV pour audits NIS2 | Celery + SQLAlchemy | Génération en arrière-plan, pas de timeout HTTP |
| Simulation d'attaques pour la formation | Conteneur Attaquant (Kali) | Environnement isolé, reproductible, sans risque |
| Zéro CLI pour l'utilisateur final | Bootstrap + API REST | Interface 100 % navigateur, architecture API-first |

### 20.2 Alignement avec les contraintes NIS2

La directive NIS2 impose trois obligations techniques directement adressées par l'architecture :

- **Supervision continue** → Celery Beat + Agent HeartBeat assurent une présence permanente sur le réseau sans intervention manuelle.
- **Traçabilité des incidents** → PostgreSQL conserve l'historique horodaté de tous les événements, alertes et scans — immuable et exportable.
- **Notification structurée** → Les exports JSON et CSV sont formatés pour être directement transmissibles à l'ANSSI ou à un prestataire d'audit.

### 20.3 Viabilité open-source et contributive

L'architecture est pensée pour **accueillir des contributeurs externes** avec un minimum de friction :

- Structure de projet Python standard, documentée et testée.
- API REST avec documentation OpenAPI auto-générée (accessible sur `/docs`).
- Environnement de développement démarrable en une commande (`docker compose up`).
- Séparation stricte des couches : un contributeur peut travailler sur les règles de détection sans toucher au frontend ni à la base de données.

### 20.4 Évolutivité vers les modules premium (v2+)

L'architecture v1 est conçue comme un **socle extensible** :

- Les workers Celery peuvent accueillir des modules IA/ML de détection comportementale sans modifier le cœur.
- Le modèle multi-tenant MSP nécessite uniquement l'ajout d'une table `tenants` et d'un middleware d'isolation dans FastAPI.
- L'offre SaaS cloud s'obtient en remplaçant le Docker Compose par un déploiement Kubernetes, sans modifier une ligne de code applicatif.

---

*Document rédigé en avril 2026 · BigBrowser — Outil de Supervision et d'Analyse Réseau*

*Sources : Feuille de cadrage projet, Business Model (avril 2026), Étude de marché (avril 2026), Schéma d'architecture v1, ANSSI Panorama de la Cybermenace 2024*
