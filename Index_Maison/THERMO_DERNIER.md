# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-28T19:42Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `65/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81229.23 | prix |
| OI | 95847.469 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.02e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.005 | crowd |
| BTC 1h/4h/24h | 0.32 / 0.88 / 0.67 % | B7 |
| Dominance BTC | 59.48% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat ATTENTION (score 65/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.02e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.005.
- BTC 24h 0.67% · 1h 0.32% · 4h 0.88%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.979 · OI 95847.469 (pas de dark pool free temps réel).
- Top traders L/S 2.12.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.74 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.48%).
- Liquidations 24h proxy ≈ 2.44 M$.
- ETF net inflow : BTC 132.8 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.584 · murC 95000 (+17.0%) · murP 75000 (-7.7%).
- Volumes cachés proxy : taker buy 0.492 · vol perp/spot 13.18×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
