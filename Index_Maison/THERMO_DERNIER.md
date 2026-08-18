# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-18T20:28Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `89/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64601.18 | prix |
| OI | 106912.672 | C13 |
| Funding | 7e-06 | C14 |
| Funding moy. ~30j | 5.457e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.349 | crowd |
| BTC 1h/4h/24h | -0.05 / -0.34 / 0.4 % | B7 |
| Dominance BTC | 56.62% | A3 |
| Alts ↓ 24h | 70.0% | B9 |

## Lecture
- Climat CALME (score 89/100).
- Funding maintenant 7e-06. Moyenne ~30j 5.457e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.349.
- BTC 24h 0.4% · 1h -0.05% · 4h -0.34%.
- Panier alts : 70.0% en baisse (14/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.914 · OI 106912.672 (pas de dark pool free temps réel).
- Top traders L/S 1.46.
- Fear & Greed 41 (Fear).
- Market cap crypto ≈ 2.29 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.62%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC -86.87 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.563 · murC 70000 (+8.4%) · murP 60000 (-7.1%).
- Volumes cachés proxy : taker buy 0.502 · vol perp/spot 13.02×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1123 · heat=100.0 · PnL sess=269.4552 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
