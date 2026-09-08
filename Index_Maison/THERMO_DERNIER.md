# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-08T04:35Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `82/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78801.04 | prix |
| OI | 107324.602 | C13 |
| Funding | 8.8e-05 | C14 |
| Funding moy. ~30j | 6.72e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.184 | crowd |
| BTC 1h/4h/24h | -0.12 / -0.64 / -0.97 % | B7 |
| Dominance BTC | 59.05% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 82/100).
- Funding maintenant 8.8e-05. Moyenne ~30j 6.72e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.184.
- BTC 24h -0.97% · 1h -0.12% · 4h -0.64%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 817926$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.869 · OI 107324.602 (pas de dark pool free temps réel).
- Top traders L/S 1.254.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.67 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.05%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 82.21 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.526 · murC 90000 (+14.2%) · murP 70000 (-11.2%).
- Volumes cachés proxy : taker buy 0.473 · vol perp/spot 13.44×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_6H00_LIVE_COLOR.log · SKIP=888 · heat=2.9 · PnL sess=-0.9802 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
