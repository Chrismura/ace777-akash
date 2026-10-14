# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-14T19:15Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `74/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81764.8 | prix |
| OI | 92658.252 | C13 |
| Funding | -8e-06 | C14 |
| Funding moy. ~30j | 3.488e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.727 | crowd |
| BTC 1h/4h/24h | 0.1 / 0.2 / -1.68 % | B7 |
| Dominance BTC | 59.3% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 74/100).
- Funding maintenant -8e-06. Moyenne ~30j 3.488e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.727.
- BTC 24h -1.68% · 1h 0.1% · 4h 0.2%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 819819$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.148 · OI 92658.252 (pas de dark pool free temps réel).
- Top traders L/S 1.825.
- Fear & Greed 62 (Greed).
- Market cap crypto ≈ 2.75 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.3%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 149.37 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.611 · murC 95000 (+16.3%) · murP 78000 (-4.5%).
- Volumes cachés proxy : taker buy 0.507 · vol perp/spot 13.63×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
