# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-01T21:24Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `76/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77125.7 | prix |
| OI | 108946.954 | C13 |
| Funding | 6.7e-05 | C14 |
| Funding moy. ~30j | 6.762e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.257 | crowd |
| BTC 1h/4h/24h | -0.37 / -0.15 / -2.15 % | B7 |
| Dominance BTC | 59.12% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 76/100).
- Funding maintenant 6.7e-05. Moyenne ~30j 6.762e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.257.
- BTC 24h -2.15% · 1h -0.37% · 4h -0.15%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.14 · OI 108946.954 (pas de dark pool free temps réel).
- Top traders L/S 1.358.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.61 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.12%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 188.31 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.562 · murC 82000 (+6.3%) · murP 70000 (-9.2%).
- Volumes cachés proxy : taker buy 0.521 · vol perp/spot 17.26×.
- ACE soft: LIVE=ACE_RADAR_ALIGNED_V2_15M_LIVE_COLOR.log · SKIP=4 · heat=0.0 · PnL sess=0.0 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
