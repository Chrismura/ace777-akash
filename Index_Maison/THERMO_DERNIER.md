# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-05T19:27Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `94/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79937.6 | prix |
| OI | 106556.937 | C13 |
| Funding | 3.2e-05 | C14 |
| Funding moy. ~30j | 6.849e-05 (n=90) | Cortana |
| Funding mois préc. | None (n=0) | Cortana |
| L/S 1h | 1.062 | crowd |
| BTC 1h/4h/24h | -0.02 / 0.22 / 0.22 % | B7 |
| Dominance BTC | 58.85% | A3 |
| Alts ↓ 24h | 5.0% | B9 |

## Lecture
- Climat CALME (score 94/100).
- Funding maintenant 3.2e-05. Moyenne ~30j 6.849e-05 (90 pts). Mois précédent None (0 pts).
- Long/Short 1.062.
- BTC 24h 0.22% · 1h -0.02% · 4h 0.22%.
- Panier alts : 5.0% en baisse (1/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 686798$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.92 · OI 106556.937 (pas de dark pool free temps réel).
- Top traders L/S 1.125.
- Fear & Greed 73 (Greed).
- Market cap crypto ≈ 2.72 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.85%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -16.8 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.539 · murC 90000 (+12.5%) · murP 70000 (-12.5%).
- Volumes cachés proxy : taker buy 0.484 · vol perp/spot 10.23×.
- ACE soft: LIVE=ACE_RADAR_ALIGNED_V4_60M_LIVE_COLOR.log · SKIP=705 · heat=27.4 · PnL sess=-9.1224 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
