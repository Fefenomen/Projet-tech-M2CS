# BigBrowser

BigBrowser est un projet de cybersurveillance réseau orienté SOC. Il vise à concevoir une solution démontrable capable d'observer un environnement réseau, de qualifier des événements de sécurité, de produire des alertes actionnables et de fournir des preuves exploitables pour l'analyse et la validation produit.

Le projet vise à couvrir les besoins suivants :

- collecte de télémétrie depuis un endpoint supervisé ;
- persistance des événements et inventaire d'actifs ;
- détection par règles simples et création d'alertes actionnables ;
- corrélation de signaux répétés ou liés à une même source ;
- triage analyste via une interface web ;
- reporting, KPI et exports CSV / JSON.

Le projet est structuré pour répondre à une exigence de validation professionnelle : relier clairement le besoin initial, les études stratégiques, le cadrage fonctionnel, la gestion de projet, le cahier des charges et l'architecture technique.

## Schéma global de fonctionnement

TO DO

## Flux métier simplifié

TO DO

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