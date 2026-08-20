# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-20T22:45Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `70/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 72665.2 | prix |
| OI | 107046.921 | C13 |
| Funding | 2.9e-05 | C14 |
| Funding moy. ~30j | 5.586e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 0.954 | crowd |
| BTC 1h/4h/24h | -0.06 / 0.37 / 4.83 % | B7 |
| Dominance BTC | 58.68% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat CALME (score 70/100).
- Funding maintenant 2.9e-05. Moyenne ~30j 5.586e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 0.954.
- BTC 24h 4.83% · 1h -0.06% · 4h 0.37%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.282 · OI 107046.921 (pas de dark pool free temps réel).
- Top traders L/S 1.048.
- Fear & Greed 62 (Greed).
- Market cap crypto ≈ 2.48 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.68%).
- Liquidations 24h proxy ≈ 0.03 B$.
- ETF net inflow : BTC 651.11 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.571 · murC 75000 (+3.2%) · murP 60000 (-17.4%).
- Volumes cachés proxy : taker buy 0.516 · vol perp/spot 11.22×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=743 · heat=100.0 · PnL sess=240.4108 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
