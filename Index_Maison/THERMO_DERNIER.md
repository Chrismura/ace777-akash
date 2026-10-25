# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-25T07:59Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `71/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80635.4 | prix |
| OI | 93225.913 | C13 |
| Funding | 6e-05 | C14 |
| Funding moy. ~30j | 3.326e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 2.065 | crowd |
| BTC 1h/4h/24h | 0.22 / -0.23 / -0.04 % | B7 |
| Dominance BTC | 60.09% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat CALME (score 71/100).
- Funding maintenant 6e-05. Moyenne ~30j 3.326e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 2.065.
- BTC 24h -0.04% · 1h 0.22% · 4h -0.23%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 567534$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.795 · OI 93225.913 (pas de dark pool free temps réel).
- Top traders L/S 2.206.
- Fear & Greed 54 (Neutral).
- Market cap crypto ≈ 2.69 T$.
- Alt season proxy : Bitcoin season (BTC.D 60.09%).
- Liquidations 24h proxy ≈ 1.93 M$.
- ETF net inflow : BTC 64.3 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.594 · murC 95000 (+17.9%) · murP 75000 (-6.9%).
- Volumes cachés proxy : taker buy 0.536 · vol perp/spot 15.39×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
