# AVIS JUGE (provider NVIDIA build.nvidia.com (100+ modeles))

## 1. VERDICT

**GO AVEC RESERVES** — le code est propre, fail-open correct, spoof rétractable implémenté comme demandé. Les réserves : seuil spoof à 15%/s est arbitraire, et le mode observation 48h est le bon filet.

## 2. Angles morts

- **`aspiration_side = "NONE"` quand `max_drop <= 0`** : si les DEUX murs fondent (marché qui se resserre des deux côtés), tu classes en NONE alors que c'est une aspiration bidirectionnelle — information perdue.
- **Spoof : comparaison `w_now` vs `w_prev` sur la même paire** — mais `aspiration_prev` est écrasé à CHAQUE probe. Si le mur fond puis se reconstruit entre deux probes (3 cycles = ~1.5s), tu rates le spoof. Le debounce est là, mais la fenêtre de détection est trop courte.
- **`drop_bid_pct_per_s` peut être négatif** (mur qui grossit) — ton `max(abs(...))` dans le spoof masque la direction. Un mur qui GROSSIT de 15%/s n'est pas un spoof, c'est un mur qui se renforce.
- **CSV : pas de flush explicite** — si le process crashe, les dernières lignes sont perdues. `csv.writer` bufferise.
- **Rate-limit MEXC** : 5 paires × 2 lectures × 1 probe/3 cycles = ~3.3 req/s en pic — proche de la limite MEXC (20 req/s). OK mais marge faible si d'autres appels cohabitent.

## 3. Amélioration GO-sized

**Ajoute `drop_direction` au retour** : `"BOTH"` si les deux murs fondent > 5%/s, `"BUY"`/`"SELL"` sinon. Ça capture l'aspiration bidirectionnelle (marché qui se resserre) et évite de la jeter en NONE. 3 lignes dans `aspiration_sense()`.

## 4. CLAUSE PERMANENTE — proposition alternative

**Passe de la double lecture à la TRIPLE lecture** (t0, t0+0.5s, t0+1.0s) sur les paires les plus actives seulement (top 2 au lieu de 5). Pourquoi : le spoof classique est un mur qui fond PUIS se reconstruit — avec 2 lectures tu ne vois que la fonte, avec 3 tu vois la reconstruction et tu qualifies le spoof avec certitude, pas avec un seuil arbitraire de 15%. Coût : 1 lecture de plus par probe, mais sur 2 paires au lieu de 5 = même charge API. Et tu sors du mode observation avec un détecteur de spoof PROUVÉ, pas calibré au doigt mouillé.
