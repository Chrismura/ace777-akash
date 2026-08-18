# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-18T21:30Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `89/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64593.84 | prix |
| OI | 106560.793 | C13 |
| Funding | 8e-06 | C14 |
| Funding moy. ~30j | 5.457e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.353 | crowd |
| BTC 1h/4h/24h | 0.07 / -0.06 / 0.45 % | B7 |
| Dominance BTC | 56.62% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 89/100).
- Funding maintenant 8e-06. Moyenne ~30j 5.457e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.353.
- BTC 24h 0.45% · 1h 0.07% · 4h -0.06%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 744186$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.693 · OI 106560.793 (pas de dark pool free temps réel).
- Top traders L/S 1.464.
- Fear & Greed 41 (Fear).
- Market cap crypto ≈ 2.29 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.62%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC -86.86 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.563 · murC 70000 (+8.4%) · murP 60000 (-7.1%).
- Volumes cachés proxy : taker buy 0.502 · vol perp/spot 13.36×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1135 · heat=100.0 · PnL sess=269.6945 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
