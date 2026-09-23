# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-23T21:24Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `84/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84350.45 | prix |
| OI | 98477.78 | C13 |
| Funding | -1.5e-05 | C14 |
| Funding moy. ~30j | 6.35e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.146 | crowd |
| BTC 1h/4h/24h | 0.18 / 0.08 / -2.14 % | B7 |
| Dominance BTC | 58.89% | A3 |
| Alts ↓ 24h | 85.0% | B9 |

## Lecture
- Climat CALME (score 84/100).
- Funding maintenant -1.5e-05. Moyenne ~30j 6.35e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.146.
- BTC 24h -2.14% · 1h 0.18% · 4h 0.08%.
- Panier alts : 85.0% en baisse (17/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 596607$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.82 · OI 98477.78 (pas de dark pool free temps réel).
- Top traders L/S 1.295.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.87 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.89%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 1663.36 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.592 · murC 95000 (+12.6%) · murP 70000 (-17.0%).
- Volumes cachés proxy : taker buy 0.499 · vol perp/spot 13.03×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
