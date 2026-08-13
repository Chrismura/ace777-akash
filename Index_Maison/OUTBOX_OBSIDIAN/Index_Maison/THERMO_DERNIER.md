# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-13T21:17Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `70/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63402.6 | prix |
| OI | 109918.408 | C13 |
| Funding | 9.7e-05 | C14 |
| Funding moy. ~30j | 5.524e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.881 | crowd |
| BTC 1h/4h/24h | 0.03 / 0.45 / -0.24 % | B7 |
| Dominance BTC | 56.24% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat CALME (score 70/100).
- Funding maintenant 9.7e-05. Moyenne ~30j 5.524e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.881.
- BTC 24h -0.24% · 1h 0.03% · 4h 0.45%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.749 · OI 109918.408 (pas de dark pool free temps réel).
- Top traders L/S 1.935.
- Fear & Greed 29 (Fear).
- Market cap crypto ≈ 2.26 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.24%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC 14.66 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.554 · murC 70000 (+10.5%) · murP 60000 (-5.3%).
- Volumes cachés proxy : taker buy 0.544 · vol perp/spot 13.31×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1125 · heat=100.0 · PnL sess=115.7714 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
