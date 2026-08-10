# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-10T16:07Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `80/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64306.72 | prix |
| OI | 105056.997 | C13 |
| Funding | 5.3e-05 | C14 |
| Funding moy. ~30j | 5.445e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.339 | crowd |
| BTC 1h/4h/24h | 0.06 / -0.82 / -1.43 % | B7 |
| Dominance BTC | 56.56% | A3 |
| Alts ↓ 24h | 100.0% | B9 |

## Lecture
- Climat CALME (score 80/100).
- Funding maintenant 5.3e-05. Moyenne ~30j 5.445e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.339.
- BTC 24h -1.43% · 1h 0.06% · 4h -0.82%.
- Panier alts : 100.0% en baisse (5/5).
- Whales proxy : 3 gros print(s) ≥500k$ (max 942451$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.875 · OI 105056.997 (pas de dark pool free temps réel).
- Top traders L/S 1.452.
- Fear & Greed 30 (Fear).
- Market cap crypto ≈ 2.28 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.56%).
- Liquidations 24h proxy ≈ 0.03 B$.
- ETF net inflow : BTC 68.41 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.593 · murC 70000 (+8.9%) · murP 60000 (-6.6%).
- Volumes cachés proxy : taker buy 0.489 · vol perp/spot 17.69×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
