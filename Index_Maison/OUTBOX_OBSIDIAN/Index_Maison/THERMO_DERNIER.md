# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-23T17:19Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `84/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83976.63 | prix |
| OI | 99253.738 | C13 |
| Funding | 2e-06 | C14 |
| Funding moy. ~30j | 6.35e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.091 | crowd |
| BTC 1h/4h/24h | -0.04 / -2.08 / -2.59 % | B7 |
| Dominance BTC | 58.82% | A3 |
| Alts ↓ 24h | 90.0% | B9 |

## Lecture
- Climat CALME (score 84/100).
- Funding maintenant 2e-06. Moyenne ~30j 6.35e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.091.
- BTC 24h -2.59% · 1h -0.04% · 4h -2.08%.
- Panier alts : 90.0% en baisse (18/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 2047991$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.9 · OI 99253.738 (pas de dark pool free temps réel).
- Top traders L/S 1.242.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.86 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.82%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 1655.99 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.593 · murC 95000 (+13.1%) · murP 70000 (-16.7%).
- Volumes cachés proxy : taker buy 0.499 · vol perp/spot 13.18×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
