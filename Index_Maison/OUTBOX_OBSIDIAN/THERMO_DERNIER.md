# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-09T06:45Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `88/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64833.2 | prix |
| OI | 106678.464 | C13 |
| Funding | 8e-05 | C14 |
| Funding moy. ~30j | 5.42e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.172 | crowd |
| BTC 1h/4h/24h | 0.09 / 0.05 / -0.19 % | B7 |
| Dominance BTC | 56.61% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat CALME (score 88/100).
- Funding maintenant 8e-05. Moyenne ~30j 5.42e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.172.
- BTC 24h -0.19% · 1h 0.09% · 4h 0.05%.
- Panier alts : 20.0% en baisse (1/5).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.337 · OI 106678.464 (pas de dark pool free temps réel).
- Top traders L/S 1.268.
- Fear & Greed 31 (Fear).
- Market cap crypto ≈ 2.30 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.61%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 84.24 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.599 · murC 70000 (+8.0%) · murP 60000 (-7.4%).
- Volumes cachés proxy : taker buy 0.503 · vol perp/spot 16.58×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
