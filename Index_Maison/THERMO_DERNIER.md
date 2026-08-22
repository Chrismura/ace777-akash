# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-22T03:18Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `60/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78538.03 | prix |
| OI | 106051.114 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.811e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.052 | crowd |
| BTC 1h/4h/24h | 0.06 / 0.26 / 5.47 % | B7 |
| Dominance BTC | 58.59% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat ATTENTION (score 60/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.811e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.052.
- BTC 24h 5.47% · 1h 0.06% · 4h 0.26%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 706807$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.279 · OI 106051.114 (pas de dark pool free temps réel).
- Top traders L/S 1.136.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.67 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.59%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 230.63 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.615 · murC 80000 (+1.9%) · murP 60000 (-23.6%).
- Volumes cachés proxy : taker buy 0.534 · vol perp/spot 12.81×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1397 · heat=100.0 · PnL sess=315.7815 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
