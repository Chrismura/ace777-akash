# AVIS codeur (provider Puter Grok (gratuit), rotation 2)

**AMELIORATIONS_PROTOTYPE**

- Remplacer le chargement complet du CSV par un générateur + `csv.DictReader` + filtrage précoce sur `--since` (évite de charger 100k+ lignes en RAM sur un fichier append-only).
- Remplacer la boucle naïve de positionnement des trades sur les bougies par `bisect` sur les timestamps des klines (O(log n) au lieu de O(n) par trade, plus propre et plus rapide).
- Ajouter un retry + backoff léger + timeout sur l’appel klines (urllib) + gestion explicite des erreurs 429/5xx Binance testnet.
- Découper le script en 4 fonctions pures : `load_trades`, `fetch_klines`, `align_trades_to_candles`, `render_html`. Le reste (parsing arguments, écriture fichier) reste dans `main`.
- Stocker les trades alignés dans une structure légère (liste de tuples) plutôt que de multiplier les dictionnaires ; le HTML généré gagne ~15-20 % de taille.
- Ajouter un paramètre `--limit` (défaut 500 bougies) pour éviter de télécharger trop de klines quand le CSV est très ancien.

Ces changements restent 100 % stdlib, n’augmentent pas la complexité et améliorent lisibilité + robustesse sans toucher au moteur.

**PLAN_INTEGRATION** (le plus propre et le moins intrusif)

1. Créer `cockpit/graph_trades.js` (nouveau fichier) contenant uniquement la logique canvas + tooltip (copie/adaptation du code du prototype).
2. Ajouter dans `index.html` (à un endroit bien délimité, ex. après le canvas radar) un nouveau `<div id="trades-panel">` contenant un `<canvas id="btc-trades">` + un petit header avec les contrôles (bouton refresh, plage since). Le tout dans un panneau repliable existant si possible.
3. Côté serveur (pont cortana ou le serveur HTTP 17800), ajouter une route minimale `/api/trades-graph?since=...` qui renvoie un JSON compact `{klines: [...], trades: [...]}` généré à la volée à partir du dernier CSV FILLED (sans bloquer le thread moteur).
4. Dans le JS du cockpit, charger ce JSON uniquement quand l’utilisateur ouvre le panneau (lazy). Aucun polling automatique.
5. Aucun autre fichier modifié, aucune dépendance ajoutée, le canvas existant (radar, synapses) reste intact.

**RISQUES**

- Collision d’ID ou de style sur le gros `index.html` (4362 lignes) → risque de casser l’affichage du cockpit entier.
- Si la nouvelle route `/api/trades-graph` lit le CSV pendant qu’il est en écriture append, possible lecture partielle (même si rare sur un fichier local).
- Ajout de canvas + JS peut légèrement augmenter la consommation mémoire du navigateur quand le panneau est ouvert (mais négligeable).
- Aucun risque direct sur le moteur ACE777 tant qu’on ne touche ni au run ni aux fichiers de trades en écriture.

**Recommandation**

**Attendre validation humaine du prototype.**

Le prototype est déjà fonctionnel et testé (167 bougies / 24 trades). Intégrer maintenant dans le cockpit de 4362 lignes alors que la décision humaine explicite est « seulement si vraiment utile » introduit un risque inutile de régression visuelle ou de maintenance. Une fois que le superviseur aura confirmé que le graphique lui apporte une vraie valeur ajoutée en conditions réelles, on applique le plan ci-dessus en une seule passe propre et non-intrusive.
