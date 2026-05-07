# BigBrowser — Lab de Démonstration Docker

Environnement Docker reproductible pour démontrer la chaîne complète de cybersurveillance BigBrowser.

## Architecture du Lab

```
DOCKER HOST
  réseau interne : BBrowser_net (172.20.0.0/24)

  [Attaquant (Docker)] 172.20.0.50
         |
         | trafic réseau / comportements suspects contrôlés
         v
  [Endpoints (Docker)]
    +-----------+  +-----------+
    | endpoint1 |  | endpoint2 |
    | 172.20.0.20|  |172.20.0.21|
    +-----------+  +-----------+
         |
         | Agent HeartBeat + Events (HTTP / JWT)
         v
  [SOC (Docker)] 172.20.0.10
    +---------------------+
    | Frontend Bootstrap  | <--- Admin Sys (http://localhost:8000)
    |                     |
    | Backend FastAPI     |
    |                     |
    | SQLite (persisté)   |
    +---------------------+
```

## Prérequis

- Docker 20.10+
- Docker Compose v2+
- Linux / macOS / WSL2

## Lancement

### Démarrer le lab

```bash
cd product/docker
./demo.sh up
```

### Lancer la démo complète

```bash
./demo.sh demo
```

Ce script :
1. Lance tous les conteneurs
2. Attend que le SOC soit prêt
3. Attend que les endpoints s'enregistrent
4. Lance les scénarios d'attaque
5. Affiche les métriques du dashboard
6. Montre les alertes générées et les logs d'audit

### Commandes disponibles

| Commande | Description |
|---|---|
| `./demo.sh up` | Démarrer le lab |
| `./demo.sh down` | Arrêter le lab |
| `./demo.sh status` | Voir l'état des conteneurs |
| `./demo.sh logs` | Voir les logs en continu |
| `./demo.sh reset` | Reset complet (down + rebuild + up) |
| `./demo.sh demo` | Lancer la démo complète |

## Accès

| Service | URL | Identifiants |
|---|---|---|
| Dashboard SOC | http://localhost:8000 | admin / admin123 |
| Swagger API | http://localhost:8000/docs | admin / admin123 |
| Health check | http://localhost:8000/health/ | Public |

## Comptes par défaut

| Username | Password | Rôle |
|---|---|---|
| `admin` | `admin123` | Administrateur |
| `analyst` | `analyst123` | Analyste |
| `agent` | `agent_secret_mvp` | Agent (heartbeat) |

## Scénario de démonstration

1. **Lancement** : `./demo.sh up` → SOC + 2 Endpoints + Attaquant
2. **Découverte** : Les endpoints s'enregistrent via heartbeat
3. **Attaque simulée** : L'attaquant exécute :
   - Scan de ports sur les endpoints
   - Flood HTTP (tentatives répétées)
   - Tentatives de login échouées
   - Trafic suspect multi-ports
4. **Détection** : Le SOC reçoit les événements et génère des alertes
5. **Analyse** : L'admin consulte le dashboard, les alertes, les logs
6. **Export** : Génération d'un export CSV/JSON comme preuve NIS2

## Configuration

### Variables d'environnement

Copier `.env.example` vers `.env` et ajuster :

```bash
cp .env.example .env
```

| Variable | Description | Défaut |
|---|---|---|
| `HOST` | Hôte d'écoute du SOC | `0.0.0.0` |
| `PORT` | Port du SOC | `8000` |
| `DATABASE_URL` | URL SQLite | `sqlite:///data/bigbrowser.db` |
| `SOC_URL` | URL du SOC (pour agent) | `http://soc:8000` |
| `AGENT_SECRET` | Mot de passe agent | `agent_secret_mvp` |
| `HEARTBEAT_INTERVAL` | Intervalle heartbeat (s) | `30` |
| `TARGET_SUBNET` | Cibles de l'attaquant | `172.20.0.20-172.20.0.21` |
| `SCENARIO_DELAY` | Délai entre scénarios (s) | `30` |

### Structure du lab

```
docker/
├── docker-compose.yml      # Configuration des 4 conteneurs
├── Dockerfile.soc          # SOC: FastAPI + SQLite + Frontend
├── Dockerfile.endpoint     # Endpoint: nginx + agent
├── Dockerfile.attacker     # Attaquant: nmap + scenarios
├── .env.example            # Variables documentées
└── demo.sh                 # Script d'orchestration

agent/
├── agent.py                # Agent heartbeat + event collector
├── entrypoint.sh           # nginx + agent
└── requirements.txt

attacker/
├── scenarios.py            # Scénarios offensifs contrôlés
├── entrypoint.sh
└── requirements.txt
```

## Scénarios d'attaque

L'attaquant exécute ces scénarios en boucle :

| Scénario | Description | Détection attendue |
|---|---|---|
| **Port Scan** | Scan TCP sur ports 22, 80, 443, 8080, 3306 | Alertes de scan |
| **HTTP Flood** | 20 requêtes HTTP rapides vers /admin | Trafic suspect |
| **Failed Logins** | 5 tentatives de login échouées | Comportement suspect |
| **Suspicious Traffic** | Connexions rapides multi-ports | Multi-ports détectés |

## Troubleshooting

### Le SOC ne démarre pas

```bash
./demo.sh logs soc
```

### Les endpoints ne s'enregistrent pas

```bash
./demo.sh logs endpoint1
```

### Reset complet

```bash
./demo.sh reset
```

## Sécurité

- ⚠️ **Ne pas exposer ce lab sur un réseau public**
- Les mots de passe par défaut sont documentés dans `.env.example`
- Les scénarios d'attaque sont contrôlés et limités au réseau `BBrowser_net`
- Aucun malware ou code destructeur n'est inclus
