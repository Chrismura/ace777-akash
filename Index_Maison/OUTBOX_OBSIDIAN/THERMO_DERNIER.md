# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-07T16:34Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `89/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78864.9 | prix |
| OI | 107937.062 | C13 |
| Funding | 2e-05 | C14 |
| Funding moy. ~30j | 6.719e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.158 | crowd |
| BTC 1h/4h/24h | 0.1 / -0.88 / -1.08 % | B7 |
| Dominance BTC | 59.1% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 89/100).
- Funding maintenant 2e-05. Moyenne ~30j 6.719e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.158.
- BTC 24h -1.08% · 1h 0.1% · 4h -0.88%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : 5 gros print(s) ≥500k$ (max 816195$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.814 · OI 107937.062 (pas de dark pool free temps réel).
- Top traders L/S 1.272.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.67 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.1%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 122.45 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.524 · murC 90000 (+14.1%) · murP 70000 (-11.3%).
- Volumes cachés proxy : taker buy 0.473 · vol perp/spot 12.29×.
- ACE soft: LIVE=ACE_RADAR_ALIGNED_V4_60M_LIVE_COLOR.log · SKIP=705 · heat=27.4 · PnL sess=-9.1224 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
