# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-27T18:10Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `91/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84539.4 | prix |
| OI | 94297.007 | C13 |
| Funding | 9e-06 | C14 |
| Funding moy. ~30j | 5.593e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.25 | crowd |
| BTC 1h/4h/24h | 0.01 / 0.06 / 0.56 % | B7 |
| Dominance BTC | 58.81% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat CALME (score 91/100).
- Funding maintenant 9e-06. Moyenne ~30j 5.593e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.25.
- BTC 24h 0.56% · 1h 0.01% · 4h 0.06%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.085 · OI 94297.007 (pas de dark pool free temps réel).
- Top traders L/S 1.348.
- Fear & Greed 70 (Greed).
- Market cap crypto ≈ 2.88 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.81%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 293.0 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.46 · murC 95000 (+12.3%) · murP 75000 (-11.3%).
- Volumes cachés proxy : taker buy 0.492 · vol perp/spot 12.39×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
