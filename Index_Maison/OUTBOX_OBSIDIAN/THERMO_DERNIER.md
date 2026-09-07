# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-07T08:43Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `94/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79447.4 | prix |
| OI | 106693.179 | C13 |
| Funding | 2.8e-05 | C14 |
| Funding moy. ~30j | 6.759e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.073 | crowd |
| BTC 1h/4h/24h | 0.11 / -0.3 / -0.37 % | B7 |
| Dominance BTC | 59.14% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 94/100).
- Funding maintenant 2.8e-05. Moyenne ~30j 6.759e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.073.
- BTC 24h -0.37% · 1h 0.11% · 4h -0.3%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.761 · OI 106693.179 (pas de dark pool free temps réel).
- Top traders L/S 1.179.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.69 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.14%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 97.25 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.538 · murC 90000 (+13.3%) · murP 70000 (-11.9%).
- Volumes cachés proxy : taker buy 0.478 · vol perp/spot 12.44×.
- ACE soft: LIVE=ACE_RADAR_ALIGNED_V4_60M_LIVE_COLOR.log · SKIP=705 · heat=27.4 · PnL sess=-9.1224 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
