# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-18T02:35Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `79/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64113.57 | prix |
| OI | 106593.086 | C13 |
| Funding | 4.4e-05 | C14 |
| Funding moy. ~30j | 5.495e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.458 | crowd |
| BTC 1h/4h/24h | -0.1 / -0.25 / 1.33 % | B7 |
| Dominance BTC | 56.53% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 79/100).
- Funding maintenant 4.4e-05. Moyenne ~30j 5.495e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.458.
- BTC 24h 1.33% · 1h -0.1% · 4h -0.25%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.605 · OI 106593.086 (pas de dark pool free temps réel).
- Top traders L/S 1.515.
- Fear & Greed 41 (Fear).
- Market cap crypto ≈ 2.28 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.53%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC -25.66 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.562 · murC 70000 (+9.2%) · murP 60000 (-6.4%).
- Volumes cachés proxy : taker buy 0.555 · vol perp/spot 16.24×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=555 · heat=100.0 · PnL sess=180.9328 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
