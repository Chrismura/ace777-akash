# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-25T11:23Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `85/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84981.67 | prix |
| OI | 96074.938 | C13 |
| Funding | -3e-06 | C14 |
| Funding moy. ~30j | 6.023e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.21 | crowd |
| BTC 1h/4h/24h | 0.34 / 1.15 / 1.75 % | B7 |
| Dominance BTC | 58.86% | A3 |
| Alts ↓ 24h | 15.0% | B9 |

## Lecture
- Climat CALME (score 85/100).
- Funding maintenant -3e-06. Moyenne ~30j 6.023e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.21.
- BTC 24h 1.75% · 1h 0.34% · 4h 1.15%.
- Panier alts : 15.0% en baisse (3/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 5183865$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.998 · OI 96074.938 (pas de dark pool free temps réel).
- Top traders L/S 1.307.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.91 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.86%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 294.53 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.467 · murC 95000 (+11.8%) · murP 78000 (-8.2%).
- Volumes cachés proxy : taker buy 0.464 · vol perp/spot 15.23×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
