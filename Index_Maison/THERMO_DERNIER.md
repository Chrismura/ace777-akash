# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-11T12:14Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `88/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83219.4 | prix |
| OI | 93158.643 | C13 |
| Funding | -2e-06 | C14 |
| Funding moy. ~30j | 3.846e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.44 | crowd |
| BTC 1h/4h/24h | 0.12 / 0.27 / 0.47 % | B7 |
| Dominance BTC | 59.64% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat CALME (score 88/100).
- Funding maintenant -2e-06. Moyenne ~30j 3.846e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.44.
- BTC 24h 0.47% · 1h 0.12% · 4h 0.27%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1477965$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 2.195 · OI 93158.643 (pas de dark pool free temps réel).
- Top traders L/S 1.521.
- Fear & Greed 61 (Greed).
- Market cap crypto ≈ 2.80 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.64%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -31.99 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.563 · murC 95000 (+14.2%) · murP 80000 (-3.8%).
- Volumes cachés proxy : taker buy 0.511 · vol perp/spot 10.34×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
