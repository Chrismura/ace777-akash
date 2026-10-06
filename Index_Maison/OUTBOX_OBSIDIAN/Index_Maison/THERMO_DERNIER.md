# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-06T20:36Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `95/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 85585.7 | prix |
| OI | 95571.195 | C13 |
| Funding | -2.7e-05 | C14 |
| Funding moy. ~30j | 4.607e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.076 | crowd |
| BTC 1h/4h/24h | 0.02 / 0.06 / -0.17 % | B7 |
| Dominance BTC | 58.72% | A3 |
| Alts ↓ 24h | 50.0% | B9 |

## Lecture
- Climat CALME (score 95/100).
- Funding maintenant -2.7e-05. Moyenne ~30j 4.607e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.076.
- BTC 24h -0.17% · 1h 0.02% · 4h 0.06%.
- Panier alts : 50.0% en baisse (10/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1156001$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.142 · OI 95571.195 (pas de dark pool free temps réel).
- Top traders L/S 1.14.
- Fear & Greed 73 (Greed).
- Market cap crypto ≈ 2.93 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.72%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 23.94 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.52 · murC 95000 (+10.9%) · murP 80000 (-6.6%).
- Volumes cachés proxy : taker buy 0.455 · vol perp/spot 12.5×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
