# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-22T03:39Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `60/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78669.37 | prix |
| OI | 106092.924 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.811e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.052 | crowd |
| BTC 1h/4h/24h | 0.25 / 0.45 / 5.6 % | B7 |
| Dominance BTC | 58.53% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat ATTENTION (score 60/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.811e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.052.
- BTC 24h 5.6% · 1h 0.25% · 4h 0.45%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.279 · OI 106092.924 (pas de dark pool free temps réel).
- Top traders L/S 1.136.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.69 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.53%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 231.02 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.615 · murC 80000 (+1.7%) · murP 60000 (-23.7%).
- Volumes cachés proxy : taker buy 0.534 · vol perp/spot 12.82×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1357 · heat=100.0 · PnL sess=317.7295 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
