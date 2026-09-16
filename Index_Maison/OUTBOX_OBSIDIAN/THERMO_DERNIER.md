# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-16T14:10Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `72/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 75507.76 | prix |
| OI | 107088.351 | C13 |
| Funding | 3.7e-05 | C14 |
| Funding moy. ~30j | 6.71e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.81 | crowd |
| BTC 1h/4h/24h | -0.14 / -0.6 / -1.23 % | B7 |
| Dominance BTC | 58.49% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat CALME (score 72/100).
- Funding maintenant 3.7e-05. Moyenne ~30j 6.71e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.81.
- BTC 24h -1.23% · 1h -0.14% · 4h -0.6%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1377765$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.83 · OI 107088.351 (pas de dark pool free temps réel).
- Top traders L/S 1.891.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.58 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.49%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -352.15 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.543 · murC 85000 (+12.7%) · murP 70000 (-7.2%).
- Volumes cachés proxy : taker buy 0.508 · vol perp/spot 12.81×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
