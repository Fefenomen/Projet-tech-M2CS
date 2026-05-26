# BigBrowser

**BigBrowser** est un projet de cybersurveillance réseau orienté SOC. Il vise à concevoir une solution démontrable capable d'observer un environnement réseau, de qualifier des événements de sécurité, de produire des alertes actionnables et de fournir des preuves exploitables pour l'analyse et la validation produit.

Le projet vise à couvrir les besoins suivants :

- collecte de télémétrie depuis un endpoint supervisé ;
- persistance des événements et inventaire d'actifs ;
- détection par règles simples et création d'alertes actionnables ;
- corrélation de signaux répétés ou liés à une même source ;
- triage analyste via une interface web ;
- reporting, KPI et exports CSV / JSON.

Le projet est structuré pour répondre à une exigence de validation professionnelle : relier clairement le besoin initial, les études stratégiques, le cadrage fonctionnel, la gestion de projet, le cahier des charges et l'architecture technique.

## Schéma global de fonctionnement

![Capture d'écran de mon projet](08_architecture/assets/Schema_global_de_fonctionnement.png)

Explication fonctionnelle simplifiée
1. Collecte de télémétrie

Les endpoints supervisés envoient des événements de sécurité :

connexions réseau ;
exécution de processus ;
logs système ;
erreurs ;
activités suspectes.

Le module Telemetry réceptionne et normalise les données.

2. Centralisation des données

Les événements sont stockés dans une base centrale :

historique des événements ;
inventaire des machines ;
données d’audit ;
traces analystes.

Cela permet la traçabilité et les analyses SOC.

3. Détection et corrélation

Le moteur de détection applique :

règles simples ;
corrélation multi-événements ;
scoring de criticité ;
logique NIS2.

Exemple :

plusieurs échecs de connexion ;
activité répétée ;
communication vers IP suspecte.

=> génération d’une alerte.

4. Gestion des alertes

Le module Alerts permet :

priorisation ;
qualification ;
assignation ;
suivi du traitement ;
clôture.

Les analystes SOC peuvent investiguer depuis l’interface web.

5. Interface SOC

Le dashboard web fournit :

vue temps réel ;
indicateurs KPI ;
reporting ;
conformité ;
exports CSV / JSON.
6. Sécurité et gouvernance

Les modules transverses assurent :

Auth : authentification ;
RBAC : contrôle des accès ;
Audit Trail : traçabilité ;
Reports : génération de rapports.

## Flux métier simplifié

1. L’attaquant Docker génère des comportements suspects contrôlés :
   - scans réseau ;
   - flood HTTP ;
   - tentatives de connexion échouées ;
   - trafic multi-ports.

2. Les endpoints supervisés exécutent l’agent BigBrowser.

3. L’agent collecte :
   - les heartbeats ;
   - les événements réseau ;
   - certains comportements détectés localement.

4. Les données sont envoyées au Backend FastAPI via API sécurisée JWT.

5. Le backend :
   - persiste les événements ;
   - met à jour l’inventaire des actifs ;
   - applique les règles de détection ;
   - génère des alertes ;
   - journalise les actions critiques.

6. Le dashboard SOC affiche :
   - les métriques ;
   - les alertes ;
   - les actifs réseau ;
   - les journaux d’audit.

7. L’administrateur ou l’analyste SOC peut :
   - investiguer les alertes ;
   - changer leur statut ;
   - consulter les événements ;
   - exporter des rapports CSV/JSON.

8. Les exports permettent de produire des preuves exploitables pour :
   - les audits ;
   - la traçabilité ;
   - la conformité NIS2.

## Présentation du projet

- **Auth** : authentification et contrôle d'accès.
- **Telemetry** : ingestion et consultation des événements.
- **Assets** : inventaire enrichi depuis les événements observés.
- **Alerts** : liste, détail et traitement des alertes.
- **Reports** : synthèse et exports.
- **RBAC** : protection des actions sensibles selon le rôle.
- **Audit Trail** : traçabilité des actions critiques.

## Structure du dépôt

- [`product/`](product/) : futur code source du produit BigBrowser.
- [`website/`](website/) : futur site web officiel [BigBrowser.com](https://BigBrowser.com).
- [`documents/`](documents/) : livrables de cadrage, stratégiques, fonctionnels et techniques.

## Navigation rapide

- Produit : [product/README.md](product/README.md)
- Site web : [website/README.md](website/README.md)
- Documents : [documents/README.md](documents/README.md)
- Étude de marché : [documents/02_etude_de_marche/rendu_principal.md](documents/02_etude_de_marche/rendu_principal.md)
- Business model : [documents/03_business_model/rendu_principal.md](documents/03_business_model/rendu_principal.md)
- Business plan : [documents/04_business_plan/rendu_principal.md](documents/04_business_plan/rendu_principal.md)
- Architecture retenue : [documents/08_architecture/rendu_principal.md](documents/08_architecture/rendu_principal.md)

## Documentation associée

- Documents de cadrage initial : [documents/01_documents_pedagogiques/README.md](documents/01_documents_pedagogiques/README.md)
- Références transverses : [documents/90_references_transverses/README.md](documents/90_references_transverses/README.md)

## État actuel

La branche `main` est organisée pour séparer clairement :

- le futur produit,
- le futur site corporate,
- les livrables de cadrage et stratégiques déjà consolidés.
