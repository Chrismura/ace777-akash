# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-06T09:24Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `96/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79933.3 | prix |
| OI | 106500.098 | C13 |
| Funding | 1.3e-05 | C14 |
| Funding moy. ~30j | 6.854e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.06 | crowd |
| BTC 1h/4h/24h | 0.16 / -0.03 / 0.33 % | B7 |
| Dominance BTC | 59.22% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat CALME (score 96/100).
- Funding maintenant 1.3e-05. Moyenne ~30j 6.854e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.06.
- BTC 24h 0.33% · 1h 0.16% · 4h -0.03%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 1444132$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.085 · OI 106500.098 (pas de dark pool free temps réel).
- Top traders L/S 1.131.
- Fear & Greed 73 (Greed).
- Market cap crypto ≈ 2.70 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.22%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC 26.02 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.539 · murC 90000 (+12.5%) · murP 70000 (-12.5%).
- Volumes cachés proxy : taker buy 0.484 · vol perp/spot 10.75×.
- ACE soft: LIVE=ACE_RADAR_ALIGNED_V4_60M_LIVE_COLOR.log · SKIP=705 · heat=27.4 · PnL sess=-9.1224 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
