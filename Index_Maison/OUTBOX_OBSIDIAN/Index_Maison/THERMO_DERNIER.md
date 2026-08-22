# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-22T00:23Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `60/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78071.7 | prix |
| OI | 105867.412 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.811e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.039 | crowd |
| BTC 1h/4h/24h | -0.33 / 0.73 / 5.91 % | B7 |
| Dominance BTC | 58.96% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat ATTENTION (score 60/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.811e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.039.
- BTC 24h 5.91% · 1h -0.33% · 4h 0.73%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 2300194$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.874 · OI 105867.412 (pas de dark pool free temps réel).
- Top traders L/S 1.087.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.65 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.96%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 229.26 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.617 · murC 80000 (+2.5%) · murP 60000 (-23.1%).
- Volumes cachés proxy : taker buy 0.534 · vol perp/spot 13.28×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1364 · heat=100.0 · PnL sess=302.9919 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
