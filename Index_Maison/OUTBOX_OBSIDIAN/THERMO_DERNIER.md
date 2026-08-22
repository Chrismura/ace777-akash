# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-22T16:02Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `90/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77034.2 | prix |
| OI | 106474.627 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.937e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 0.992 | crowd |
| BTC 1h/4h/24h | 0.05 / -0.34 / -0.17 % | B7 |
| Dominance BTC | None% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat CALME (score 90/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.937e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 0.992.
- BTC 24h -0.17% · 1h 0.05% · 4h -0.34%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.019 · OI 106474.627 (pas de dark pool free temps réel).
- Top traders L/S 1.116.
- Fear & Greed 71 (Greed).
- Liquidations 24h proxy ≈ 0.04 B$.
- ETF net inflow : BTC 226.22 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.614 · murC 78000 (+1.3%) · murP 60000 (-22.1%).
- Volumes cachés proxy : taker buy 0.534 · vol perp/spot 10.75×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1344 · heat=100.0 · PnL sess=316.5848 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
