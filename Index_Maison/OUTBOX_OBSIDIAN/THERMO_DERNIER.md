# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-25T22:38Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `72/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80486.4 | prix |
| OI | 93288.976 | C13 |
| Funding | 3.2e-05 | C14 |
| Funding moy. ~30j | 3.449e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.122 | crowd |
| BTC 1h/4h/24h | 0.32 / -0.16 / -0.13 % | B7 |
| Dominance BTC | 60.03% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 72/100).
- Funding maintenant 3.2e-05. Moyenne ~30j 3.449e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.122.
- BTC 24h -0.13% · 1h 0.32% · 4h -0.16%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.807 · OI 93288.976 (pas de dark pool free temps réel).
- Top traders L/S 2.265.
- Fear & Greed 54 (Neutral).
- Market cap crypto ≈ 2.69 T$.
- Alt season proxy : Bitcoin season (BTC.D 60.03%).
- Liquidations 24h proxy ≈ 3.51 M$.
- ETF net inflow : BTC -236.33 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.594 · murC 95000 (+18.1%) · murP 75000 (-6.8%).
- Volumes cachés proxy : taker buy 0.481 · vol perp/spot 16.97×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
