# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-06T14:26Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `96/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79620.09 | prix |
| OI | 106677.557 | C13 |
| Funding | 3.3e-05 | C14 |
| Funding moy. ~30j | 6.854e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.056 | crowd |
| BTC 1h/4h/24h | -0.21 / -0.43 / -0.03 % | B7 |
| Dominance BTC | 59.25% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat CALME (score 96/100).
- Funding maintenant 3.3e-05. Moyenne ~30j 6.854e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.056.
- BTC 24h -0.03% · 1h -0.21% · 4h -0.43%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.821 · OI 106677.557 (pas de dark pool free temps réel).
- Top traders L/S 1.128.
- Fear & Greed 73 (Greed).
- Market cap crypto ≈ 2.69 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.25%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 526.93 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.54 · murC 90000 (+13.0%) · murP 70000 (-12.1%).
- Volumes cachés proxy : taker buy 0.484 · vol perp/spot 10.64×.
- ACE soft: LIVE=ACE_RADAR_ALIGNED_V4_60M_LIVE_COLOR.log · SKIP=705 · heat=27.4 · PnL sess=-9.1224 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
