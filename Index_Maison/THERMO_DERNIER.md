# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-07T19:36Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `91/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79337.3 | prix |
| OI | 107452.792 | C13 |
| Funding | 2.7e-05 | C14 |
| Funding moy. ~30j | 6.719e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.166 | crowd |
| BTC 1h/4h/24h | 0.22 / 0.69 / -0.56 % | B7 |
| Dominance BTC | 59.12% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 91/100).
- Funding maintenant 2.7e-05. Moyenne ~30j 6.719e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.166.
- BTC 24h -0.56% · 1h 0.22% · 4h 0.69%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.667 · OI 107452.792 (pas de dark pool free temps réel).
- Top traders L/S 1.275.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.68 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.12%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 123.18 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.525 · murC 90000 (+13.4%) · murP 70000 (-11.8%).
- Volumes cachés proxy : taker buy 0.473 · vol perp/spot 12.41×.
- ACE soft: LIVE=ACE_RADAR_ALIGNED_V4_60M_LIVE_COLOR.log · SKIP=705 · heat=27.4 · PnL sess=-9.1224 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
