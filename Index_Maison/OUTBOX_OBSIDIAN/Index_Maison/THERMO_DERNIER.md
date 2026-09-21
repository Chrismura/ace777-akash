# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-21T19:59Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `63/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 86571.12 | prix |
| OI | 110255.652 | C13 |
| Funding | 4e-05 | C14 |
| Funding moy. ~30j | 6.76e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 0.85 | crowd |
| BTC 1h/4h/24h | 0.6 / 0.77 / 6.72 % | B7 |
| Dominance BTC | 59.03% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat ATTENTION (score 63/100).
- Funding maintenant 4e-05. Moyenne ~30j 6.76e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 0.85.
- BTC 24h 6.72% · 1h 0.6% · 4h 0.77%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 751336$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.771 · OI 110255.652 (pas de dark pool free temps réel).
- Top traders L/S 0.927.
- Fear & Greed 70 (Greed).
- Market cap crypto ≈ 2.94 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.03%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -69.66 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.5 · murC 95000 (+9.7%) · murP 70000 (-19.1%).
- Volumes cachés proxy : taker buy 0.54 · vol perp/spot 11.99×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
