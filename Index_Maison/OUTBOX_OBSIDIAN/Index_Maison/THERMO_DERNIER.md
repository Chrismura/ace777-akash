# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-21T23:18Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `60/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78668.2 | prix |
| OI | 106397.46 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.696e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.053 | crowd |
| BTC 1h/4h/24h | 0.26 / 2.13 / 7.79 % | B7 |
| Dominance BTC | 59.01% | A3 |
| Alts ↓ 24h | 15.0% | B9 |

## Lecture
- Climat ATTENTION (score 60/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.696e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.053.
- BTC 24h 7.79% · 1h 0.26% · 4h 2.13%.
- Panier alts : 15.0% en baisse (3/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 576094$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.948 · OI 106397.46 (pas de dark pool free temps réel).
- Top traders L/S 1.098.
- Fear & Greed 72 (Greed).
- Market cap crypto ≈ 2.67 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.01%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 1010.15 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.616 · murC 80000 (+1.8%) · murP 60000 (-23.7%).
- Volumes cachés proxy : taker buy 0.534 · vol perp/spot 13.32×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1408 · heat=100.0 · PnL sess=306.9477 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
