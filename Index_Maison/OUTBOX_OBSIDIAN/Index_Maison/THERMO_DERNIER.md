# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-29T20:48Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `63/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78740.92 | prix |
| OI | 92581.193 | C13 |
| Funding | 3.9e-05 | C14 |
| Funding moy. ~30j | 4.125e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.805 | crowd |
| BTC 1h/4h/24h | -2.48 / -2.99 / -2.8 % | B7 |
| Dominance BTC | 59.57% | A3 |
| Alts ↓ 24h | 85.0% | B9 |

## Lecture
- Climat ATTENTION (score 63/100).
- Funding maintenant 3.9e-05. Moyenne ~30j 4.125e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.805.
- BTC 24h -2.8% · 1h -2.48% · 4h -2.99%.
- Panier alts : 85.0% en baisse (17/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 592789$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.071 · OI 92581.193 (pas de dark pool free temps réel).
- Top traders L/S 1.947.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.68 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.57%).
- Liquidations 24h proxy ≈ 3.05 M$.
- ETF net inflow : BTC 144.78 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.603 · murC 95000 (+20.5%) · murP 75000 (-4.8%).
- Volumes cachés proxy : taker buy 0.526 · vol perp/spot 16.07×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
