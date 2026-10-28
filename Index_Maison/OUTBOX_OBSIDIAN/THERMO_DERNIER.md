# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-28T05:30Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `66/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80906.7 | prix |
| OI | 96082.562 | C13 |
| Funding | 5.6e-05 | C14 |
| Funding moy. ~30j | 3.887e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.965 | crowd |
| BTC 1h/4h/24h | -0.06 / 0.01 / 1.44 % | B7 |
| Dominance BTC | 59.41% | A3 |
| Alts ↓ 24h | 10.0% | B9 |

## Lecture
- Climat ATTENTION (score 66/100).
- Funding maintenant 5.6e-05. Moyenne ~30j 3.887e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.965.
- BTC 24h 1.44% · 1h -0.06% · 4h 0.01%.
- Panier alts : 10.0% en baisse (2/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 642959$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.759 · OI 96082.562 (pas de dark pool free temps réel).
- Top traders L/S 2.084.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.73 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.41%).
- Liquidations 24h proxy ≈ 1.50 M$.
- ETF net inflow : BTC -22.6 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.593 · murC 95000 (+17.5%) · murP 75000 (-7.2%).
- Volumes cachés proxy : taker buy 0.513 · vol perp/spot 15.16×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
