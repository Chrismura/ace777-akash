# AVIS codeur (provider Puter Grok (gratuit), rotation 1)

**AMELIORATIONS_PROTOTYPE**

- Lecture CSV : passer à `csv.DictReader` + validation stricte des colonnes + détection automatique du dernier timestamp valide (permet de ne pas re-traiter tout le fichier sur un CSV append-only très gros).
- Récupération klines : ajouter `urllib` avec timeout + retry exponentiel (3 essais max) + gestion propre des erreurs 429/5xx. Éviter de tout re-télécharger à chaque run en gardant un cache simple en mémoire (dict timestamp → close).
- Logique métier : séparer clairement trois fonctions (`load_trades`, `fetch_klines`, `render_html`). Ajouter un petit index temporel (dict ts → kline) pour le positionnement des points au lieu de boucles O(n²).
- Gestion trades ouverts : filtrer ou marquer explicitement les lignes sans `exitPrice` (ou avec `exitReason == "OPEN"`).
- HTML/canvas : pré-calculer les min/max une seule fois, utiliser `requestAnimationFrame` pour le tooltip, et limiter le nombre de points dessinés (regroupement visuel si > 500 trades).
- Robustesse : passer `--since` en epoch ms directement et ignorer les trades antérieurs dès la lecture CSV (gain mémoire et temps sur gros fichiers).

**PLAN_INTEGRATION** (le plus propre et le moins intrusif)

1. Créer un nouveau fichier `cockpit/graph_trades.js` autonome (fonctions `fetchTrades(since)`, `drawTradesOnCanvas(ctx, trades, klines)`, tooltip).
2. Ajouter un seul `<canvas id="trades-btc">` dans un panneau existant du `index.html` (idéalement à côté du radar ou dans un onglet "Charts" déjà présent) sans toucher à la structure globale.
3. Côté serveur : exposer un endpoint très léger (`/api/trades?since=...`) qui lit uniquement les lignes récentes du CSV (seek + lecture ligne par ligne) et renvoie un JSON compact `{trades: [...], klines: [...]}`. Le pont cortana (17777) peut servir de relais si on veut éviter de toucher le serveur principal.
4. Dans le JS du cockpit, charger le module `graph_trades.js` de façon dynamique (`import` ou script tag) uniquement quand l’utilisateur active la vue, et ne faire le fetch que sur demande.
5. Aucune modification du moteur ni du run en cours.

**RISQUES**

- Toute modification directe de `index.html` (4362 lignes) peut casser le layout ou le rendu canvas existant (radar/synapses).
- Un fetch supplémentaire pendant le run peut créer de la contention sur le CSV si le moteur écrit en même temps (risque faible mais réel sur append-only sans flush explicite).
- Ajout de canvas + event listeners peut dégrader les perfs du cockpit si le dessin n’est pas optimisé (surtout avec beaucoup de trades).
- Endpoint mal implémenté pourrait bloquer le thread HTTP du serveur local.
- Le prototype hors-cockpit est déjà validé ; l’intégration prématurée expose le système à des bugs visuels ou de données pendant un run testnet.

**Recommandation** : **attendre validation humaine du prototype**.

Le prototype est déjà fonctionnel et testé (167 bougies / 24 trades). La décision humaine explicite était d’intégrer **seulement si** le prototype s’avère vraiment utile. Tant que cette validation n’est pas faite, il est plus sûr de laisser le cockpit intact et de continuer à itérer sur le script standalone. Intégration seulement après un retour positif explicite du superviseur.
