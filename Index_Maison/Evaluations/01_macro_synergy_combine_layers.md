# Éval #1 — @macro_synergy / combine fundamentals + sentiment + price

- **Date :** 2026-07-28
- **Source compte :** [Ralph Sueppel @macro_synergy](https://x.com/macro_synergy) (Macrosynergy, Londres — vrai quant macro, pas un farm WTF)
- **Post ciblé :** « How to Combine Fundamentals, Sentiment, and Price Into One Backtest (Python) »
- **Lien tweeté :** Medium `@axionquant/...` (curation ; l’écosystème maison = [macrosynergy.com](https://macrosynergy.com) + package GitHub `macrosynergy/macrosynergy`)

## Verdict Cursor

| | |
|--|--|
| **Compte** | **Bonne adresse** — flux papers + Python sérieux (pas Brady Long) |
| **Idée post** | **SEMI-VRAI / garder le pattern**, pas le stack JPMaQS entier |
| **Thermo maison ?** | **Oui (inspiré)** — combiner 2–3 signaux ≠ un seul prix |
| **Trend maison ?** | **Oui (inspiré)** — facteurs lents + prix |
| **Utile ACE/Hulk hot ?** | **Non** — trop lourd, data macro payante / mensuelle |
| **Action** | Extraire le **cadre** ; ignorer le produit commercial JPMaQS pour l’instant |

## Ce qu’il y a de bon (à prendre)

1. **Séparer les couches** puis les fusionner en un signal : prix + (chez eux) macro/sentiment — chez nous : **prix BTC/panier + tension/univers Hulk + (plus tard) sentiment veille**.
2. **Point-in-time / pas de look-ahead** — règle d’or backtest (utile si on historise le thermo).
3. **Combinaison simple d’abord** (somme pondérée / parity) avant ML (`SignalOptimizer`) — pour un Mac 8 Go et un gate soft, la version simple gagne.
4. **Un signal → un régime** — exactement thermo (chaud/froid) + biais trend.

## Ce qu’on jette / on n’adopte pas maintenant

- Dépendance **JPMaQS / DataQuery** (macro institutionnel) — hors scope ACE paper.
- RL market-neutral, NN portfolio weights (autres tweets du compte) — **bruit** pour Hulk dip/rip.
- Remplacer le champion ACE par un backtest Medium.

## Mapping vers Index Maison

| Leur vocabulaire | Notre sauce |
|------------------|-------------|
| Fundamentals | (plus tard) funding / OI / dominance — pas obligatoire v1 |
| Sentiment | veille Hulk hints + Fear proxy optionnel |
| Price | **BTC + panier index maison** (cœur v1) |
| One backtest signal | `regime = f(thermo, trend)` → SKIP_BUY / size |

## Tweets récents du compte (coup d’œil)

Surtout des **papers** : DRL market-neutral, portfolio + macro NN, leverage effect, inflation Fed, surprises éco + code Macrosynergy, vol trading guides…  
→ Compte **à garder en watchlist Index** (idées trend/régime), pas à copier trade par trade.

## Décision proposée

- **Garder :** pattern « multi-couches → un score → backtest honnête ».
- **Pour v1 thermo/trend :** BTC (+ panier) d’abord ; sentiment = couche 2 ; fundamentals = couche 3 ou jamais.
- **Prochaine idée :** envoie le lien suivant.
