# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-26T04:08Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `60/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79715.4 | prix |
| OI | 94646.55 | C13 |
| Funding | 5.7e-05 | C14 |
| Funding moy. ~30j | 3.46e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 2.256 | crowd |
| BTC 1h/4h/24h | 0.19 / -0.53 / -1.37 % | B7 |
| Dominance BTC | 60.02% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat ATTENTION (score 60/100).
- Funding maintenant 5.7e-05. Moyenne ~30j 3.46e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 2.256.
- BTC 24h -1.37% · 1h 0.19% · 4h -0.53%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.153 · OI 94646.55 (pas de dark pool free temps réel).
- Top traders L/S 2.384.
- Fear & Greed 50 (Neutral).
- Market cap crypto ≈ 2.66 T$.
- Alt season proxy : Bitcoin season (BTC.D 60.02%).
- Liquidations 24h proxy ≈ 1.50 M$.
- ETF net inflow : BTC 30.21 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.593 · murC 95000 (+19.3%) · murP 75000 (-5.8%).
- Volumes cachés proxy : taker buy 0.481 · vol perp/spot 17.36×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
