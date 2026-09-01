# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-01T23:21Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `78/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77256.97 | prix |
| OI | 108983.8 | C13 |
| Funding | 8.3e-05 | C14 |
| Funding moy. ~30j | 6.762e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.268 | crowd |
| BTC 1h/4h/24h | 0.01 / -0.05 / -1.6 % | B7 |
| Dominance BTC | 59.11% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 78/100).
- Funding maintenant 8.3e-05. Moyenne ~30j 6.762e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.268.
- BTC 24h -1.6% · 1h 0.01% · 4h -0.05%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1321626$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.929 · OI 108983.8 (pas de dark pool free temps réel).
- Top traders L/S 1.373.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.62 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.11%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 188.63 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.566 · murC 82000 (+6.2%) · murP 70000 (-9.4%).
- Volumes cachés proxy : taker buy 0.521 · vol perp/spot 17.12×.
- ACE soft: LIVE=ACE_RADAR_ALIGNED_V3_15M_LIVE_COLOR.log · SKIP=64 · heat=1.4 · PnL sess=-0.4723 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
