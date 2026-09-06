# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-06T22:28Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `93/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79766.59 | prix |
| OI | 106091.247 | C13 |
| Funding | 5.8e-05 | C14 |
| Funding moy. ~30j | 6.815e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.058 | crowd |
| BTC 1h/4h/24h | -0.18 / -0.19 / 0.02 % | B7 |
| Dominance BTC | 59.19% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat CALME (score 93/100).
- Funding maintenant 5.8e-05. Moyenne ~30j 6.815e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.058.
- BTC 24h 0.02% · 1h -0.18% · 4h -0.19%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 947128$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.987 · OI 106091.247 (pas de dark pool free temps réel).
- Top traders L/S 1.137.
- Fear & Greed 73 (Greed).
- Market cap crypto ≈ 2.70 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.19%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 527.9 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.54 · murC 90000 (+12.8%) · murP 70000 (-12.3%).
- Volumes cachés proxy : taker buy 0.478 · vol perp/spot 11.57×.
- ACE soft: LIVE=ACE_RADAR_ALIGNED_V4_60M_LIVE_COLOR.log · SKIP=705 · heat=27.4 · PnL sess=-9.1224 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
