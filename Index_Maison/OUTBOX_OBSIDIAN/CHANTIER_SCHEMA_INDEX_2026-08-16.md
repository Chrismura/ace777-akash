# 🗺️ CHANTIER — SCHÉMA DE TOUS LES INDEX (16/08/2026)

> Demande Christophe : « faire un schéma de tous les index » + « ça peut pas servir d'indice, du genre moyen ? »
> Réponse : OUI — la sonde aspiration Hulk peut devenir un indice agrégé (le 7ᵉ d'Ada), au même format que les 6 existants.

---

## 1. Les sources brutes (thermo/live.json)

Chaque champ brut, lu depuis `Index_Maison/thermo/live.json` (fallback `cockpit/mission.json`).

| Champ | Sens | Unité |
|---|---|---|
| `mark` | prix BTC | USDT |
| `oi` | open interest | contrat |
| `funding` / `fundingAvg30` | funding instantané / moyenne 30 j | % |
| `longShort` | ratio positions long/short | ratio |
| `chg24` / `chg1h` / `chg4h` | variation prix | % |
| `volQuote` | volume 24 h | USDT |
| `btcDominance` | dominance BTC | % |
| `panierDownPct` | baisse du panier de paires | % |
| `whaleN` / `whaleUsd` / `whaleMax` | baleines détectées | n / USDT |
| `takerRatio` | ratio taker acheteur/vendeur | ratio |
| `topTraderLS` | ratio long/short top traders | ratio |
| `fearGreed` | indice peur/avidité | 0-100 |
| `marketCapUsd` | capitalisation crypto | USDT |
| `altSeason` / `altSeasonScore` | saison altcoins | score |
| `liq24Usd` / `liqLongUsd` / `liqShortUsd` | liquidations 24 h | USDT |
| `etfBtcM` / `etfEthM` / `etfXrpM` | flux ETF | M$ |
| `gexPutCall` / `gexCallWall` / `gexPutWall` | GEX options | ratio/USDT |
| `volumeCachedTaker` | volume taker caché | USDT |
| `onchain` (whaleCumul24hBtc, whaleDir, cpfpSignal) | onchain baleines / CPFP | BTC / signal |

---

## 2. Les index dérivés — Ada SAISON (`ada_saison.py`)

6 signaux déterministes → **alignement** → **SAISON**.

| Indice | Lit | Direction | Force | Seuils |
|---|---|---|---|---|
| 🌡️ température | climate, score | neutre | 0-2 | hot=2, warn=1, score≥70 |
| 💓 pouls | funding | long/short/neutre | 0-2 | \|funding\|≥0.05% |
| 🛁 bassin | deltas.oi.dir | long/short/neutre | 0-1 | up/down |
| 🌀 vortex | chg24 | long/short/neutre | 0-2 | ≥1% = 2, ≥0.3% = 1 |
| 🐝 essaim | longShort, takerRatio, fearGreed | long/short/neutre | 0-2 | LS>1.5 / <0.8, taker>0.55, FG<25 ou >75 |
| 🐋 baleines | whaleN, whaleUsd | neutre | 0-1 | n≥3 ou usd≥5M |

**Alignement** : nb_long, nb_short, score = |nb_long−nb_short|/max(1,total), direction majoritaire.

**Saison** (règles de priorité) :
- `CHAOS ⛈️` : liq24 ≥ 50 M$ ET (vol=2 ou funding chaud)
- `MOUVEMENT 🌀` : score ≥ 0.6 ET ≥ 3 indices alignés ET vol ≥ 1
- `CHAUFFE 🌡️` : température ≥ 1 ET (funding chaud ou OI long)
- `ACCUMULATION 💧` : OI long ET vol=0 ET funding neutre
- `CALME 🧊` : sinon

Sorties : `strategie/ada_saison_live.json` (live + état + archive JSONL, rotation 2 Mo).

---

## 3. Les index de la GARDIENNE (`ada_gardienne.py`)

Lit la saison + thermo + journal → **pressions** → **voilure** → **zone**.

| Pression | Formule | Rôle |
|---|---|---|
| 🩸 bleed | perte/ancrage (relatif) + vitesse de chute | saignement de la session |
| ⛈️ storm | saison_map × 0.6 + intensité (funding, chg24, liq, fear) × 0.4 | tempête marché |
| 🔄 reversal | part du camp opposé dans l'alignement | retournement |

**Voilure** = 100 × (1 − lissage(0.40×bleed + 0.40×storm + 0.20×reversal)) × modulateurs (onchain ±7%, CPFP ×0.93).

**Zone** : VERT ≥70 % 🟢 · JAUNE ≥45 % 🟡 · ROUGE 🔴 · PRENDS_LA_PERTE ⛔ (perte ≥ seuil X relatif).

Sirènes instantanées (pas de lissage) : bascule de saison, CHAOS, funding ≥ 3× moyenne, liq ≥ 50 M$, vortex force 2, chute ≥ 30 %.

Sorties : `strategie/ada_gardienne_live.json` + historique roulant (60 scans).

---

## 4. Les index HULK (paper MEXC, `ace_sense_mexc.py` + `paper_diprip.py`)

| Signal | Lit | Rôle |
|---|---|---|
| régime | score_pair (15 j) | WATCH / COOLING / IMPULSE / IMPULSE_WAIT |
| tension | move6 / cadence (+ dd) | orage ≥ 2.5 = intéressant |
| sense (book) | spread, profondeur, imbalance, murs | gate d'entrée |
| **aspiration** (nouveau) | **double lecture carnet** | drop_bid/ask %/s, side, spread_delta, price_delta, **btc_delta** |
| vol_spike | vol24 / cadence | small caps vs liquides |
| spoof | mur reconstruit après fonte | debounce « rétractable à maintenant » |

CSV calibration : `runs/ASPIRATION_CALIB_*.csv` (48 h observation, zéro effet moteur).

---

## 5. ➕ LE 7ᵉ INDICE PROPOSÉ — « BASSIN HULK » (sonde agrégée)

**Format identique aux 6 d'Ada** (direction, force, brut) — intégration dans `ada_saison.py::signaux()` :

| Champ | Calcul |
|---|---|
| direction | majorité des `aspiration_side` sur les paires actives (BUY > SELL → long) |
| force | intensité médiane des `max_drop_pct_per_s` (0 = calme · 1 = mouvement · 2 = tempête) |
| brut | médiane des drops + compteur paires BUY/SELL |
| **filtre BTC** | signal neutralisé si `btc_delta_pct` fort (la marée BTC domine les small caps) |

**Effet dans la chaîne Ada** : entre dans l'alignement (1 voix de plus), donc dans la saison, donc dans la voilure. C'est la première vue **micro** (murs des 15 paires) dans un système qui ne voyait que le **macro** (BTC).

**Étapes (après les 48 h d'observation)** :
1. Analyser `ASPIRATION_CALIB_*.csv` : la sonde prédit-elle les moves (price_delta) ?
2. Si justesse > 60 % → activer l'effet sur les entrées Hulk (V2).
3. En parallèle : ajouter l'indice agrégé dans `ada_saison.py` (mode ombre d'abord, affichage seulement).

---

## 6. Cortana / Kelly (conseil, pas index)

| Signal | Rôle |
|---|---|
| justesse Cortana | % des propositions correctes (ADVISORY < 60 %) |
| kelly_ombre | sizing calculé, jamais appliqué (ombre) |

---

## Notes

- **Ne rien toucher au moteur** : `ada_saison.py`, `ada_gardienne.py`, genesis ACE sont intouchés par la sonde.
- Le 7ᵉ indice se branche côté Ada (lecture seule des CSV Hulk), pas dans Hulk.
- Registre md5 : `paper_diprip.py` / `ace_sense_mexc.py` / `defaults.env` déclarés 16/08 22:45Z.
