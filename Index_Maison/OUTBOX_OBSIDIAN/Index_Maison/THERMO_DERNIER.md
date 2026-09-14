# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-14T15:39Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `79/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78445.2 | prix |
| OI | 105498.273 | C13 |
| Funding | 4.4e-05 | C14 |
| Funding moy. ~30j | 6.639e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.324 | crowd |
| BTC 1h/4h/24h | -0.05 / 0.89 / 1.83 % | B7 |
| Dominance BTC | 58.61% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 79/100).
- Funding maintenant 4.4e-05. Moyenne ~30j 6.639e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.324.
- BTC 24h 1.83% · 1h -0.05% · 4h 0.89%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 2218371$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.965 · OI 105498.273 (pas de dark pool free temps réel).
- Top traders L/S 1.361.
- Fear & Greed 57 (Greed).
- Market cap crypto ≈ 2.68 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.61%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -364.25 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.548 · murC 85000 (+8.4%) · murP 70000 (-10.8%).
- Volumes cachés proxy : taker buy 0.513 · vol perp/spot 13.43×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
