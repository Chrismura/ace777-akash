# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-14T04:27Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `71/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63384.3 | prix |
| OI | 109940.596 | C13 |
| Funding | 8.8e-05 | C14 |
| Funding moy. ~30j | 5.508e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.855 | crowd |
| BTC 1h/4h/24h | 0.15 / -0.21 / -0.31 % | B7 |
| Dominance BTC | 56.22% | A3 |
| Alts ↓ 24h | 50.0% | B9 |

## Lecture
- Climat CALME (score 71/100).
- Funding maintenant 8.8e-05. Moyenne ~30j 5.508e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.855.
- BTC 24h -0.31% · 1h 0.15% · 4h -0.21%.
- Panier alts : 50.0% en baisse (10/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.807 · OI 109940.596 (pas de dark pool free temps réel).
- Top traders L/S 1.919.
- Fear & Greed 29 (Fear).
- Market cap crypto ≈ 2.26 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.22%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC -82.4 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.553 · murC 70000 (+10.5%) · murP 60000 (-5.3%).
- Volumes cachés proxy : taker buy 0.544 · vol perp/spot 11.51×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1125 · heat=100.0 · PnL sess=115.7714 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
