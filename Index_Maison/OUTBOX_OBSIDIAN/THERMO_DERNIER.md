# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-22T09:25Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `87/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77209.9 | prix |
| OI | 105997.119 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.919e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.006 | crowd |
| BTC 1h/4h/24h | 0.04 / -0.19 / -0.56 % | B7 |
| Dominance BTC | 58.74% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat CALME (score 87/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.919e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.006.
- BTC 24h -0.56% · 1h 0.04% · 4h -0.19%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.82 · OI 105997.119 (pas de dark pool free temps réel).
- Top traders L/S 1.114.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.63 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.74%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 226.73 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.609 · murC 78000 (+1.0%) · murP 60000 (-22.3%).
- Volumes cachés proxy : taker buy 0.534 · vol perp/spot 10.9×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1400 · heat=100.0 · PnL sess=312.7484 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
