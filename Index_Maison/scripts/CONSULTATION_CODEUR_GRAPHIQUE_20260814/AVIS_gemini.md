# AVIS gemini (provider Google Gemini, 4.6s)

### 1. AMELIORATIONS_PROTOTYPE (Revue du script `scripts/graph_trades_btc.py`)

Le prototype est bien conçu (stdlib uniquement, HTML autonome, canvas pur), mais présente quelques axes d'optimisation pour la robustesse et les gros volumes de données :

*   **Gestion des fichiers CSV *append-only* énormes :** Lire l'intégralité d'un CSV volumineux en mémoire avec `csv.DictReader` peut saturer la RAM si le run dure plusieurs jours. Il faut ajouter un mécanisme de lecture inversée ou filtrer à la volée via l'argument `--since` dès l'ouverture du fichier.
*   **Pagination / Limite de l'API Binance Klines :** L'endpoint `/fapi/v1/klines` est limité à 1500 bougies par requête. Si le run dépasse 25 heures en unité 1m, le script actuel n'interroge pas les blocs précédents. Il faut implémenter une boucle de pagination rétroactive (`startTime` / `endTime`).
*   **Robustesse du Parsing Temporel :** Assurer la conversion systématique des timestamps en UTC pur (`datetime.timezone.utc`) pour éviter les décalages d'heures locales lors du rapprochement bougies/trades.
*   **Échelle de prix (Axis Scaling) :** Si les trades comportent des micro-mouvements ou si le BTC subit un flash crash, normaliser le min/max du canvas avec une marge (ex: ±0.2%) évite que les mèches ne collent aux bords supérieur/inférieur du canvas.

---

### 2. PLAN_INTEGRATION (Pour le Cockpit `127.0.0.1:17800`)

Pour intégrer le graphique sans modifier le monolithe `index.html` (4362 lignes) et sans impacter le moteur :

*   **Étape 1 : Externalisation de la vue**
    Créer un nouveau module JS autonome `cockpit/js/btc_chart_widget.js` contenant la logique de dessin sur canvas et de récupération des données.
*   **Étape 2 : Création d'un endpoint léger (ou réutilisation du pont)**
    Ajouter une route simple dans le serveur HTTP existant (ou le pont Cortana sur le port `17777`) qui renvoie directement le JSON des klines et le dernier CSV filtré, évitant au navigateur d'interroger Binance en direct (contournement CORS + centralisation).
*   **Étape 3 : Injection non invasive dans le DOM**
    Ajouter un nouvel onglet ou un panneau repliable (accordion) dans l'interface du cockpit existant via un conteneur `<div id="btc-chart-panel"></div>` sans toucher aux panneaux critiques (radar/synapses).
*   **Étape 4 : Chargement asynchrone**
    Initialiser le graphique à la demande (au clic sur l'onglet dédié) pour ne pas consommer de cycles CPU/mémoire sur le thread principal du navigateur pendant que le run tourne.

---

### 3. RISQUES (Ce qui peut casser)

*   **Surcharge du Navigateur (DOM / Canvas) :** Redessiner un canvas 1m avec des centaines de trades à chaque tick de rafraîchissement du cockpit va provoquer des chutes de FPS et faire figer l'interface. *(Solution : Rendu statique à la demande ou rafraîchissement bridé à toutes les X minutes).*
*   **Conflits CSS / Layout :** Le cockpit utilise potentiellement des grilles CSS strictes ou du positionnement absolu. Insérer un canvas responsive non contraint risque de casser la disposition des panneaux adjacents.
*   **Blocage Réseau (CORS) :** Si le script JS du navigateur tente d'appeler l'API Binance Klines directement, les politiques CORS bloqueront la requête (nécessite de passer par le serveur local du cockpit).

---

### 4. RECOMMANDATION FINALE

👉 **Attendre la validation humaine du prototype hors-cockpit (Statut : RECOMMANDÉ).**

**Justification :** Le moteur est actuellement en cours de test (run 4h en conditions réelles). Le principe cardinal du trading algorithmique est de **ne jamais modifier un système qui tourne**. Le prototype hors-cockpit remplit parfaitement son rôle d'audit visuel sans aucun risque pour l'intégrité du port `17800` ou du moteur ACE777. 

Validez d'abord la pertinence visuelle des trades sur vos 4h de testnet via le script externe. Une fois le run terminé et validé, l'intégration propre pourra être planifiée pour le prochain run.
