# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-11-01T06:59Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `56/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77986.79 | prix |
| OI | 97448.552 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.366e-05 (n=90) | Cortana |
| Funding mois préc. | 4.378e-05 (n=93) | Cortana |
| L/S 1h | 2.54 | crowd |
| BTC 1h/4h/24h | 0.14 / 0.38 / 0.82 % | B7 |
| Dominance BTC | 59.31% | A3 |
| Alts ↓ 24h | 50.0% | B9 |

## Lecture
- Climat ATTENTION (score 56/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.366e-05 (90 pts). Mois précédent 4.378e-05 (93 pts).
- Long/Short 2.54.
- BTC 24h 0.82% · 1h 0.14% · 4h 0.38%.
- Panier alts : 50.0% en baisse (10/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.703 · OI 97448.552 (pas de dark pool free temps réel).
- Top traders L/S 2.682.
- Fear & Greed 34 (Fear).
- Market cap crypto ≈ 2.64 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.31%).
- Liquidations 24h proxy ≈ 1.53 M$.
- ETF net inflow : BTC 58.85 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.675 · murC 90000 (+15.5%) · murP 74000 (-5.0%).
- Volumes cachés proxy : taker buy 0.537 · vol perp/spot 7.88×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
