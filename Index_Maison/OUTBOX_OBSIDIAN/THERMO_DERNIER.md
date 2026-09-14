# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-14T16:42Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `82/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78597.72 | prix |
| OI | 105731.222 | C13 |
| Funding | 3.6e-05 | C14 |
| Funding moy. ~30j | 6.627e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.262 | crowd |
| BTC 1h/4h/24h | 0.06 / 1.2 / 1.68 % | B7 |
| Dominance BTC | 58.59% | A3 |
| Alts ↓ 24h | 50.0% | B9 |

## Lecture
- Climat CALME (score 82/100).
- Funding maintenant 3.6e-05. Moyenne ~30j 6.627e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.262.
- BTC 24h 1.68% · 1h 0.06% · 4h 1.2%.
- Panier alts : 50.0% en baisse (10/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1706965$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.905 · OI 105731.222 (pas de dark pool free temps réel).
- Top traders L/S 1.298.
- Fear & Greed 57 (Greed).
- Market cap crypto ≈ 2.69 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.59%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -364.96 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.546 · murC 85000 (+8.1%) · murP 70000 (-11.0%).
- Volumes cachés proxy : taker buy 0.511 · vol perp/spot 13.61×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
