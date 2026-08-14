# AVIS gemini (provider Google Gemini, 6.0s)

### 1. AMÉLIORATIONS_PROTOTYPE (Revue du script `scripts/graph_trades_btc.py`)

Le prototype est remarquable par son approche "zéro dépendance" (stdlib Python pure), mais pour un usage en conditions réelles (runs longs, gros volumes de données), plusieurs optimisations de robustesse et de performance s'imposent :

1. **Gestion des fichiers CSV "append-only" massifs :**
   * *Problème actuel :* Lecture intégrale du CSV en mémoire à chaque exécution. Si le fichier atteint des centaines de mégaoctets après 24h/48h de run, le script va saturer la mémoire et ralentir.
   * *Amélioration :* Utiliser un générateur ou `collections.deque` avec une limite, ou filtrer les lignes à la volée dès l'ouverture du fichier (surtout avec le paramètre `--since`).
2. **Robustesse de l'API Binance Testnet (Klines) :**
   * *Problème actuel :* Pas de retry en cas de coupure réseau ou de rate-limit (HTTP 429/418) sur l'endpoint `/fapi/v1/klines`.
   * *Amélioration :* Implémenter un mécanisme de retry exponentiel simple (3 essais max avec `time.sleep`) via `urllib.request`.
3. **Paginage des requêtes Klines (limite Binance à 1500 bougies) :**
   * *Problème actuel :* Si le run dépasse 25 heures en unité 1m (1500 bougies), une seule requête ne suffira pas.
   * *Amélioration :* Boucler sur le paramètre `startTime` pour récupérer l'historique par tranches si `--since` est très ancien.
4. **Optimisation du rendu HTML/Canvas :**
   * *Amélioration :* Éviter de dupliquer les données JSON dans le HTML si le dataset est très grand, et s'assurer que le script JS gère bien le *downsampling* visuel (si 10 000 bougies sur un écran de 1200px, fusionner les ticks min/max pour garder des mèches propres sans saturer le Canvas 2D).

---

### 2. PLAN_INTEGRATION (Intégration Cockpit non-intrusive)

Pour respecter la règle d'or (*NE RIEN casser, NE PAS toucher au run*), l'intégration doit être **découplée** et **modulaire**.

* **Étape 1 : Création d'un module JS dédié**
  * Créer un fichier `cockpit/js/btc_trades_render.js` contenant la logique de dessin du canvas (reprise épurée du prototype).
* **Étape 2 : Ajout d'un panneau repliable dans le Cockpit (`index.html`)**
  * Ajouter un nouveau bloc `<div class="panel" id="btc-graph-panel">` dans une zone neutre de la grille existante (ex: sous le radar ou à côté des synapses), muni d'un bouton "Afficher/Masquer le Graph BTC". Aucun impact sur les 4362 lignes existantes si on encapsule le code.
* **Étape 3 : Exposition des données via le Pont Cortana (Port 17777) ou endpoint dédié**
  * Plutôt que de parser le CSV côté client (lourd en JS), ajouter une route légère dans le serveur Python du pont cortana (ou un script annexe) qui lit le CSV du run actif, filtre les données, et renvoie un JSON propre (`/api/btc_trades_data`).
* **Étape 4 : Fetch asynchrone léger**
  * Le JS du cockpit appelle `fetch('/api/btc_trades_data')` toutes les X minutes ou au clic, et met à jour le canvas localement.

---

### 3. RISQUES (Ce qui peut casser le cockpit ou le moteur)

1. **Concurrence sur le fichier CSV :** Si le moteur ACE777 écrit dans le CSV au moment exact où le script de graphe ou le pont le lit, risque de `PermissionError` (sous Windows) ou de lecture de ligne tronquée (partielle). *Mitigation :* Copier le CSV dans un fichier temporaire `/tmp` avant lecture, ou utiliser un verrouillage doux.
2. **Surcharge du DOM / Fuite mémoire JS :** Un canvas pur mal nettoyé ou des écouteurs d'événements (survol infobulle) mal gérés sur une page de 4362 lignes (`index.html`) peuvent ralentir le navigateur à force de rafraîchissements.
3. **Effet de bord CSS dans le monolithe :** Modifier `index.html` ou injecter des styles globaux peut casser la grille existante du cockpit. *Mitigation :* Isoler le CSS du nouveau panneau dans un bloc préfixé (`#btc-graph-panel ...`).

---

### 4. RECOMMANDATION DU CODEUR

> **🎯 RECOMMANDATION : Attendre la validation humaine du prototype (Option 2)**

* **Pourquoi ?** Le moteur tourne en testnet (run 4h critique). Même si l'intégration est conçue pour être propre, modifier `index.html` ou le serveur du pont en plein run comporte un risque inutile. 
* **La bonne tactique :** 
  1. Valider et stabiliser le script autonome `scripts/graph_trades_btc.py` (en appliquant les améliorations de robustesse API / pagination Klines).
  2. Laisser le superviseur exploiter le HTML généré hors-cockpit pour analyser ses points d'entrée/sortie sur ce run 4h.
  3. Une fois le run terminé et les stratégies validées, procéder à l'intégration propre dans le cockpit (via le plan modulaire ci-dessus) pour les futurs runs de production.
