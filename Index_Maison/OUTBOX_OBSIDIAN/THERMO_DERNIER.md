# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-10T01:33Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `81/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82559.9 | prix |
| OI | 92354.595 | C13 |
| Funding | 3e-05 | C14 |
| Funding moy. ~30j | 4.156e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.48 | crowd |
| BTC 1h/4h/24h | 0.04 / 0.07 / 1.06 % | B7 |
| Dominance BTC | 59.14% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat CALME (score 81/100).
- Funding maintenant 3e-05. Moyenne ~30j 4.156e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.48.
- BTC 24h 1.06% · 1h 0.04% · 4h 0.07%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1100442$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.014 · OI 92354.595 (pas de dark pool free temps réel).
- Top traders L/S 1.546.
- Fear & Greed 64 (Greed).
- Market cap crypto ≈ 2.80 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.14%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -31.74 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.575 · murC 95000 (+15.1%) · murP 80000 (-3.1%).
- Volumes cachés proxy : taker buy 0.476 · vol perp/spot 13.47×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
