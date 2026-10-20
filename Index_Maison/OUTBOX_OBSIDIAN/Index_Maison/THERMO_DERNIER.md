# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-20T08:58Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `70/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81422.75 | prix |
| OI | 95153.732 | C13 |
| Funding | 4.6e-05 | C14 |
| Funding moy. ~30j | 3.198e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.73 | crowd |
| BTC 1h/4h/24h | -0.12 / -0.78 / -1.67 % | B7 |
| Dominance BTC | 59.58% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 70/100).
- Funding maintenant 4.6e-05. Moyenne ~30j 3.198e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.73.
- BTC 24h -1.67% · 1h -0.12% · 4h -0.78%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.869 · OI 95153.732 (pas de dark pool free temps réel).
- Top traders L/S 1.843.
- Fear & Greed 55 (Greed).
- Market cap crypto ≈ 2.74 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.58%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -10.5 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.569 · murC 95000 (+16.7%) · murP 75000 (-7.8%).
- Volumes cachés proxy : taker buy 0.459 · vol perp/spot 14.42×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
