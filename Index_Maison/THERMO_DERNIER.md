# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-22T10:25Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `81/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 76597.25 | prix |
| OI | 106507.335 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.919e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 0.999 | crowd |
| BTC 1h/4h/24h | -0.58 / -1.13 / -1.8 % | B7 |
| Dominance BTC | None% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat CALME (score 81/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.919e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 0.999.
- BTC 24h -1.8% · 1h -0.58% · 4h -1.13%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.795 · OI 106507.335 (pas de dark pool free temps réel).
- Top traders L/S 1.113.
- Fear & Greed 71 (Greed).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 224.93 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.61 · murC 78000 (+1.8%) · murP 60000 (-21.7%).
- Volumes cachés proxy : taker buy 0.534 · vol perp/spot 10.93×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1381 · heat=100.0 · PnL sess=316.1624 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
