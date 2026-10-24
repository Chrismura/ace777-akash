# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-24T04:21Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `62/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80816.05 | prix |
| OI | 92897.753 | C13 |
| Funding | 7e-05 | C14 |
| Funding moy. ~30j | 3.244e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 2.15 | crowd |
| BTC 1h/4h/24h | -0.16 / 0.28 / -1.14 % | B7 |
| Dominance BTC | 59.47% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat ATTENTION (score 62/100).
- Funding maintenant 7e-05. Moyenne ~30j 3.244e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 2.15.
- BTC 24h -1.14% · 1h -0.16% · 4h 0.28%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 943684$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.021 · OI 92897.753 (pas de dark pool free temps réel).
- Top traders L/S 2.245.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.73 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.47%).
- Liquidations 24h proxy ≈ 2.66 M$.
- ETF net inflow : BTC 64.45 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.576 · murC 95000 (+17.7%) · murP 75000 (-7.1%).
- Volumes cachés proxy : taker buy 0.505 · vol perp/spot 15.67×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
