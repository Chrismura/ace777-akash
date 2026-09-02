# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-02T15:43Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `86/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77309.33 | prix |
| OI | 107856.511 | C13 |
| Funding | 4.1e-05 | C14 |
| Funding moy. ~30j | 6.758e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.259 | crowd |
| BTC 1h/4h/24h | 0.34 / 0.65 / -0.78 % | B7 |
| Dominance BTC | 59.09% | A3 |
| Alts ↓ 24h | 65.0% | B9 |

## Lecture
- Climat CALME (score 86/100).
- Funding maintenant 4.1e-05. Moyenne ~30j 6.758e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.259.
- BTC 24h -0.78% · 1h 0.34% · 4h 0.65%.
- Panier alts : 65.0% en baisse (13/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 765022$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.029 · OI 107856.511 (pas de dark pool free temps réel).
- Top traders L/S 1.328.
- Fear & Greed 63 (Greed).
- Market cap crypto ≈ 2.62 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.09%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 59.46 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.55 · murC 82000 (+6.1%) · murP 70000 (-9.4%).
- Volumes cachés proxy : taker buy 0.521 · vol perp/spot 14.99×.
- ACE soft: LIVE=ACE_RADAR_ALIGNED_V4_60M_LIVE_COLOR.log · SKIP=705 · heat=27.4 · PnL sess=-9.1224 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
