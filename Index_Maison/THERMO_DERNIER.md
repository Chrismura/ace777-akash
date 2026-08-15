# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-15T21:17Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `73/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63077.74 | prix |
| OI | 111567.353 | C13 |
| Funding | 2.2e-05 | C14 |
| Funding moy. ~30j | 5.449e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 2.079 | crowd |
| BTC 1h/4h/24h | 0.0 / 0.05 / 0.31 % | B7 |
| Dominance BTC | 56.13% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 73/100).
- Funding maintenant 2.2e-05. Moyenne ~30j 5.449e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 2.079.
- BTC 24h 0.31% · 1h 0.0% · 4h 0.05%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.877 · OI 111567.353 (pas de dark pool free temps réel).
- Top traders L/S 2.143.
- Fear & Greed 34 (Fear).
- Market cap crypto ≈ 2.25 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.13%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -26.5 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.555 · murC 70000 (+11.0%) · murP 60000 (-4.8%).
- Volumes cachés proxy : taker buy 0.483 · vol perp/spot 14.32×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1300 · heat=100.0 · PnL sess=183.0674 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
