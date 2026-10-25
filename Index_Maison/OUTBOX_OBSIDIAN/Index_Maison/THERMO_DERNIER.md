# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-25T20:03Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `71/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80507.25 | prix |
| OI | 93303.616 | C13 |
| Funding | 4.8e-05 | C14 |
| Funding moy. ~30j | 3.449e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.125 | crowd |
| BTC 1h/4h/24h | -0.06 / -0.36 / -0.04 % | B7 |
| Dominance BTC | 60.02% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat CALME (score 71/100).
- Funding maintenant 4.8e-05. Moyenne ~30j 3.449e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.125.
- BTC 24h -0.04% · 1h -0.06% · 4h -0.36%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 1310308$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.594 · OI 93303.616 (pas de dark pool free temps réel).
- Top traders L/S 2.263.
- Fear & Greed 54 (Neutral).
- Market cap crypto ≈ 2.69 T$.
- Alt season proxy : Bitcoin season (BTC.D 60.02%).
- Liquidations 24h proxy ≈ 2.70 M$.
- ETF net inflow : BTC -236.39 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.594 · murC 95000 (+18.1%) · murP 75000 (-6.7%).
- Volumes cachés proxy : taker buy 0.481 · vol perp/spot 16.63×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
