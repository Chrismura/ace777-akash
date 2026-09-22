# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-22T11:05Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `82/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 85937.04 | prix |
| OI | 109604.883 | C13 |
| Funding | 7.7e-05 | C14 |
| Funding moy. ~30j | 6.734e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 0.947 | crowd |
| BTC 1h/4h/24h | 0.09 / 0.72 / 1.73 % | B7 |
| Dominance BTC | 58.9% | A3 |
| Alts ↓ 24h | 50.0% | B9 |

## Lecture
- Climat CALME (score 82/100).
- Funding maintenant 7.7e-05. Moyenne ~30j 6.734e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 0.947.
- BTC 24h 1.73% · 1h 0.09% · 4h 0.72%.
- Panier alts : 50.0% en baisse (10/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 601568$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.688 · OI 109604.883 (pas de dark pool free temps réel).
- Top traders L/S 1.074.
- Fear & Greed 78 (Extreme Greed).
- Market cap crypto ≈ 2.92 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.9%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -22.0 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.529 · murC 95000 (+10.5%) · murP 70000 (-18.6%).
- Volumes cachés proxy : taker buy 0.54 · vol perp/spot 11.62×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
