# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-12T10:33Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `76/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64109.68 | prix |
| OI | 108038.066 | C13 |
| Funding | 8e-05 | C14 |
| Funding moy. ~30j | 5.514e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.709 | crowd |
| BTC 1h/4h/24h | 0.05 / 0.66 / -0.19 % | B7 |
| Dominance BTC | 56.32% | A3 |
| Alts ↓ 24h | 0.0% | B9 |

## Lecture
- Climat CALME (score 76/100).
- Funding maintenant 8e-05. Moyenne ~30j 5.514e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.709.
- BTC 24h -0.19% · 1h 0.05% · 4h 0.66%.
- Panier alts : 0.0% en baisse (0/5).
- Whales proxy : 1 gros print(s) ≥500k$ (max 502159$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.148 · OI 108038.066 (pas de dark pool free temps réel).
- Top traders L/S 1.777.
- Fear & Greed 27 (Fear).
- Market cap crypto ≈ 2.28 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.32%).
- Liquidations 24h proxy ≈ 0.03 B$.
- ETF net inflow : BTC 37.58 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.575 · murC 70000 (+9.2%) · murP 60000 (-6.4%).
- Volumes cachés proxy : taker buy 0.498 · vol perp/spot 11.87×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
