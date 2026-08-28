# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-28T05:18Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `82/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79621.4 | prix |
| OI | 109934.694 | C13 |
| Funding | 9.5e-05 | C14 |
| Funding moy. ~30j | 6.481e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 0.926 | crowd |
| BTC 1h/4h/24h | -0.01 / -1.07 / 1.28 % | B7 |
| Dominance BTC | 59.25% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 82/100).
- Funding maintenant 9.5e-05. Moyenne ~30j 6.481e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 0.926.
- BTC 24h 1.28% · 1h -0.01% · 4h -1.07%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 1292002$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.7 · OI 109934.694 (pas de dark pool free temps réel).
- Top traders L/S 1.017.
- Fear & Greed 73 (Greed).
- Market cap crypto ≈ 2.69 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.25%).
- Liquidations 24h proxy ≈ 0.04 B$.
- ETF net inflow : BTC 143.73 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.654 · murC 82000 (+3.0%) · murP 70000 (-12.1%).
- Volumes cachés proxy : taker buy 0.496 · vol perp/spot 13.68×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
