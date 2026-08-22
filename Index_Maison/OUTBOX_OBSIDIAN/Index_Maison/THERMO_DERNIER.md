# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-22T17:12Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `89/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77322.56 | prix |
| OI | 106710.655 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.937e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.003 | crowd |
| BTC 1h/4h/24h | 0.01 / 0.02 / -0.37 % | B7 |
| Dominance BTC | 58.84% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat CALME (score 89/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.937e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.003.
- BTC 24h -0.37% · 1h 0.01% · 4h 0.02%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.257 · OI 106710.655 (pas de dark pool free temps réel).
- Top traders L/S 1.124.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.63 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.84%).
- Liquidations 24h proxy ≈ 0.04 B$.
- ETF net inflow : BTC 227.06 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.614 · murC 78000 (+0.9%) · murP 60000 (-22.4%).
- Volumes cachés proxy : taker buy 0.5 · vol perp/spot 10.73×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1349 · heat=100.0 · PnL sess=319.771 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
