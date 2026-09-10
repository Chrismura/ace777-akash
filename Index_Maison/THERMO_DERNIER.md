# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-10T18:09Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `70/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77041.28 | prix |
| OI | 107257.803 | C13 |
| Funding | 6.5e-05 | C14 |
| Funding moy. ~30j | 6.807e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.588 | crowd |
| BTC 1h/4h/24h | -0.34 / -0.44 / -1.99 % | B7 |
| Dominance BTC | 58.48% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat CALME (score 70/100).
- Funding maintenant 6.5e-05. Moyenne ~30j 6.807e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.588.
- BTC 24h -1.99% · 1h -0.34% · 4h -0.44%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 1012713$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.091 · OI 107257.803 (pas de dark pool free temps réel).
- Top traders L/S 1.668.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.65 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.48%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -136.81 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.539 · murC 90000 (+16.9%) · murP 70000 (-9.1%).
- Volumes cachés proxy : taker buy 0.447 · vol perp/spot 14.42×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
