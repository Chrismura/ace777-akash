# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-24T17:17Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `91/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84472.07 | prix |
| OI | 95876.099 | C13 |
| Funding | 5e-06 | C14 |
| Funding moy. ~30j | 6.134e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.231 | crowd |
| BTC 1h/4h/24h | -0.02 / 0.26 / 0.66 % | B7 |
| Dominance BTC | 58.59% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat CALME (score 91/100).
- Funding maintenant 5e-06. Moyenne ~30j 6.134e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.231.
- BTC 24h 0.66% · 1h -0.02% · 4h 0.26%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.968 · OI 95876.099 (pas de dark pool free temps réel).
- Top traders L/S 1.321.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.89 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.59%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 292.77 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.636 · murC 95000 (+12.5%) · murP 70000 (-17.1%).
- Volumes cachés proxy : taker buy 0.464 · vol perp/spot 10.78×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
