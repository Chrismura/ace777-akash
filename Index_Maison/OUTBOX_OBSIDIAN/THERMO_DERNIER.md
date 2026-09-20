# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-19T23:54Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `87/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81263.1 | prix |
| OI | 107408.858 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 6.8e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 0.938 | crowd |
| BTC 1h/4h/24h | 0.04 / -0.08 / 0.47 % | B7 |
| Dominance BTC | 58.85% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat CALME (score 87/100).
- Funding maintenant 0.0001. Moyenne ~30j 6.8e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 0.938.
- BTC 24h 0.47% · 1h 0.04% · 4h -0.08%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 558994$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.925 · OI 107408.858 (pas de dark pool free temps réel).
- Top traders L/S 1.092.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.77 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.85%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -119.29 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.563 · murC 85000 (+4.6%) · murP 70000 (-13.9%).
- Volumes cachés proxy : taker buy 0.532 · vol perp/spot 10.23×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
