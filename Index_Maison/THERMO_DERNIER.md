# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-29T17:19Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `73/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81041.4 | prix |
| OI | 94305.693 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.125e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.648 | crowd |
| BTC 1h/4h/24h | -0.23 / 0.96 / 0.69 % | B7 |
| Dominance BTC | 59.43% | A3 |
| Alts ↓ 24h | 65.0% | B9 |

## Lecture
- Climat CALME (score 73/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.125e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.648.
- BTC 24h 0.69% · 1h -0.23% · 4h 0.96%.
- Panier alts : 65.0% en baisse (13/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.839 · OI 94305.693 (pas de dark pool free temps réel).
- Top traders L/S 1.784.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.73 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.43%).
- Liquidations 24h proxy ≈ 2.78 M$.
- ETF net inflow : BTC 149.01 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.595 · murC 95000 (+17.3%) · murP 75000 (-7.4%).
- Volumes cachés proxy : taker buy 0.526 · vol perp/spot 16.69×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
