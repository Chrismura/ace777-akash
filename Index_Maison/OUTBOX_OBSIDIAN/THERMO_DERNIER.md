# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-12T01:06Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `70/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63736.5 | prix |
| OI | 109415.316 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.473e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.839 | crowd |
| BTC 1h/4h/24h | 0.03 / 0.15 / -0.38 % | B7 |
| Dominance BTC | 56.28% | A3 |
| Alts ↓ 24h | 0.0% | B9 |

## Lecture
- Climat CALME (score 70/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.473e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.839.
- BTC 24h -0.38% · 1h 0.03% · 4h 0.15%.
- Panier alts : 0.0% en baisse (0/5).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.558 · OI 109415.316 (pas de dark pool free temps réel).
- Top traders L/S 1.939.
- Fear & Greed 27 (Fear).
- Market cap crypto ≈ 2.27 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.28%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC 37.36 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.576 · murC 70000 (+9.9%) · murP 60000 (-5.8%).
- Volumes cachés proxy : taker buy 0.498 · vol perp/spot 15.45×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
