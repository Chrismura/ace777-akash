# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-11-01T02:02Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `58/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77715.0 | prix |
| OI | 96752.713 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.366e-05 (n=90) | Cortana |
| Funding mois préc. | 4.378e-05 (n=93) | Cortana |
| L/S 1h | 2.564 | crowd |
| BTC 1h/4h/24h | 0.05 / 0.28 / 0.48 % | B7 |
| Dominance BTC | 59.23% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat ATTENTION (score 58/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.366e-05 (90 pts). Mois précédent 4.378e-05 (93 pts).
- Long/Short 2.564.
- BTC 24h 0.48% · 1h 0.05% · 4h 0.28%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1307323$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.452 · OI 96752.713 (pas de dark pool free temps réel).
- Top traders L/S 2.724.
- Fear & Greed 34 (Fear).
- Market cap crypto ≈ 2.63 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.23%).
- Liquidations 24h proxy ≈ 1.33 M$.
- ETF net inflow : BTC 58.64 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.677 · murC 90000 (+15.9%) · murP 74000 (-4.7%).
- Volumes cachés proxy : taker buy 0.537 · vol perp/spot 7.23×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
