# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-02T12:38Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `73/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 86798.9 | prix |
| OI | 99441.259 | C13 |
| Funding | 6.2e-05 | C14 |
| Funding moy. ~30j | 4.963e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 0.897 | crowd |
| BTC 1h/4h/24h | 0.47 / 0.67 / 3.51 % | B7 |
| Dominance BTC | 58.85% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 73/100).
- Funding maintenant 6.2e-05. Moyenne ~30j 4.963e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 0.897.
- BTC 24h 3.51% · 1h 0.47% · 4h 0.67%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.083 · OI 99441.259 (pas de dark pool free temps réel).
- Top traders L/S 0.958.
- Fear & Greed 72 (Greed).
- Market cap crypto ≈ 2.97 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.85%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 6.89 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.504 · murC 95000 (+9.4%) · murP 75000 (-13.6%).
- Volumes cachés proxy : taker buy 0.526 · vol perp/spot 10.83×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
