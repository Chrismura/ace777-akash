# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-13T18:09Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `72/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63215.82 | prix |
| OI | 110571.447 | C13 |
| Funding | 7.1e-05 | C14 |
| Funding moy. ~30j | 5.524e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.884 | crowd |
| BTC 1h/4h/24h | 0.15 / -0.97 / -0.36 % | B7 |
| Dominance BTC | 56.18% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 72/100).
- Funding maintenant 7.1e-05. Moyenne ~30j 5.524e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.884.
- BTC 24h -0.36% · 1h 0.15% · 4h -0.97%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.051 · OI 110571.447 (pas de dark pool free temps réel).
- Top traders L/S 1.941.
- Fear & Greed 29 (Fear).
- Market cap crypto ≈ 2.26 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.18%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC 14.62 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.55 · murC 70000 (+10.8%) · murP 60000 (-5.0%).
- Volumes cachés proxy : taker buy 0.544 · vol perp/spot 13.45×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1041 · heat=100.0 · PnL sess=114.1468 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
