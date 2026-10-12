# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-12T03:31Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `87/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83635.7 | prix |
| OI | 93244.356 | C13 |
| Funding | -2e-06 | C14 |
| Funding moy. ~30j | 3.76e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.376 | crowd |
| BTC 1h/4h/24h | -0.19 / -0.1 / 0.9 % | B7 |
| Dominance BTC | 59.71% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat CALME (score 87/100).
- Funding maintenant -2e-06. Moyenne ~30j 3.76e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.376.
- BTC 24h 0.9% · 1h -0.19% · 4h -0.1%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.35 · OI 93244.356 (pas de dark pool free temps réel).
- Top traders L/S 1.468.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.81 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.71%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -72.08 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.563 · murC 95000 (+13.7%) · murP 80000 (-4.3%).
- Volumes cachés proxy : taker buy 0.476 · vol perp/spot 15.89×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
