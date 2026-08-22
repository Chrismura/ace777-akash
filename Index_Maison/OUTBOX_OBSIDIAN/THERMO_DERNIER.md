# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-22T03:33Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `60/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78662.5 | prix |
| OI | 106114.75 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.811e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.052 | crowd |
| BTC 1h/4h/24h | 0.26 / 0.46 / 5.45 % | B7 |
| Dominance BTC | None% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat ATTENTION (score 60/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.811e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.052.
- BTC 24h 5.45% · 1h 0.26% · 4h 0.46%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.279 · OI 106114.75 (pas de dark pool free temps réel).
- Top traders L/S 1.136.
- Fear & Greed 71 (Greed).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 231.0 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.615 · murC 80000 (+1.7%) · murP 60000 (-23.7%).
- Volumes cachés proxy : taker buy 0.534 · vol perp/spot 12.81×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1358 · heat=100.0 · PnL sess=317.7295 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
