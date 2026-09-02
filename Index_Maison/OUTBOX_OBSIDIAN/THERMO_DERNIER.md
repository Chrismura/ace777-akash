# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-02T11:38Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `77/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 76602.95 | prix |
| OI | 108414.408 | C13 |
| Funding | 5.8e-05 | C14 |
| Funding moy. ~30j | 6.758e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.305 | crowd |
| BTC 1h/4h/24h | -0.05 / -1.09 / -1.93 % | B7 |
| Dominance BTC | 59.02% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 77/100).
- Funding maintenant 5.8e-05. Moyenne ~30j 6.758e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.305.
- BTC 24h -1.93% · 1h -0.05% · 4h -1.09%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 2170921$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.744 · OI 108414.408 (pas de dark pool free temps réel).
- Top traders L/S 1.379.
- Fear & Greed 63 (Greed).
- Market cap crypto ≈ 2.61 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.02%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 58.91 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.553 · murC 82000 (+7.0%) · murP 70000 (-8.6%).
- Volumes cachés proxy : taker buy 0.521 · vol perp/spot 15.99×.
- ACE soft: LIVE=ACE_RADAR_ALIGNED_V4_60M_LIVE_COLOR.log · SKIP=705 · heat=27.4 · PnL sess=-9.1224 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
