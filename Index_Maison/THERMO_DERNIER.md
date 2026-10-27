# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-27T23:24Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `65/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80780.5 | prix |
| OI | 94958.055 | C13 |
| Funding | 6.6e-05 | C14 |
| Funding moy. ~30j | 3.849e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.059 | crowd |
| BTC 1h/4h/24h | -0.12 / 0.01 / 1.09 % | B7 |
| Dominance BTC | 59.46% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat ATTENTION (score 65/100).
- Funding maintenant 6.6e-05. Moyenne ~30j 3.849e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.059.
- BTC 24h 1.09% · 1h -0.12% · 4h 0.01%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : 4 gros print(s) ≥500k$ (max 1416009$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.803 · OI 94958.055 (pas de dark pool free temps réel).
- Top traders L/S 2.145.
- Fear & Greed 48 (Neutral).
- Market cap crypto ≈ 2.72 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.46%).
- Liquidations 24h proxy ≈ 2.32 M$.
- ETF net inflow : BTC 71.1 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.59 · murC 95000 (+17.7%) · murP 75000 (-7.1%).
- Volumes cachés proxy : taker buy 0.513 · vol perp/spot 16.96×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
