# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-14T20:31Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `68/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 62926.7 | prix |
| OI | 112087.365 | C13 |
| Funding | 3.4e-05 | C14 |
| Funding moy. ~30j | 5.421e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 2.091 | crowd |
| BTC 1h/4h/24h | -0.02 / -0.28 / -0.79 % | B7 |
| Dominance BTC | 56.14% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat ATTENTION (score 68/100).
- Funding maintenant 3.4e-05. Moyenne ~30j 5.421e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 2.091.
- BTC 24h -0.79% · 1h -0.02% · 4h -0.28%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 867854$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.09 · OI 112087.365 (pas de dark pool free temps réel).
- Top traders L/S 2.186.
- Fear & Greed 29 (Fear).
- Market cap crypto ≈ 2.25 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.14%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -199.92 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.533 · murC 70000 (+11.3%) · murP 60000 (-4.6%).
- Volumes cachés proxy : taker buy 0.538 · vol perp/spot 10.77×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1128 · heat=100.0 · PnL sess=169.6072 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
