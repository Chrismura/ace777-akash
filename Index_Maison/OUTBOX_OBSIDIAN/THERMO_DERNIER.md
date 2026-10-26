# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-26T14:22Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `63/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80182.7 | prix |
| OI | 95070.86 | C13 |
| Funding | 8.3e-05 | C14 |
| Funding moy. ~30j | 3.493e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 2.296 | crowd |
| BTC 1h/4h/24h | 0.65 / -0.18 / -0.16 % | B7 |
| Dominance BTC | 59.43% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat ATTENTION (score 63/100).
- Funding maintenant 8.3e-05. Moyenne ~30j 3.493e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 2.296.
- BTC 24h -0.16% · 1h 0.65% · 4h -0.18%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 806778$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.137 · OI 95070.86 (pas de dark pool free temps réel).
- Top traders L/S 2.425.
- Fear & Greed 50 (Neutral).
- Market cap crypto ≈ 2.70 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.43%).
- Liquidations 24h proxy ≈ 2.57 M$.
- ETF net inflow : BTC 30.39 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.594 · murC 95000 (+18.7%) · murP 75000 (-6.3%).
- Volumes cachés proxy : taker buy 0.481 · vol perp/spot 15.75×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
