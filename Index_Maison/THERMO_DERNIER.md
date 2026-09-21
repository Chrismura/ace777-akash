# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-21T23:07Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `61/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 86563.03 | prix |
| OI | 108983.519 | C13 |
| Funding | 7.2e-05 | C14 |
| Funding moy. ~30j | 6.76e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 0.89 | crowd |
| BTC 1h/4h/24h | 0.14 / 0.1 / 6.73 % | B7 |
| Dominance BTC | 58.82% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat ATTENTION (score 61/100).
- Funding maintenant 7.2e-05. Moyenne ~30j 6.76e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 0.89.
- BTC 24h 6.73% · 1h 0.14% · 4h 0.1%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.752 · OI 108983.519 (pas de dark pool free temps réel).
- Top traders L/S 0.961.
- Fear & Greed 70 (Greed).
- Market cap crypto ≈ 2.94 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.82%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 453.05 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.511 · murC 95000 (+9.8%) · murP 70000 (-19.1%).
- Volumes cachés proxy : taker buy 0.54 · vol perp/spot 11.89×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
