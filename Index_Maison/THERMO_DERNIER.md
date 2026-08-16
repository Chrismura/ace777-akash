# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-16T02:28Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `77/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63080.84 | prix |
| OI | 111497.448 | C13 |
| Funding | -1e-06 | C14 |
| Funding moy. ~30j | 5.375e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 2.05 | crowd |
| BTC 1h/4h/24h | 0.05 / -0.03 / 0.01 % | B7 |
| Dominance BTC | 56.15% | A3 |
| Alts ↓ 24h | 65.0% | B9 |

## Lecture
- Climat CALME (score 77/100).
- Funding maintenant -1e-06. Moyenne ~30j 5.375e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 2.05.
- BTC 24h 0.01% · 1h 0.05% · 4h -0.03%.
- Panier alts : 65.0% en baisse (13/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1109126$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.09 · OI 111497.448 (pas de dark pool free temps réel).
- Top traders L/S 2.122.
- Fear & Greed 34 (Fear).
- Market cap crypto ≈ 2.25 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.15%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -37.89 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.555 · murC 70000 (+11.0%) · murP 60000 (-4.8%).
- Volumes cachés proxy : taker buy 0.483 · vol perp/spot 13.4×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1277 · heat=100.0 · PnL sess=183.5558 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
