# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-21T22:25Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `59/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78614.9 | prix |
| OI | 106766.039 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.696e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.059 | crowd |
| BTC 1h/4h/24h | 0.17 / 1.96 / 8.04 % | B7 |
| Dominance BTC | None% | A3 |
| Alts ↓ 24h | 15.0% | B9 |

## Lecture
- Climat ATTENTION (score 59/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.696e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.059.
- BTC 24h 8.04% · 1h 0.17% · 4h 1.96%.
- Panier alts : 15.0% en baisse (3/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 4641487$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.482 · OI 106766.039 (pas de dark pool free temps réel).
- Top traders L/S 1.098.
- Fear & Greed 72 (Greed).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 1009.46 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.616 · murC 80000 (+1.8%) · murP 60000 (-23.7%).
- Volumes cachés proxy : taker buy 0.534 · vol perp/spot 13.36×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1383 · heat=100.0 · PnL sess=306.7634 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
