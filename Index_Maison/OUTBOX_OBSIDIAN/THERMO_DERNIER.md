# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-29T17:30Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `84/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83159.8 | prix |
| OI | 93324.401 | C13 |
| Funding | 2.2e-05 | C14 |
| Funding moy. ~30j | 5.177e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.417 | crowd |
| BTC 1h/4h/24h | 0.16 / -1.19 / -0.85 % | B7 |
| Dominance BTC | 58.32% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 84/100).
- Funding maintenant 2.2e-05. Moyenne ~30j 5.177e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.417.
- BTC 24h -0.85% · 1h 0.16% · 4h -1.19%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 501287$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.897 · OI 93324.401 (pas de dark pool free temps réel).
- Top traders L/S 1.484.
- Fear & Greed 73 (Greed).
- Market cap crypto ≈ 2.86 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.32%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 310.67 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.507 · murC 95000 (+14.2%) · murP 75000 (-9.8%).
- Volumes cachés proxy : taker buy 0.517 · vol perp/spot 13.68×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
