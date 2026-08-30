# TOUR 3 (4 s)

ENCORE UNE AMELIORATION :

**1. Angles morts extrêmes et remparts (Niveau 4)**
*   **État sans fichier (Crash RAM pure / SSD plein)** : *Angle mort* : Si le disque renvoie `ENOSPC`, l'écriture atomique échoue et l'état volatile est perdu. *Rempart N4* : Réserve d'urgence de 2 Mo allouée au démarrage (`os.ftruncate` d'un fichier tampon) supprimée uniquement en cas d'alerte critique pour permettre l'écriture du dernier log d'erreur.
*   **Double panne simultanée (API down + Horloge système compromise)** : *Angle mort* : NTP dérive de 2 heures pendant que l'API secondaire est en 503, faussant le TTL de fraîcheur. *Rempart N4* : Le TTL utilise un compteur de blocs Bitcoin (`block height`) extrait directement du dernier payload valide, s'affranchissant totalement de l'horloge système.
*   **Acteur menteur "Counterfeit Healthy" (Zombie intelligent)** : *Angle mort* : Le processus répond au heartbeat, met à jour le fichier et l'âge du canari, mais sa boucle d'analyse IA (Cortana) est bloquée dans un thread mort ou génère des données factices statiques. *Rempart N4* : Le heartbeat est un *challenge-response* cryptographique. Le superviseur injecte une transaction-test fictive (poussière connue) ; le worker doit la retrouver dans le hash de sortie du cycle. Si le hash ne correspond pas au challenge, le worker est déclaré "mentant" et tué instantanément.

**2. (A) Fonctionnement (Synthèse)**
*   Orchestrateur mono-thread synchrone piloté par `launchd` (toutes les 30s).
*   Zero dépendance externe (stdlib Python uniquement), empreinte mémoire stricte < 250 Mo (purge via `malloc_zone_pressure_relief`).
*   Persistance locale impérative (`./state/`) pour les backoffs, le state de bascule multi-source et le challenge-response.

**3. (B) Détection (Seuils chiffrés)**
*   **Mort silencieuse** : Heartbeat / Challenge non résolu > 45 s.
*   **Fichiers figés** : SHA-256 invariant sur 3 cycles consécutifs.
*   **Score saturé** : 0 ou 100 maintenu > 5 min.
*   **Carnet vide** : 0 tx dust détectées > 60 s.
*   **Aveugle API** : 3 erreurs consécutives (bascule immédiate sur source B).
*   **Hiérarchie de surveillance** : `launchd` surveille le Superviseur. Le Superviseur exécute le *Challenge-Response* sur le Worker Cortana.

**4. (C) Évaluation**
*   **Indécis** : Score = 0 (Ni bon ni mauvais, rejeté du calcul de justesse).
*   **Abstention** : Échantillon $N < 30$.
*   **Nullité** : Données manquantes > 20% sur la fenêtre.
*   **Verdict Marché** : Valide si $N \ge 30$ sur 7 jours ET justesse $\ge 60\%$
