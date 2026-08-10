# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-10T08:32Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `86/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 65266.7 | prix |
| OI | 107762.467 | C13 |
| Funding | 8.8e-05 | C14 |
| Funding moy. ~30j | 5.435e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.109 | crowd |
| BTC 1h/4h/24h | 0.13 / 0.44 / 0.62 % | B7 |
| Dominance BTC | None% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 86/100).
- Funding maintenant 8.8e-05. Moyenne ~30j 5.435e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.109.
- BTC 24h 0.62% · 1h 0.13% · 4h 0.44%.
- Panier alts : 40.0% en baisse (2/5).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.847 · OI 107762.467 (pas de dark pool free temps réel).
- Top traders L/S 1.187.
- Fear & Greed 30 (Fear).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC 69.44 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.592 · murC 70000 (+7.3%) · murP 60000 (-8.0%).
- Volumes cachés proxy : taker buy 0.518 · vol perp/spot 18.0×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
