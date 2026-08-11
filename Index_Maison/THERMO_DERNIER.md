# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-11T10:21Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `74/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64201.0 | prix |
| OI | 105616.88 | C13 |
| Funding | 5.9e-05 | C14 |
| Funding moy. ~30j | 5.371e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.61 | crowd |
| BTC 1h/4h/24h | -0.12 / 0.41 / -1.26 % | B7 |
| Dominance BTC | 56.54% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 74/100).
- Funding maintenant 5.9e-05. Moyenne ~30j 5.371e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.61.
- BTC 24h -1.26% · 1h -0.12% · 4h 0.41%.
- Panier alts : 60.0% en baisse (3/5).
- Whales proxy : 1 gros print(s) ≥500k$ (max 500511$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.24 · OI 105616.88 (pas de dark pool free temps réel).
- Top traders L/S 1.669.
- Fear & Greed 29 (Fear).
- Market cap crypto ≈ 2.28 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.54%).
- Liquidations 24h proxy ≈ 0.03 B$.
- ETF net inflow : BTC 120.72 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.583 · murC 70000 (+9.1%) · murP 60000 (-6.5%).
- Volumes cachés proxy : taker buy 0.489 · vol perp/spot 17.87×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
