# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-05T13:25Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `95/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79711.6 | prix |
| OI | 106933.24 | C13 |
| Funding | 2.1e-05 | C14 |
| Funding moy. ~30j | 6.893e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.05 | crowd |
| BTC 1h/4h/24h | 0.06 / 0.15 / 0.42 % | B7 |
| Dominance BTC | 58.92% | A3 |
| Alts ↓ 24h | 10.0% | B9 |

## Lecture
- Climat CALME (score 95/100).
- Funding maintenant 2.1e-05. Moyenne ~30j 6.893e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.05.
- BTC 24h 0.42% · 1h 0.06% · 4h 0.15%.
- Panier alts : 10.0% en baisse (2/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.088 · OI 106933.24 (pas de dark pool free temps réel).
- Top traders L/S 1.123.
- Fear & Greed 73 (Greed).
- Market cap crypto ≈ 2.71 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.92%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -16.75 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.539 · murC 90000 (+12.8%) · murP 70000 (-12.2%).
- Volumes cachés proxy : taker buy 0.474 · vol perp/spot 12.17×.
- ACE soft: LIVE=ACE_RADAR_ALIGNED_V4_60M_LIVE_COLOR.log · SKIP=705 · heat=27.4 · PnL sess=-9.1224 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
