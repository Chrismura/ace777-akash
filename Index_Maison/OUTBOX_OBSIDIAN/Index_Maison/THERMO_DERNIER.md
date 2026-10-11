# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-11T18:24Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `84/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83845.21 | prix |
| OI | 92845.362 | C13 |
| Funding | 1.9e-05 | C14 |
| Funding moy. ~30j | 3.821e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.409 | crowd |
| BTC 1h/4h/24h | 0.07 / 0.9 / 1.03 % | B7 |
| Dominance BTC | 59.61% | A3 |
| Alts ↓ 24h | 10.0% | B9 |

## Lecture
- Climat CALME (score 84/100).
- Funding maintenant 1.9e-05. Moyenne ~30j 3.821e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.409.
- BTC 24h 1.03% · 1h 0.07% · 4h 0.9%.
- Panier alts : 10.0% en baisse (2/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.005 · OI 92845.362 (pas de dark pool free temps réel).
- Top traders L/S 1.468.
- Fear & Greed 61 (Greed).
- Market cap crypto ≈ 2.82 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.61%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -32.24 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.564 · murC 95000 (+13.4%) · murP 80000 (-4.5%).
- Volumes cachés proxy : taker buy 0.476 · vol perp/spot 15.39×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
