# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-09T12:25Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `91/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64915.71 | prix |
| OI | 106367.402 | C13 |
| Funding | 5e-05 | C14 |
| Funding moy. ~30j | 5.413e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.189 | crowd |
| BTC 1h/4h/24h | -0.01 / 0.19 / -0.07 % | B7 |
| Dominance BTC | 56.65% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 91/100).
- Funding maintenant 5e-05. Moyenne ~30j 5.413e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.189.
- BTC 24h -0.07% · 1h -0.01% · 4h 0.19%.
- Panier alts : 60.0% en baisse (3/5).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.886 · OI 106367.402 (pas de dark pool free temps réel).
- Top traders L/S 1.282.
- Fear & Greed 31 (Fear).
- Market cap crypto ≈ 2.30 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.65%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 84.34 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.597 · murC 70000 (+7.9%) · murP 60000 (-7.5%).
- Volumes cachés proxy : taker buy 0.503 · vol perp/spot 17.82×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
