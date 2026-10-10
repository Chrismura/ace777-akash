# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-10T07:36Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `86/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82708.54 | prix |
| OI | 92886.946 | C13 |
| Funding | 9e-06 | C14 |
| Funding moy. ~30j | 4.156e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.541 | crowd |
| BTC 1h/4h/24h | 0.0 / 0.17 / 0.17 % | B7 |
| Dominance BTC | 59.07% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 86/100).
- Funding maintenant 9e-06. Moyenne ~30j 4.156e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.541.
- BTC 24h 0.17% · 1h 0.0% · 4h 0.17%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : 4 gros print(s) ≥500k$ (max 1229880$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.849 · OI 92886.946 (pas de dark pool free temps réel).
- Top traders L/S 1.609.
- Fear & Greed 64 (Greed).
- Market cap crypto ≈ 2.80 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.07%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -31.8 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.575 · murC 95000 (+14.9%) · murP 80000 (-3.2%).
- Volumes cachés proxy : taker buy 0.476 · vol perp/spot 13.49×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
