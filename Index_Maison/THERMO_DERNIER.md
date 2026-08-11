# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-11T12:28Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `75/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64278.79 | prix |
| OI | 105770.683 | C13 |
| Funding | 6.5e-05 | C14 |
| Funding moy. ~30j | 5.371e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.59 | crowd |
| BTC 1h/4h/24h | -0.13 / 0.26 / -1.14 % | B7 |
| Dominance BTC | 56.53% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 75/100).
- Funding maintenant 6.5e-05. Moyenne ~30j 5.371e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.59.
- BTC 24h -1.14% · 1h -0.13% · 4h 0.26%.
- Panier alts : 60.0% en baisse (3/5).
- Whales proxy : 1 gros print(s) ≥500k$ (max 728263$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.398 · OI 105770.683 (pas de dark pool free temps réel).
- Top traders L/S 1.646.
- Fear & Greed 29 (Fear).
- Market cap crypto ≈ 2.28 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.53%).
- Liquidations 24h proxy ≈ 0.03 B$.
- ETF net inflow : BTC 120.87 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.582 · murC 70000 (+9.0%) · murP 60000 (-6.6%).
- Volumes cachés proxy : taker buy 0.489 · vol perp/spot 18.18×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
