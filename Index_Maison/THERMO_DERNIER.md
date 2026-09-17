# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-17T09:02Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `79/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 76640.83 | prix |
| OI | 107746.888 | C13 |
| Funding | 3.9e-05 | C14 |
| Funding moy. ~30j | 6.694e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.483 | crowd |
| BTC 1h/4h/24h | 0.13 / 0.45 / 1.18 % | B7 |
| Dominance BTC | 58.32% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 79/100).
- Funding maintenant 3.9e-05. Moyenne ~30j 6.694e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.483.
- BTC 24h 1.18% · 1h 0.13% · 4h 0.45%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 1552129$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.834 · OI 107746.888 (pas de dark pool free temps réel).
- Top traders L/S 1.552.
- Fear & Greed 50 (Neutral).
- Market cap crypto ≈ 2.63 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.32%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -173.56 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.554 · murC 90000 (+17.5%) · murP 70000 (-8.6%).
- Volumes cachés proxy : taker buy 0.478 · vol perp/spot 12.53×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
