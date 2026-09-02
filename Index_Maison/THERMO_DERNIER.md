# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-02T23:00Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `88/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77004.74 | prix |
| OI | 107631.104 | C13 |
| Funding | 5.7e-05 | C14 |
| Funding moy. ~30j | 6.773e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.215 | crowd |
| BTC 1h/4h/24h | 0.01 / -0.38 / -0.3 % | B7 |
| Dominance BTC | 59.06% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 88/100).
- Funding maintenant 5.7e-05. Moyenne ~30j 6.773e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.215.
- BTC 24h -0.3% · 1h 0.01% · 4h -0.38%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 645920$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.904 · OI 107631.104 (pas de dark pool free temps réel).
- Top traders L/S 1.294.
- Fear & Greed 63 (Greed).
- Market cap crypto ≈ 2.61 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.06%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 59.22 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.55 · murC 82000 (+6.5%) · murP 70000 (-9.1%).
- Volumes cachés proxy : taker buy 0.581 · vol perp/spot 14.57×.
- ACE soft: LIVE=ACE_RADAR_ALIGNED_V4_60M_LIVE_COLOR.log · SKIP=705 · heat=27.4 · PnL sess=-9.1224 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
