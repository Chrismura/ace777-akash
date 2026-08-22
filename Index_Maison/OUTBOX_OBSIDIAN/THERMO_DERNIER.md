# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-22T09:49Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `82/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 76918.4 | prix |
| OI | 106060.894 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.919e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.006 | crowd |
| BTC 1h/4h/24h | -0.3 / -0.53 / -1.57 % | B7 |
| Dominance BTC | None% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat CALME (score 82/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.919e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.006.
- BTC 24h -1.57% · 1h -0.3% · 4h -0.53%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 788002$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.82 · OI 106060.894 (pas de dark pool free temps réel).
- Top traders L/S 1.114.
- Fear & Greed 71 (Greed).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 225.88 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.609 · murC 78000 (+1.3%) · murP 60000 (-22.0%).
- Volumes cachés proxy : taker buy 0.534 · vol perp/spot 10.91×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1382 · heat=100.0 · PnL sess=312.6548 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
