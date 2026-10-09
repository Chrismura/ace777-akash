# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-09T16:31Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `76/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82694.03 | prix |
| OI | 91760.873 | C13 |
| Funding | 2.3e-05 | C14 |
| Funding moy. ~30j | 4.137e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.526 | crowd |
| BTC 1h/4h/24h | -0.19 / -0.36 / 1.81 % | B7 |
| Dominance BTC | 59.23% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat CALME (score 76/100).
- Funding maintenant 2.3e-05. Moyenne ~30j 4.137e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.526.
- BTC 24h 1.81% · 1h -0.19% · 4h -0.36%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 799972$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.911 · OI 91760.873 (pas de dark pool free temps réel).
- Top traders L/S 1.588.
- Fear & Greed 59 (Greed).
- Market cap crypto ≈ 2.80 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.23%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -111.42 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.57 · murC 95000 (+14.9%) · murP 80000 (-3.2%).
- Volumes cachés proxy : taker buy 0.476 · vol perp/spot 11.11×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
