# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-22T04:59Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `64/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78484.09 | prix |
| OI | 105839.6 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.811e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.055 | crowd |
| BTC 1h/4h/24h | 0.1 / 0.71 / 4.7 % | B7 |
| Dominance BTC | None% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat ATTENTION (score 64/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.811e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.055.
- BTC 24h 4.7% · 1h 0.1% · 4h 0.71%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.979 · OI 105839.6 (pas de dark pool free temps réel).
- Top traders L/S 1.138.
- Fear & Greed 71 (Greed).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 230.47 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.615 · murC 80000 (+1.9%) · murP 60000 (-23.5%).
- Volumes cachés proxy : taker buy 0.534 · vol perp/spot 12.69×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1355 · heat=100.0 · PnL sess=317.603 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
