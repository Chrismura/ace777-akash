# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-12T13:42Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `81/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63970.77 | prix |
| OI | 108119.616 | C13 |
| Funding | 5.3e-05 | C14 |
| Funding moy. ~30j | 5.514e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.569 | crowd |
| BTC 1h/4h/24h | -0.17 / -0.15 / -0.29 % | B7 |
| Dominance BTC | 56.31% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat CALME (score 81/100).
- Funding maintenant 5.3e-05. Moyenne ~30j 5.514e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.569.
- BTC 24h -0.29% · 1h -0.17% · 4h -0.15%.
- Panier alts : 20.0% en baisse (1/5).
- Whales proxy : 1 gros print(s) ≥500k$ (max 595220$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.995 · OI 108119.616 (pas de dark pool free temps réel).
- Top traders L/S 1.64.
- Fear & Greed 27 (Fear).
- Market cap crypto ≈ 2.28 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.31%).
- Liquidations 24h proxy ≈ 0.03 B$.
- ETF net inflow : BTC 37.49 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.553 · murC 70000 (+9.5%) · murP 60000 (-6.1%).
- Volumes cachés proxy : taker buy 0.498 · vol perp/spot 12.3×.
- ACE soft: LIVE=NUAGE_PROD_4H_LIVE_COLOR.log · SKIP=928 · heat=100.0 · PnL sess=172.5426 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
