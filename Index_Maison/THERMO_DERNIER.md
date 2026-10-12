# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-12T02:57Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `86/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83812.0 | prix |
| OI | 93096.475 | C13 |
| Funding | 0.0 | C14 |
| Funding moy. ~30j | 3.76e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.396 | crowd |
| BTC 1h/4h/24h | 0.22 / 0.25 / 0.91 % | B7 |
| Dominance BTC | 59.73% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat CALME (score 86/100).
- Funding maintenant 0.0. Moyenne ~30j 3.76e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.396.
- BTC 24h 0.91% · 1h 0.22% · 4h 0.25%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 954679$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.624 · OI 93096.475 (pas de dark pool free temps réel).
- Top traders L/S 1.491.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.81 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.73%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -72.23 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.563 · murC 95000 (+13.4%) · murP 80000 (-4.5%).
- Volumes cachés proxy : taker buy 0.476 · vol perp/spot 16.01×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
