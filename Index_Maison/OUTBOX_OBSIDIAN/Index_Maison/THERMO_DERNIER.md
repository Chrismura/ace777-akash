# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-18T21:03Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `76/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80963.77 | prix |
| OI | 93621.404 | C13 |
| Funding | 8e-06 | C14 |
| Funding moy. ~30j | 3.28e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.843 | crowd |
| BTC 1h/4h/24h | 0.03 / -0.23 / -0.81 % | B7 |
| Dominance BTC | 60.25% | A3 |
| Alts ↓ 24h | 100.0% | B9 |

## Lecture
- Climat CALME (score 76/100).
- Funding maintenant 8e-06. Moyenne ~30j 3.28e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.843.
- BTC 24h -0.81% · 1h 0.03% · 4h -0.23%.
- Panier alts : 100.0% en baisse (20/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 848831$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.876 · OI 93621.404 (pas de dark pool free temps réel).
- Top traders L/S 1.934.
- Fear & Greed 53 (Neutral).
- Market cap crypto ≈ 2.70 T$.
- Alt season proxy : Bitcoin season (BTC.D 60.25%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -45.96 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.591 · murC 95000 (+17.4%) · murP 80000 (-1.1%).
- Volumes cachés proxy : taker buy 0.455 · vol perp/spot 15.41×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
