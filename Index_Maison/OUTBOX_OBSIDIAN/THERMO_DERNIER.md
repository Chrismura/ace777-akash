# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-14T08:37Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `76/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77714.26 | prix |
| OI | 106448.457 | C13 |
| Funding | 6.2e-05 | C14 |
| Funding moy. ~30j | 6.639e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.526 | crowd |
| BTC 1h/4h/24h | -0.19 / 0.08 / 1.13 % | B7 |
| Dominance BTC | 58.88% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 76/100).
- Funding maintenant 6.2e-05. Moyenne ~30j 6.639e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.526.
- BTC 24h 1.13% · 1h -0.19% · 4h 0.08%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.183 · OI 106448.457 (pas de dark pool free temps réel).
- Top traders L/S 1.572.
- Fear & Greed 57 (Greed).
- Market cap crypto ≈ 2.65 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.88%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -8.68 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.548 · murC 90000 (+15.8%) · murP 70000 (-9.9%).
- Volumes cachés proxy : taker buy 0.513 · vol perp/spot 14.36×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
