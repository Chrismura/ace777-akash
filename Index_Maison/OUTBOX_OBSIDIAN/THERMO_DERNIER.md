# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-30T05:11Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `84/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78122.89 | prix |
| OI | 108416.267 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 6.545e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.139 | crowd |
| BTC 1h/4h/24h | 0.05 / 0.09 / 0.62 % | B7 |
| Dominance BTC | None% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat CALME (score 84/100).
- Funding maintenant 0.0001. Moyenne ~30j 6.545e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.139.
- BTC 24h 0.62% · 1h 0.05% · 4h 0.09%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 745630$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.939 · OI 108416.267 (pas de dark pool free temps réel).
- Top traders L/S 1.2.
- Fear & Greed 69 (Greed).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 201.86 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.569 · murC 82000 (+4.9%) · murP 70000 (-10.4%).
- Volumes cachés proxy : taker buy 0.478 · vol perp/spot 11.45×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
