# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-10T07:47Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `86/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82736.01 | prix |
| OI | 92886.687 | C13 |
| Funding | 1e-06 | C14 |
| Funding moy. ~30j | 4.156e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.541 | crowd |
| BTC 1h/4h/24h | 0.04 / 0.21 / 0.29 % | B7 |
| Dominance BTC | 59.11% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat CALME (score 86/100).
- Funding maintenant 1e-06. Moyenne ~30j 4.156e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.541.
- BTC 24h 0.29% · 1h 0.04% · 4h 0.21%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 534725$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.849 · OI 92886.687 (pas de dark pool free temps réel).
- Top traders L/S 1.609.
- Fear & Greed 64 (Greed).
- Market cap crypto ≈ 2.80 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.11%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -31.81 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.575 · murC 95000 (+14.8%) · murP 80000 (-3.3%).
- Volumes cachés proxy : taker buy 0.476 · vol perp/spot 13.54×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
