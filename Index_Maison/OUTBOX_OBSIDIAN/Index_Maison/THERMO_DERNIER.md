# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-22T01:48Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `67/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77898.28 | prix |
| OI | 105838.678 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.811e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.039 | crowd |
| BTC 1h/4h/24h | -0.05 / -0.78 / 4.12 % | B7 |
| Dominance BTC | None% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat ATTENTION (score 67/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.811e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.039.
- BTC 24h 4.12% · 1h -0.05% · 4h -0.78%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.838 · OI 105838.678 (pas de dark pool free temps réel).
- Top traders L/S 1.085.
- Fear & Greed 71 (Greed).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 228.75 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.616 · murC 78000 (+0.1%) · murP 60000 (-23.0%).
- Volumes cachés proxy : taker buy 0.534 · vol perp/spot 13.1×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1368 · heat=100.0 · PnL sess=307.3701 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
