# Sources de Référence — BigBrowser

> Document consolidé à partir des fichiers `01_exigences_referentielles.md`, `02_scenarios_recette.md`, `03_securite_conformite.md` et `04_sources_reference.md`.

---

## Section 1 — Exigences référentielles

### 1.1. Règles métier (RM)

| ID | Règle | Description | Critère de vérification | Priorité |
|---|---|---|---|---|
| RM-001 | Authentification utilisateur | Un utilisateur doit disposer d'un identifiant, d'un mot de passe stocké sous forme hachée et d'un rôle. | Un accès sans session valide est refusé. | P1 |
| RM-002 | Scan borné | Tout scan réseau doit être limité à la plage IP configurée. | Un scan hors plage autorisée est refusé ou ignoré. | P1 |
| RM-003 | Détection de ports | Les ports ouverts détectés sur un équipement doivent être associés à l'actif correspondant. | Le résultat de scan est consultable dans le détail de l'actif. | P1 |
| RM-004 | Détection de comportements suspects | Au moins trois tentatives similaires depuis une même IP doivent produire une alerte. | Le scénario de test contrôlé génère une alerte. | P1 |
| RM-005 | Statuts d'alerte | Une alerte doit au minimum supporter les statuts `nouvelle`, `en cours` et `clôturée`. | Le statut est visible et modifiable par un utilisateur autorisé. | P1 |
| RM-006 | Preuve exportable | Un export doit contenir les données du scénario, une date de génération, un format et un identifiant de demande. | Le fichier CSV/JSON permet de retrouver le scénario joué. | P1 |
| RM-007 | Audit obligatoire | Connexion, export, changement de statut d'alerte et action d'administration doivent produire une entrée d'audit. | Chaque action sensible apparaît dans les journaux d'audit. | P1 |
| RM-008 | Validation des entrées | Tout champ de saisie (plage IP, filtre, formulaire) doit être validé strictement côté serveur via Pydantic et regex. | Un payload invalide est rejeté proprement, sans erreur non contrôlée. | P1 |

### 1.2. Exigences fonctionnelles (F)

#### Authentification et contrôle d'accès

| ID | Exigence | Priorité | Critère d'acceptation |
|---|---|---|---|
| F-AUTH-001 | Le système doit permettre l'authentification sécurisée des utilisateurs. | P1 | Un utilisateur valide accède au tableau de bord après connexion. |
| F-AUTH-002 | Le système doit distinguer les rôles `admin` et `analyst`. | P1 | Les permissions diffèrent selon le rôle. |
| F-AUTH-003 | Le système doit restreindre les actions sensibles selon le rôle. | P1 | Un analyste ne peut pas exécuter une action réservée à l'administration. |

#### Découverte réseau et inventaire des actifs

| ID | Exigence | Priorité | Critère d'acceptation |
|---|---|---|---|
| F-DISC-001 | Le système doit scanner une plage IP définie par l'utilisateur. | P1 | Une plage IP configurée est analysée et les actifs créés ou mis à jour. |
| F-DISC-002 | Le système doit identifier les équipements observables. | P1 | Au moins un actif est créé avec son adresse IP et son statut. |
| F-DISC-003 | Le système doit détecter les ports ouverts. | P1 | Les ports détectés sont associés à l'actif correspondant. |
| F-DISC-004 | Le système doit récupérer des informations de services quand elles sont disponibles. | P2 | Les services observés apparaissent dans le détail d'un actif. |
| F-ASSET-001 | Le système doit maintenir un inventaire d'actifs consultable. | P1 | L'interface affiche la liste et le détail des actifs connus. |

#### Capture et analyse du trafic réseau

| ID | Exigence | Priorité | Critère d'acceptation |
|---|---|---|---|
| F-TRAF-001 | Le système doit capturer des flux réseau sur l'interface configurée. | P1 | Des captures de trafic sont disponibles dans l'interface. |
| F-TRAF-002 | Le système doit permettre le filtrage du trafic capturé. | P2 | L'utilisateur peut filtrer par IP, port ou protocole. |

#### Détection et alerting

| ID | Exigence | Priorité | Critère d'acceptation |
|---|---|---|---|
| F-ALERT-001 | Le système doit produire des alertes issues de règles simples. | P1 | Un comportement suspect génère une alerte. |
| F-ALERT-002 | Le système doit proposer une vue de liste des alertes. | P1 | Les alertes sont consultables dans l'interface. |
| F-ALERT-003 | Le système doit proposer une vue de détail d'une alerte. | P1 | Une alerte affiche son contexte, sa source et son horodatage. |
| F-ALERT-004 | Le système doit gérer un cycle de vie minimal des alertes. | P1 | Une alerte peut changer de statut ou être qualifiée. |
| F-ALERT-005 | Le système doit permettre la configuration des règles d'alerte. | P2 | Un administrateur peut ajuster les seuils de détection. |

#### Interface web

| ID | Exigence | Priorité | Critère d'acceptation |
|---|---|---|---|
| F-UI-001 | L'interface doit proposer un tableau de bord de synthèse. | P1 | Le tableau de bord affiche les métriques clés. |
| F-UI-002 | L'interface doit permettre la consultation des actifs. | P1 | La liste et le détail des actifs sont accessibles. |
| F-UI-003 | L'interface doit permettre la consultation des alertes. | P1 | Les alertes générées sont visibles et filtrables. |
| F-UI-004 | L'interface doit permettre la consultation du trafic capturé. | P1 | Les flux réseau capturés sont visualisables. |
| F-UI-005 | L'interface doit permettre la consultation des journaux d'audit. | P2 | Les actions sensibles journalisées sont consultables par `admin`. |

#### Reporting et exports

| ID | Exigence | Priorité | Critère d'acceptation |
|---|---|---|---|
| F-EXP-001 | Le système doit produire un export CSV. | P1 | Un fichier CSV est généré avec les colonnes obligatoires définies. |
| F-EXP-002 | Le système doit produire un export JSON. | P1 | Un fichier JSON est généré avec les métadonnées obligatoires. |
| F-EXP-003 | Les exports doivent servir de preuve opérationnelle de conformité NIS2. | P1 | L'export contient des données cohérentes avec le scénario joué. |
| F-EXP-004 | Les exports doivent être accessibles uniquement aux utilisateurs autorisés. | P1 | Un utilisateur non autorisé ne peut pas générer ou consulter un export. |

#### Audit et journalisation

| ID | Exigence | Priorité | Critère d'acceptation |
|---|---|---|---|
| F-AUD-001 | Le système doit journaliser les authentifications. | P1 | Une connexion génère une entrée d'audit. |
| F-AUD-002 | Le système doit journaliser les exports. | P1 | Un export génère une entrée d'audit. |
| F-AUD-003 | Le système doit journaliser les actions sensibles d'administration. | P1 | Une action sensible est traçable. |
| F-AUD-004 | Les journaux doivent être consultables par un profil autorisé. | P2 | Un administrateur consulte les journaux d'audit. |

### 1.3. Exigences non fonctionnelles (NF)

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
| NF-SEC-001 | Sécurité | Les exports doivent être chiffrés ou contrôlés en accès local. | P2 | Un utilisateur non autorisé ne peut pas accéder aux fichiers exportés. |
| NF-SEC-002 | Sécurité | Les scans furtifs avec délais inter-requêtes doivent être configurables. | P2 | Des délais inter-requêtes sont paramétrables depuis la configuration. |
| NF-ARCH-001 | Architecture | Les traitements asynchrones doivent être isolés du chemin synchrone de l'API. | P1 | Celery/Redis sont séparés de la boucle de requêtes FastAPI. |
| NF-ARCH-002 | Architecture | Les routes d'ingestion agent doivent être distinctes des routes utilisateur. | P1 | Les endpoints `/telemetry/*` sont séparés des routes métier. |

### 1.4. Exigences de sécurité (SEC)

| ID | Exigence | Priorité | Critère d'acceptation | Référence OWASP ASVS |
|---|---|---|---|---|
| SEC-001 | L'accès à l'interface doit nécessiter une authentification. | P1 | Une page protégée n'est pas accessible sans session valide. | V2 (Authentication) |
| SEC-002 | Les actions sensibles doivent être contrôlées par rôle. | P1 | Un `analyst` ne peut pas effectuer une action réservée à `admin`. | V4 (Access Control) |
| SEC-003 | Les champs de saisie (plage IP, filtres) doivent être validés strictement via Pydantic et regex. | P1 | Une injection de commande dans un champ IP est bloquée. | V5 (Validation, Sanitization) |
| SEC-004 | Les exports doivent être chiffrés ou contrôlés en accès local. | P1 | Un utilisateur non autorisé ne peut pas accéder aux fichiers exportés. | V8 (Data Protection) |
| SEC-005 | Les secrets ne doivent pas être exposés dans le dépôt. | P1 | Aucun secret réel n'est versionné dans le dépôt GitHub. | V8 (Data Protection) |
| SEC-006 | Les actions sensibles doivent produire une entrée d'audit. | P1 | Les connexions, exports et actions d'administration sont tracés. | V7 (Logging) |
| SEC-007 | Les scans doivent être limités à la plage IP configurée par l'administrateur. | P1 | Aucun scan ne cible une IP hors de la plage autorisée. | V5 (Input Validation) |
| SEC-008 | Les requêtes réseau de scan doivent inclure des délais pour éviter le bannissement IDS. | P2 | Des délais inter-requêtes sont configurables (scans furtifs). | V5 (Rate Limiting) |

### 1.5. Priorisation MoSCoW

**Priorité P1 — Must have (indispensable MVP)**

| Domaine | Éléments |
|---|---|
| Authentification | F-AUTH-001, F-AUTH-002, F-AUTH-003, RM-001 |
| Découverte réseau | F-DISC-001, F-DISC-002, F-DISC-003, F-ASSET-001, RM-002, RM-003 |
| Trafic réseau | F-TRAF-001 |
| Détection et alerting | F-ALERT-001, F-ALERT-002, F-ALERT-003, F-ALERT-004, RM-004, RM-005 |
| Interface web | F-UI-001, F-UI-002, F-UI-003, F-UI-004 |
| Reporting | F-EXP-001, F-EXP-002, F-EXP-003, F-EXP-004, RM-006 |
| Audit | F-AUD-001, F-AUD-002, F-AUD-003, RM-007 |
| Sécurité | SEC-001, SEC-002, SEC-003, SEC-004, SEC-005, SEC-006, SEC-007 |
| Qualité | NF-QUAL-001, NF-QUAL-002, RM-008 |
| Performance | NF-PERF-001, NF-PERF-002, NF-PERF-003 |
| Observabilité | NF-OBS-001, NF-OBS-002 |
| Déploiement | NF-DEP-001, NF-DEP-002 |
| Architecture | NF-ARCH-001, NF-ARCH-002 |

**Priorité P2 — Should have (fortement souhaitable)**

| Domaine | Éléments |
|---|---|
| Découverte réseau | F-DISC-004 (récupération services) |
| Trafic réseau | F-TRAF-002 (filtrage trafic) |
| Alerting | F-ALERT-005 (configuration règles) |
| Interface web | F-UI-005 (consultation audit logs) |
| Audit | F-AUD-004 |
| Sécurité | SEC-008 (scans furtifs) |
| Performance | NF-SEC-001, NF-SEC-002 |

**Priorité P3 — Could have (extension)**

| Domaine | Éléments |
|---|---|
| Conformité | Dashboard NIS2 dédié |
| Détection | Modules IA/ML comportementale |
| Déploiement | Offre SaaS hébergée |
| Documentation | API REST documentée complète (v2) |
| Internationalisation | Support Belgique, Luxembourg |

### 1.6. Matrice de traçabilité complète

| Besoin initial | Exigences associées | Scénario de recette | Preuve attendue |
|---|---|---|---|
| Sécuriser l'accès à l'application | F-AUTH-001, F-AUTH-002, F-AUTH-003, SEC-001, SEC-002, RM-001 | REC-001, REC-002 | Connexion valide, refus d'accès sans session, entrée d'audit |
| Découvrir les équipements réseau | F-DISC-001, F-DISC-002, F-DISC-003, F-ASSET-001, RM-002, RM-003 | REC-003 | Vue actifs, résultat de scan, ports et services associés |
| Détecter des comportements suspects | F-ALERT-001, F-ALERT-002, F-ALERT-003, RM-004 | REC-004 | Vue alerte, événement source, contexte de détection |
| Qualifier et gérer les alertes | F-ALERT-004, F-AUD-003, RM-005 | REC-005 | Changement de statut, qualification, entrée d'audit |
| Produire des preuves de conformité NIS2 | F-EXP-001, F-EXP-002, F-EXP-003, F-AUD-002, RM-006 | REC-006 | Fichier CSV/JSON, métadonnées d'export, entrée d'audit |
| Valider et sécuriser les entrées utilisateur | SEC-003, RM-008, NF-QUAL-002 | REC-007 | Réponse d'erreur contrôlée, payload invalide rejeté |
| Garantir la performance de l'interface | NF-PERF-001, NF-PERF-002, NF-PERF-003 | REC-008 | Temps de réponse mesuré sous les seuils définis |
| Assurer la santé et la déployabilité | NF-OBS-001, NF-DEP-001, NF-DEP-002 | REC-009 | Endpoint `/health` opérationnel, déploiement reproductible |
| Démontrer la chaîne fonctionnelle complète | Toutes exigences P1 | REC-010 | Chaîne scan → détection → alerte → export visible et reproductible |
| Journaliser les actions sensibles | F-AUD-001, F-AUD-002, F-AUD-003, F-AUD-004, SEC-006, RM-007 | REC-001, REC-005, REC-006 | Entrées d'audit consultables pour chaque action sensible |
| Contrôler les permissions par rôle | SEC-002, RM-001, F-AUTH-002, F-AUTH-003 | REC-002 | Matrice des permissions respectée |
| Limiter les scans au périmètre autorisé | SEC-007, RM-002 | REC-003 | Scan borné à la plage IP configurée |

### 1.7. Contrat API MVP (13 endpoints)

| Méthode | Endpoint | Usage | Accès | Priorité |
|---|---|---|---|---|
| `POST` | `/auth/login` | Authentification utilisateur | Public | P1 |
| `GET` | `/auth/me` | Informations utilisateur courant | `admin`, `analyst` | P1 |
| `GET` | `/health` | Santé applicative | Public | P1 |
| `POST` | `/telemetry/heartbeat` | Réception heartbeat agent | Agent | P1 |
| `POST` | `/telemetry/events` | Réception events agent | Agent | P1 |
| `POST` | `/scan` | Lancement d'un scan réseau | `admin` | P1 |
| `GET` | `/assets` | Liste des actifs | `admin`, `analyst` | P1 |
| `GET` | `/assets/{id}` | Détail d'un actif | `admin`, `analyst` | P1 |
| `GET` | `/alerts` | Liste des alertes | `admin`, `analyst` | P1 |
| `GET` | `/alerts/{id}` | Détail d'une alerte | `admin`, `analyst` | P1 |
| `PATCH` | `/alerts/{id}` | Qualification / changement de statut | `admin`, `analyst` | P2 |
| `POST` | `/exports` | Génération d'un export CSV/JSON | `admin`, `analyst` | P1 |
| `GET` | `/audit-logs` | Consultation des journaux d'audit | `admin` | P2 |

### 1.8. Entités de données et champs minimaux

| Entité | Champs minimaux MVP |
|---|---|
| `users` | `id`, `username`, `password_hash`, `role`, `created_at`, `is_active` |
| `assets` | `id`, `ip_address`, `hostname`, `first_seen_at`, `last_seen_at`, `status` |
| `ports` | `id`, `asset_id`, `port`, `protocol`, `state`, `observed_at` |
| `alerts` | `id`, `title`, `severity`, `status`, `source_ip`, `description`, `created_at`, `updated_at` |
| `audit_logs` | `id`, `user_id`, `role`, `action`, `target_type`, `result`, `created_at` |
| `exports` | `id`, `format`, `requested_by`, `scope`, `file_path`, `created_at`, `row_count` |
| `events` | `id`, `source_ip`, `target_ip`, `event_type`, `severity`, `message`, `created_at`, `asset_id` |

### 1.9. Flux de données

| ID | Source | Destination | Description |
|---|---|---|---|
| FLUX-001 | Module scan | Réseau supervisé | Scan de plage IP, détection d'actifs et ports |
| FLUX-002 | Module capture | Interface réseau | Capture et analyse du trafic |
| FLUX-003 | Interface web | API FastAPI | Consultation des actifs, alertes, exports |
| FLUX-004 | API FastAPI | Base de données | Persistance et lecture des données |
| FLUX-005 | API FastAPI | Worker asynchrone | Planification des scans et traitements différés |
| FLUX-006 | Worker | Base de données | Création ou mise à jour des alertes et actifs |

### 1.10. Matrice des permissions MVP

| Fonction | `admin` | `analyst` | Non authentifié |
|---|---|---|---|
| Se connecter à l'interface | Oui | Oui | Non |
| Consulter le tableau de bord | Oui | Oui | Non |
| Lancer un scan réseau | Oui | Non | Non |
| Consulter les équipements et alertes | Oui | Oui | Non |
| Qualifier une alerte ou changer son statut | Oui | Oui | Non |
| Générer un export CSV/JSON | Oui | Oui | Non |
| Consulter les journaux d'audit | Oui | Non | Non |
| Administrer les utilisateurs ou rôles | Oui | Non | Non |

---

## Section 2 — Scénarios de recette (REC-001 à REC-010)

### REC-001 — Connexion utilisateur

| Champ | Valeur |
|---|---|
| ID | REC-001 |
| Titre | Connexion utilisateur et contrôle d'accès |
| Exigences couvertes | F-AUTH-001, RM-001, SEC-001, F-AUD-001 |
| Périmètre | Authentification |

**Préconditions :** Compte `admin` (admin/admin123) et compte `analyst` (analyst/analyst123) créés. Application accessible sur `http://localhost:8000`.

**Étapes :**
1. Accéder à `http://localhost:8000` sans session active (redirection page login).
2. Saisir identifiant et mot de passe valides, soumettre, vérifier accès tableau de bord.
3. Se déconnecter, tenter d'accéder à `/dashboard` sans session, vérifier refus (401 ou redirection).

**Résultat attendu :** Connexion valide → accès accordé. Accès sans session → refus.

**Preuve :** Capture tableau de bord, réponse HTTP 401/302, entrée `audit_logs`.

---

### REC-002 — Contrôle des permissions par rôle

| Champ | Valeur |
|---|---|
| ID | REC-002 |
| Titre | Contrôle des permissions selon le rôle |
| Exigences couvertes | F-AUTH-002, F-AUTH-003, SEC-002 |
| Périmètre | RBAC |

**Préconditions :** Compte `analyst` connecté, compte `admin` disponible.

**Étapes :**
1. Connecter `analyst`, tenter d'accéder à `/audit-logs` et `/scan`.
2. Vérifier refus 403 pour les deux.
3. Connecter `admin`, accéder aux deux ressources, vérifier succès.

**Résultat attendu :** Actions réservées à `admin` refusées pour `analyst` (403). Autorisées pour `admin`.

**Preuve :** Réponse 403, captures interface, entrées d'audit.

---

### REC-003 — Scan réseau borné

| Champ | Valeur |
|---|---|
| ID | REC-003 |
| Titre | Scan réseau et découverte d'actifs |
| Exigences couvertes | F-DISC-001/2/3, F-ASSET-001, RM-002/3, SEC-007 |
| Périmètre | Discovery, Assets |

**Préconditions :** Compte `admin` connecté, plage IP `192.168.100.0/24`, réseau accessible.

**Étapes :**
1. Lancer un scan sur `192.168.100.0/24`, attendre la fin asynchrone.
2. Consulter la liste des actifs, vérifier création.
3. Consulter le détail d'un actif, vérifier les ports ouverts.
4. Tenter un scan sur `10.0.0.0/8`, vérifier refus.

**Résultat attendu :** Actifs créés avec IP, statut et ports. Scan hors zone refusé.

**Preuve :** Vue liste actifs, vue détail ports, message de refus.

---

### REC-004 — Détection de comportement suspect

| Champ | Valeur |
|---|---|
| ID | REC-004 |
| Titre | Détection de comportement suspect (règle de seuil) |
| Exigences couvertes | F-ALERT-001/2/3, RM-004 |
| Périmètre | Alerts, Détection |

**Préconditions :** Worker Celery actif, règles de détection configurées (seuil : 3 tentatives depuis une même IP source).

**Étapes :**
1. Générer 1 tentative (10.0.0.99 → 192.168.100.10:22) → aucune alerte.
2. Générer 2 tentatives supplémentaires → attendre traitement asynchrone.
3. Consulter la liste des alertes, vérifier création avec titre, source IP, sévérité, statut `nouvelle`.

**Résultat attendu :** Pas d'alerte avant le seuil. Alerte créée après la 3e tentative.

**Preuve :** Vue liste alertes, vue détail avec contexte, log worker.

---

### REC-005 — Cycle de vie d'une alerte

| Champ | Valeur |
|---|---|
| ID | REC-005 |
| Titre | Gestion du cycle de vie d'une alerte |
| Exigences couvertes | F-ALERT-004, F-AUD-003, RM-005, RM-007 |
| Périmètre | Alerts, Audit |

**Préconditions :** Alerte existante avec statut `nouvelle`, utilisateur connecté.

**Étapes :**
1. Vérifier statut `nouvelle`, basculer à `en cours`, vérifier mise à jour.
2. Ajouter un commentaire de qualification.
3. Basculer à `clôturée`, vérifier mise à jour.
4. Consulter les journaux d'audit (admin), vérifier les entrées.

**Résultat attendu :** Trois statuts supportés, changements persistés et audités.

**Preuve :** Vue détail alerte, entrées `audit_logs`, horodatage.

---

### REC-006 — Export de preuve CSV/JSON

| Champ | Valeur |
|---|---|
| ID | REC-006 |
| Titre | Génération d'export CSV et JSON |
| Exigences couvertes | F-EXP-001/2/3, F-AUD-002, RM-006 |
| Périmètre | Reports, Exports |

**Préconditions :** Au moins une alerte présente, utilisateur connecté.

**Étapes :**
1. Sélectionner périmètre `alerts`, format `CSV`, générer, télécharger.
2. Vérifier colonnes : `export_id`, `generated_at`, `type`, `id`, `source_ip`, `severity`, `status`, `created_at`, `description`.
3. Répéter en `JSON`, vérifier structure : `export_id`, `generated_at`, `format`, `scope`, `items`.
4. Vérifier présence de l'alerte REC-004 dans les deux exports.
5. Consulter `audit_logs` pour tracer les exports.

**Résultat attendu :** Fichiers valides avec métadonnées et données cohérentes. Entrées d'audit présentes.

**Preuve :** Fichiers CSV et JSON, entrées `audit_logs`.

---

### REC-007 — Validation d'injection IP

| Champ | Valeur |
|---|---|
| ID | REC-007 |
| Titre | Rejet d'injection de commande via champ IP |
| Exigences couvertes | SEC-003, RM-008, NF-QUAL-002 |
| Périmètre | Sécurité, Validation |

**Préconditions :** Compte `admin` connecté, interface de scan accessible.

**Étapes :**
1. Saisir dans le champ IP :
   - `192.168.1.1; rm -rf /`
   - `192.168.1.1' OR '1'='1`
   - `999.999.999.999`
   - Chaîne vide
2. Soumettre chaque cas, vérifier rejet (422 ou 400).
3. Vérifier absence d'effet de bord et d'erreur non contrôlée dans les logs.

**Résultat attendu :** Chaque payload invalide rejeté proprement. Aucune exécution système.

**Preuve :** Réponse 422 avec détail Pydantic, logs de validation.

---

### REC-008 — Latence de l'interface

| Champ | Valeur |
|---|---|
| ID | REC-008 |
| Titre | Mesure de performance des vues principales |
| Exigences couvertes | NF-PERF-001, NF-PERF-003 |
| Périmètre | Performance |

**Préconditions :** Jeu de données : 50 actifs, 200 événements, 25 alertes, 10 exports.

**Étapes :**
1. Mesurer temps de chargement (moyenne sur 3 essais) : tableau de bord, liste actifs, liste alertes.
2. Mesurer temps de génération d'un export CSV 100 lignes.

**Résultat attendu :** Vues < 2s, export CSV < 5s.

**Preuve :** Relevé des temps de réponse.

---

### REC-009 — Santé et déployabilité

| Champ | Valeur |
|---|---|
| ID | REC-009 |
| Titre | Vérification de l'état de santé et de la déployabilité |
| Exigences couvertes | NF-OBS-001, NF-DEP-001, NF-DEP-002 |
| Périmètre | Observabilité, Déploiement |

**Préconditions :** Application démarrée, `.env.example` présent, README documenté.

**Étapes :**
1. Exécuter `curl http://localhost:8000/health`.
2. Vérifier réponse JSON : `api: ok`, `database: connected`, `worker: active`.
3. Vérifier documentation d'installation et dépôt GitHub public.

**Résultat attendu :** Endpoint `/health` opérationnel. Déploiement autonome possible.

**Preuve :** Réponse JSON `/health`, README, `docker-compose.yml`.

---

### REC-010 — Démonstration complète

| Champ | Valeur |
|---|---|
| ID | REC-010 |
| Titre | Parcours complet de démonstration |
| Exigences couvertes | Toutes exigences P1 |
| Périmètre | Intégration |

**Préconditions :** Lab Docker complet (SOC + Endpoints + Attaquant), jeu de données chargé.

**Étapes :**
1. Lancer `docker compose up`, connecter `admin`.
2. Lancer scan (REC-003), attendre découverte actifs.
3. Déclencher scénario offensif (3 tentatives SSH), attendre alerte (REC-004).
4. Qualifier alerte : `nouvelle` → `en cours` → `clôturée` (REC-005).
5. Générer exports CSV et JSON (REC-006).
6. Consulter journaux d'audit (REC-002).
7. Vérifier `/health` (REC-009).
8. Produire rapport avec captures, exports et logs.

**Résultat attendu :** Chaîne complète visible : scan → actifs → événements → alerte → qualification → export → audit.

**Preuve :** Captures écran, fichiers CSV/JSON, logs, rapport synthétique.

### Synthèse des scénarios

| ID | Titre | Exigences couvertes | Résultat principal |
|---|---|---|---|
| REC-001 | Connexion utilisateur | F-AUTH-001, RM-001, SEC-001, F-AUD-001 | Accès valide, refus sans session |
| REC-002 | Contrôle permissions | F-AUTH-002/3, SEC-002 | Accès restreint par rôle |
| REC-003 | Scan réseau borné | F-DISC-001/2/3, F-ASSET-001, RM-002/3, SEC-007 | Actifs et ports découverts |
| REC-004 | Détection suspect | F-ALERT-001/2/3, RM-004 | Alerte générée après seuil |
| REC-005 | Cycle de vie alerte | F-ALERT-004, F-AUD-003, RM-005/7 | Statuts modifiés et audités |
| REC-006 | Export preuve | F-EXP-001/2/3, F-AUD-002, RM-006 | Fichiers CSV et JSON valides |
| REC-007 | Validation injection | SEC-003, RM-008, NF-QUAL-002 | Payload invalide rejeté |
| REC-008 | Latence interface | NF-PERF-001/3 | Réponse < 2s, export < 5s |
| REC-009 | Santé déployabilité | NF-OBS-001, NF-DEP-001/2 | `/health` OK, doc disponible |
| REC-010 | Démonstration complète | Toutes P1 | Chaîne complète démontrable |

---

## Section 3 — Sécurité et conformité

### 3.1. SEC-001 — Authentification obligatoire

JWT (HMAC-SHA256) avec `Authorization: Bearer <token>`. Middleware FastAPI sur toutes les routes protégées. Routes publiques : `/auth/login`, `/health`. Durée du token : 24h (configurable). Mots de passe hachés avec bcrypt (coût 12).

**OWASP ASVS :** V2 (Authentication).

### 3.2. SEC-002 — Contrôle d'accès par rôle (RBAC)

Rôles `admin` et `analyst`. Décorateur `@requires_role("admin")` sur les routes réservées. Vérification après JWT.

**Permissions :**

| Fonction | `admin` | `analyst` | Non auth. |
|---|---|---|---|
| Connexion | Oui | Oui | Non |
| Tableau de bord | Oui | Oui | Non |
| Scan réseau | Oui | Non | Non |
| Actifs et alertes | Oui | Oui | Non |
| Qualification alerte | Oui | Oui | Non |
| Export CSV/JSON | Oui | Oui | Non |
| Journaux d'audit | Oui | Non | Non |
| Administration utilisateurs | Oui | Non | Non |

**OWASP ASVS :** V4 (Access Control).

### 3.3. SEC-003 — Validation stricte des entrées

Schémas Pydantic avec regex IP/CIDR :
```
^(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?:/(?:[0-9]|[12][0-9]|3[0-2]))?$
```
Rejet des payloads invalides (422). Aucune exécution de commande système. Tests de résistance injections (commandes, SQL, XSS).

**OWASP ASVS :** V5 (Validation, Sanitization and Encoding).

### 3.4. SEC-004 — Contrôle d'accès aux exports

Fichiers dans répertoire non public. Téléchargement via endpoint authentifié `GET /exports/{id}/download`. Vérification rôle et appartenance. Nettoyage périodique (rétention configurable). Chiffrement AES-256 optionnel.

**OWASP ASVS :** V8 (Data Protection).

### 3.5. SEC-005 — Non-exposition des secrets

Variables d'environnement pour tous les secrets. `.env.example` documenté (valeurs factices). `.env` dans `.gitignore`. Revue de code systématique.

**Variables sensibles :** `SECRET_KEY`, `DATABASE_URL`, `AGENT_SECRET`, `REDIS_URL`.

**OWASP ASVS :** V8 (Data Protection).

### 3.6. SEC-006 — Journalisation des actions sensibles (Audit Trail)

Table `audit_logs` : `id`, `user_id`, `role`, `action`, `target_type`, `target_id`, `result`, `created_at`. Décorateur `@audit_logged`. Actions tracées : login, logout, export, alert_status_change, user_create/update/delete, scan_start, accès refusé. Consultation réservée à `admin`.

**OWASP ASVS :** V7 (Error Handling and Logging).

### 3.7. SEC-007 — Scan réseau borné

Plage autorisée dans `SCAN_ALLOWED_RANGES`. Validation serveur via `ipaddress` Python. Rejet 403 si hors plage. Logs des tentatives refusées.

### 3.8. SEC-008 — Scans furtifs (P2)

`SCAN_DELAY_MS` configurable (défaut : 100 ms). Mode SYN scan optionnel. P2 (non bloquant MVP).

### 3.9. Conformité OWASP ASVS

| Catégorie OWASP ASVS | Exigences BigBrowser | Statut MVP |
|---|---|---|
| V1 — Architecture | NF-ARCH-001/2, NF-QUAL-001 | ✅ Couvert |
| V2 — Authentication | SEC-001, F-AUTH-001, RM-001 | ✅ Couvert |
| V3 — Session Management | SEC-001 (JWT) | ✅ Couvert |
| V4 — Access Control | SEC-002, F-AUTH-002/3 | ✅ Couvert |
| V5 — Validation & Sanitization | SEC-003, RM-008, NF-QUAL-002 | ✅ Couvert |
| V6 — Storage Cryptography | SEC-005 (bcrypt) | ✅ Couvert |
| V7 — Error Handling & Logging | SEC-006, F-AUD-001/2/3, RM-007 | ✅ Couvert |
| V8 — Data Protection | SEC-004, SEC-005 | ✅ Couvert |
| V9 — Communications | NF-DEP-001/2 | ✅ Couvert |
| V10 — Malicious Code | SEC-003 | ✅ Couvert |
| V11 — Business Logic | RM-001 à RM-008 | ✅ Couvert |
| V12 — Files & Resources | SEC-004 | ✅ Couvert |

### 3.10. Conformité NIS2 (Directive 2022/2555)

| Exigence NIS2 | Réponse BigBrowser | Statut |
|---|---|---|
| Art. 21(2)(a) — Analyse des risques | Cartographie actifs (F-DISC-001/2/3), détection (F-ALERT-001) | ✅ |
| Art. 21(2)(b) — Gestion des incidents | Alertes (RM-004, F-ALERT-001 à 004), cycle de vie (RM-005) | ✅ |
| Art. 21(2)(c) — Continuité | Exports de preuve (F-EXP-001/2/3) | ✅ |
| Art. 21(2)(d) — Chaîne d'approvisionnement | Scan réseau, inventaire actifs | ✅ |
| Art. 21(2)(e) — Sécurité des réseaux | Supervision temps réel, heartbeat agents | ✅ |
| Art. 21(2)(f) — Évaluation efficacité | Rapports et exports (F-EXP-001/2/3) | ✅ |
| Art. 21(2)(g) — Gestion vulnérabilités | Détection ports ouverts, services | ✅ |
| Art. 21(2)(h) — Hygiène cyber | Traçabilité (RM-007, SEC-006) | ✅ |
| Art. 21(2)(i) — Tests de sécurité | REC-001 à 010, scénarios offensifs | ✅ |
| Art. 23 — Signalement incidents | Alertes actionnables, exports de preuve | ✅ |

### 3.11. Conformité RGPD

Minimisation des données : seules les données nécessaires sont collectées (username, password_hash, role, IP). Limitation de conservation (90 jours pour les logs). Sécurité : chiffrement bcrypt, JWT, contrôle d'accès. Droit d'accès et de suppression pour les administrateurs.

### 3.12. Synthèse des mesures de sécurité par couche

| Couche | Mesures |
|---|---|
| **Transport** | HTTPS obligatoire en production |
| **Authentification** | JWT (HMAC-SHA256), bcrypt (coût 12), durée limitée |
| **Autorisation** | RBAC (admin/analyst), décorateurs par route |
| **Validation entrées** | Pydantic, regex IP/CIDR, pas de shell |
| **Stockage** | Mots de passe hachés, exports protégés, chiffrement optionnel |
| **Journalisation** | Audit trail complet, logs structurés |
| **Configuration** | Variables d'environnement, `.env.example`, `.gitignore` |
| **Déploiement** | Docker isolé, réseau BBrowser_net, secrets Docker |

---

## Section 4 — Sources

### Référentiels normatifs et réglementaires

- [OWASP ASVS v4.0](https://owasp.org/www-project-application-security-verification-standard/)
- [NIS2 Directive 2022/2555](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive)
- [RGPD (Règlement UE 2016/679)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679)
- [France 2030](https://www.france2030.gouv.fr/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [NIST CSF 2.0](https://www.nist.gov/cyberframework)
- [OWASP Risk Rating](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology)
- [ANSSI](https://cyber.gouv.fr/)
- [OWASP Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html)

### Outils et technologies

- [Pydantic](https://docs.pydantic.dev/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [JWT.io](https://jwt.io/)
- [bcrypt](https://pypi.org/project/bcrypt/)
- [pytest](https://docs.pytest.org/)
- [httpx](https://www.python-httpx.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

### Documents de cadrage interne

| Source | Chemin relatif |
|---|---|
| Cahier des charges BigBrowser v1.0 | `../rendu_principal.md` |
| Architecture définitive | `../../08_architecture/rendu_principal.md` |
| Feuille de cadrage projet | `../../01_documents_pedagogiques/rendu_principal.md` |
| Business Model | `../../03_business_model/rendu_principal.md` |
| Business Plan | `../../04_business_plan/rendu_principal.md` |
| Étude de marché | `../../02_etude_de_marche/rendu_principal.md` |
| Gestion de projet | `../../05_gestion_de_projet/rendu_principal.md` |
| Registre des références transverses | `../../90_references_transverses/README.md` |

### Sources de données marché

| Source | Donnée | URL |
|---|---|---|
| Mordor Intelligence | Marché cybersécurité 250 Mds $ | https://www.mordorintelligence.com |
| PAC | Marché français IT | https://www.pac-online.com |
| OPIIEC | Observatoire métiers numérique | https://www.opiiec.fr |
| Gartner | Magic Quadrant SIEM | https://www.gartner.com |
| ANSSI | Rapport d'activité | https://www.ssi.gouv.fr |
| Cybermalveillance.gouv.fr | Statistiques PME | https://www.cybermalveillance.gouv.fr |
| Insee | Démographie PME/ETI | https://www.insee.fr |

---

*Document consolidé le 26 mai 2026. Remplace les fichiers `01_exigences_referentielles.md`, `02_scenarios_recette.md`, `03_securite_conformite.md` et `04_sources_reference.md`.*
