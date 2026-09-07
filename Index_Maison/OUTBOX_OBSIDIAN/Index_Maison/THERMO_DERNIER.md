# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-07T21:34Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `88/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79178.25 | prix |
| OI | 106911.722 | C13 |
| Funding | 4.3e-05 | C14 |
| Funding moy. ~30j | 6.719e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.156 | crowd |
| BTC 1h/4h/24h | -0.04 / 0.03 / -0.85 % | B7 |
| Dominance BTC | 59.1% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat CALME (score 88/100).
- Funding maintenant 4.3e-05. Moyenne ~30j 6.719e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.156.
- BTC 24h -0.85% · 1h -0.04% · 4h 0.03%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 6862796$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.002 · OI 106911.722 (pas de dark pool free temps réel).
- Top traders L/S 1.266.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.69 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.1%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 122.93 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.525 · murC 90000 (+13.6%) · murP 70000 (-11.6%).
- Volumes cachés proxy : taker buy 0.473 · vol perp/spot 12.38×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_1H30_LIVE_COLOR.log · SKIP=540 · heat=0.7 · PnL sess=-0.2458 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
