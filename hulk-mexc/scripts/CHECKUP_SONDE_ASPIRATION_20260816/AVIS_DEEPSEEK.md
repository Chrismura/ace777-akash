# AVIS DEEPSEEK (provider NVIDIA build.nvidia.com (100+ modeles))

1. **VERDICT** : GO AVEC RÉSERVES. Le code est propre, fail-open correct, normalisation temporelle GROK appliquée, seuil 500$ JUGE respecté. Réserve principale : le mode OBSERVATION ne calibre rien tant que le CSV n'est pas analysé — c'est un GO conditionnel à l'exploitation des données dans 48h.

2. **ANGLES MORTS** :
   - **Spoof mal détecté** : le seuil 15%/s est arbitraire, non calibré. Un mur qui fond à 14%/s sur 2 lectures sera classé "aspiration" alors que c'est du spoof lent. Le critère de reconstruction (≤10% de différence) est trop strict : un mur qui revient à 12% près est déjà un spoof.
   - **Rate-limit MEXC** : `ASPIRATION_MAX_PAIRS=5` × `PROBE_EVERY=3` cycles = 5 paires × 2 lectures toutes les ~3s = 10 requêtes/3s. MEXC limite à 20 req/s par IP — OK, mais si le cycle moteur accélère (régime IMPULSE), tu passes à 10 req/s sans marge.
   - **CSV non protégé** : si le fichier est verrouillé par un autre process (lecture pendant écriture), `csv.writer` lève une exception non catchée → crash de `probe_aspiration()` → le moteur continue mais la sonde meurt silencieusement.

3. **AMÉLIORATION CONCRÈTE** : **Calibration dynamique du seuil spoof**. Au lieu du 15%/s fixe, utilise la médiane glissante des `drop_*_pct_per_s` sur les 100 derniers échantillons par paire (stockée dans `self.aspiration_prev`). Le spoof est déclaré si `drop_now > 3 × médiane` ET reconstruction ≤10%. Ça s'adapte à la volatilité réelle du marché, pas à un chiffre sorti du chapeau.

4. **CLAUSE PERMANENTE — PROPOSITION** : **Passe de la double lecture à une lecture unique + historique**. L'aspiration ACE V8 se base sur l'évolution du carnet sur plusieurs secondes, pas 2 snapshots à 0.5s. Au lieu de `aspiration_sense()` qui fait 2 requêtes, garde un buffer de 10 lectures espacées de 0.5s (soit 5s d'historique) et calcule la pente de régression linéaire sur `wall_bid_usdt` et `wall_ask_usdt`. Ça donne :
   - Une pente robuste (moins de bruit qu'un delta sur 2 points).
   - Une détection spoof naturelle : si la pente s'inverse dans les 2 dernières lectures, c'est un spoof.
   - Un seul appel API par échantillon (rate-limit divisé par 2).
   Coût : 10 lectures en mémoire par paire, mais on est à 5 paires max → 50 flottants, trivial.
