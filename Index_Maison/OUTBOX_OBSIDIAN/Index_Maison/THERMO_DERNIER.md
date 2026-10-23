# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-23T23:30Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `70/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80889.2 | prix |
| OI | 92958.604 | C13 |
| Funding | 3.3e-05 | C14 |
| Funding moy. ~30j | 3.202e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.107 | crowd |
| BTC 1h/4h/24h | 0.13 / -0.45 / -0.49 % | B7 |
| Dominance BTC | 59.49% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 70/100).
- Funding maintenant 3.3e-05. Moyenne ~30j 3.202e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.107.
- BTC 24h -0.49% · 1h 0.13% · 4h -0.45%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.506 · OI 92958.604 (pas de dark pool free temps réel).
- Top traders L/S 2.19.
- Fear & Greed 50 (Neutral).
- Market cap crypto ≈ 2.73 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.49%).
- Liquidations 24h proxy ≈ 2.93 M$.
- ETF net inflow : BTC 64.51 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.576 · murC 95000 (+17.6%) · murP 75000 (-7.2%).
- Volumes cachés proxy : taker buy 0.505 · vol perp/spot 15.58×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
