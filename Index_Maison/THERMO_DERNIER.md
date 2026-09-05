# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-05T12:25Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `86/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79643.0 | prix |
| OI | 107228.53 | C13 |
| Funding | 3.1e-05 | C14 |
| Funding moy. ~30j | 6.893e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.038 | crowd |
| BTC 1h/4h/24h | 0.08 / 0.03 / -1.81 % | B7 |
| Dominance BTC | 59.0% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 86/100).
- Funding maintenant 3.1e-05. Moyenne ~30j 6.893e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.038.
- BTC 24h -1.81% · 1h 0.08% · 4h 0.03%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.155 · OI 107228.53 (pas de dark pool free temps réel).
- Top traders L/S 1.114.
- Fear & Greed 73 (Greed).
- Market cap crypto ≈ 2.71 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.0%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -16.74 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.539 · murC 90000 (+12.9%) · murP 70000 (-12.2%).
- Volumes cachés proxy : taker buy 0.474 · vol perp/spot 13.32×.
- ACE soft: LIVE=ACE_RADAR_ALIGNED_V4_60M_LIVE_COLOR.log · SKIP=705 · heat=27.4 · PnL sess=-9.1224 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
