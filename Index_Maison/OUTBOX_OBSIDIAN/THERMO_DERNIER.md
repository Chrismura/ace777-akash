# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-19T19:35Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `59/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 68196.5 | prix |
| OI | 109744.401 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.443e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.1 | crowd |
| BTC 1h/4h/24h | -0.26 / -0.5 / 5.39 % | B7 |
| Dominance BTC | 56.94% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat ATTENTION (score 59/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.443e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.1.
- BTC 24h 5.39% · 1h -0.26% · 4h -0.5%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 982835$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.19 · OI 109744.401 (pas de dark pool free temps réel).
- Top traders L/S 1.147.
- Fear & Greed 46 (Fear).
- Market cap crypto ≈ 2.41 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.94%).
- Liquidations 24h proxy ≈ 0.12 B$.
- ETF net inflow : BTC -39.77 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.546 · murC 70000 (+2.6%) · murP 60000 (-12.0%).
- Volumes cachés proxy : taker buy 0.493 · vol perp/spot 13.58×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=476 · heat=100.0 · PnL sess=308.8527 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
