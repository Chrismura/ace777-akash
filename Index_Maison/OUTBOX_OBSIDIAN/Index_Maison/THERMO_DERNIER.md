# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-21T20:02Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `60/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 76960.0 | prix |
| OI | 106318.216 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.696e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.026 | crowd |
| BTC 1h/4h/24h | -0.05 / -0.65 / 5.88 % | B7 |
| Dominance BTC | 59.27% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat ATTENTION (score 60/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.696e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.026.
- BTC 24h 5.88% · 1h -0.05% · 4h -0.65%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.73 · OI 106318.216 (pas de dark pool free temps réel).
- Top traders L/S 1.096.
- Fear & Greed 72 (Greed).
- Market cap crypto ≈ 2.61 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.27%).
- Liquidations 24h proxy ≈ 0.04 B$.
- ETF net inflow : BTC 988.21 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.611 · murC 78000 (+1.3%) · murP 60000 (-22.1%).
- Volumes cachés proxy : taker buy 0.534 · vol perp/spot 13.17×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=647 · heat=100.0 · PnL sess=282.1468 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
