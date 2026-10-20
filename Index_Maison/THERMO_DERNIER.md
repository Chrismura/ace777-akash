# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-20T12:00Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `75/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81486.5 | prix |
| OI | 95521.324 | C13 |
| Funding | 2e-05 | C14 |
| Funding moy. ~30j | 3.198e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.811 | crowd |
| BTC 1h/4h/24h | 0.02 / -0.02 / -1.01 % | B7 |
| Dominance BTC | 59.57% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 75/100).
- Funding maintenant 2e-05. Moyenne ~30j 3.198e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.811.
- BTC 24h -1.01% · 1h 0.02% · 4h -0.02%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.581 · OI 95521.324 (pas de dark pool free temps réel).
- Top traders L/S 1.925.
- Fear & Greed 55 (Greed).
- Market cap crypto ≈ 2.74 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.57%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -10.5 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.568 · murC 95000 (+16.7%) · murP 75000 (-7.9%).
- Volumes cachés proxy : taker buy 0.459 · vol perp/spot 15.58×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
