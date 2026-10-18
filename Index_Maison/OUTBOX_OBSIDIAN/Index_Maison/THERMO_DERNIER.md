# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-18T04:22Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `73/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81878.81 | prix |
| OI | 93198.939 | C13 |
| Funding | 8.6e-05 | C14 |
| Funding moy. ~30j | 3.312e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.729 | crowd |
| BTC 1h/4h/24h | -0.05 / 0.45 / 0.47 % | B7 |
| Dominance BTC | 59.46% | A3 |
| Alts ↓ 24h | 85.0% | B9 |

## Lecture
- Climat CALME (score 73/100).
- Funding maintenant 8.6e-05. Moyenne ~30j 3.312e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.729.
- BTC 24h 0.47% · 1h -0.05% · 4h 0.45%.
- Panier alts : 85.0% en baisse (17/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.484 · OI 93198.939 (pas de dark pool free temps réel).
- Top traders L/S 1.815.
- Fear & Greed 53 (Neutral).
- Market cap crypto ≈ 2.76 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.46%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -46.48 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.584 · murC 95000 (+16.1%) · murP 75000 (-8.3%).
- Volumes cachés proxy : taker buy 0.531 · vol perp/spot 18.39×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
