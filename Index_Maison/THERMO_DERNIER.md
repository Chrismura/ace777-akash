# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-22T13:07Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `89/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 86177.1 | prix |
| OI | 109569.5 | C13 |
| Funding | 4.9e-05 | C14 |
| Funding moy. ~30j | 6.734e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 0.943 | crowd |
| BTC 1h/4h/24h | 0.22 / -0.03 / 0.93 % | B7 |
| Dominance BTC | 58.8% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 89/100).
- Funding maintenant 4.9e-05. Moyenne ~30j 6.734e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 0.943.
- BTC 24h 0.93% · 1h 0.22% · 4h -0.03%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1016438$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.172 · OI 109569.5 (pas de dark pool free temps réel).
- Top traders L/S 1.069.
- Fear & Greed 78 (Extreme Greed).
- Market cap crypto ≈ 2.93 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.8%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -22.06 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.538 · murC 95000 (+10.2%) · murP 70000 (-18.8%).
- Volumes cachés proxy : taker buy 0.54 · vol perp/spot 11.54×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
