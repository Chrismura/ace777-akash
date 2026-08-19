# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-19T16:34Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `55/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 68714.2 | prix |
| OI | 110959.119 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.443e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.236 | crowd |
| BTC 1h/4h/24h | 0.28 / 5.95 / 6.21 % | B7 |
| Dominance BTC | 57.16% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat ATTENTION (score 55/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.443e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.236.
- BTC 24h 6.21% · 1h 0.28% · 4h 5.95%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 980489$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.416 · OI 110959.119 (pas de dark pool free temps réel).
- Top traders L/S 1.258.
- Fear & Greed 46 (Fear).
- Market cap crypto ≈ 2.42 T$.
- Alt season proxy : Bitcoin season (BTC.D 57.16%).
- Liquidations 24h proxy ≈ 0.13 B$.
- ETF net inflow : BTC -40.07 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.542 · murC 70000 (+1.9%) · murP 60000 (-12.7%).
- Volumes cachés proxy : taker buy 0.493 · vol perp/spot 13.68×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=532 · heat=100.0 · PnL sess=311.9424 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
