# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-02T14:45Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `81/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77237.82 | prix |
| OI | 107885.628 | C13 |
| Funding | 4.9e-05 | C14 |
| Funding moy. ~30j | 6.758e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.298 | crowd |
| BTC 1h/4h/24h | 0.15 / 0.77 / -1.43 % | B7 |
| Dominance BTC | 59.06% | A3 |
| Alts ↓ 24h | 70.0% | B9 |

## Lecture
- Climat CALME (score 81/100).
- Funding maintenant 4.9e-05. Moyenne ~30j 6.758e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.298.
- BTC 24h -1.43% · 1h 0.15% · 4h 0.77%.
- Panier alts : 70.0% en baisse (14/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 1044667$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.117 · OI 107885.628 (pas de dark pool free temps réel).
- Top traders L/S 1.365.
- Fear & Greed 63 (Greed).
- Market cap crypto ≈ 2.62 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.06%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 59.4 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.55 · murC 82000 (+6.2%) · murP 70000 (-9.3%).
- Volumes cachés proxy : taker buy 0.521 · vol perp/spot 15.11×.
- ACE soft: LIVE=ACE_RADAR_ALIGNED_V4_60M_LIVE_COLOR.log · SKIP=705 · heat=27.4 · PnL sess=-9.1224 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
