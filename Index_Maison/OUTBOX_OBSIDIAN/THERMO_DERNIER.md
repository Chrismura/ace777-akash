# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-11-01T21:59Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `61/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77855.63 | prix |
| OI | 95935.602 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.463e-05 (n=90) | Cortana |
| Funding mois préc. | 4.469e-05 (n=93) | Cortana |
| L/S 1h | 2.266 | crowd |
| BTC 1h/4h/24h | -0.02 / -0.12 / 0.29 % | B7 |
| Dominance BTC | 59.99% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat ATTENTION (score 61/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.463e-05 (90 pts). Mois précédent 4.469e-05 (93 pts).
- Long/Short 2.266.
- BTC 24h 0.29% · 1h -0.02% · 4h -0.12%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.327 · OI 95935.602 (pas de dark pool free temps réel).
- Top traders L/S 2.377.
- Fear & Greed 34 (Fear).
- Market cap crypto ≈ 2.61 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.99%).
- Liquidations 24h proxy ≈ 1.57 M$.
- ETF net inflow : BTC 58.75 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.663 · murC 90000 (+15.7%) · murP 60000 (-22.9%).
- Volumes cachés proxy : taker buy 0.528 · vol perp/spot 7.18×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
