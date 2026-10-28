# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-28T16:34Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `70/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80534.9 | prix |
| OI | 97187.834 | C13 |
| Funding | 8.8e-05 | C14 |
| Funding moy. ~30j | 4.02e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.985 | crowd |
| BTC 1h/4h/24h | 0.01 / -0.21 / -0.09 % | B7 |
| Dominance BTC | 59.44% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 70/100).
- Funding maintenant 8.8e-05. Moyenne ~30j 4.02e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.985.
- BTC 24h -0.09% · 1h 0.01% · 4h -0.21%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.921 · OI 97187.834 (pas de dark pool free temps réel).
- Top traders L/S 2.115.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.71 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.44%).
- Liquidations 24h proxy ≈ 2.68 M$.
- ETF net inflow : BTC 131.67 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.583 · murC 95000 (+18.1%) · murP 75000 (-6.8%).
- Volumes cachés proxy : taker buy 0.492 · vol perp/spot 12.64×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
