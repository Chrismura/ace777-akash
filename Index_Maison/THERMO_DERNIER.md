# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-16T08:25Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `75/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63043.85 | prix |
| OI | 111420.067 | C13 |
| Funding | 2.1e-05 | C14 |
| Funding moy. ~30j | 5.379e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 2.057 | crowd |
| BTC 1h/4h/24h | 0.01 / -0.02 / 0.02 % | B7 |
| Dominance BTC | 56.16% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 75/100).
- Funding maintenant 2.1e-05. Moyenne ~30j 5.379e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 2.057.
- BTC 24h 0.02% · 1h 0.01% · 4h -0.02%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.905 · OI 111420.067 (pas de dark pool free temps réel).
- Top traders L/S 2.126.
- Fear & Greed 34 (Fear).
- Market cap crypto ≈ 2.25 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.16%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -37.87 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.552 · murC 70000 (+11.1%) · murP 60000 (-4.8%).
- Volumes cachés proxy : taker buy 0.483 · vol perp/spot 14.75×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1269 · heat=100.0 · PnL sess=183.2334 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
