# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-07T19:09Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `72/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83404.7 | prix |
| OI | 95531.034 | C13 |
| Funding | -3e-06 | C14 |
| Funding moy. ~30j | 4.481e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.669 | crowd |
| BTC 1h/4h/24h | 0.02 / -0.01 / -2.39 % | B7 |
| Dominance BTC | 58.82% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 72/100).
- Funding maintenant -3e-06. Moyenne ~30j 4.481e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.669.
- BTC 24h -2.39% · 1h 0.02% · 4h -0.01%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.459 · OI 95531.034 (pas de dark pool free temps réel).
- Top traders L/S 1.751.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.84 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.82%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -87.87 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.534 · murC 95000 (+13.9%) · murP 80000 (-4.1%).
- Volumes cachés proxy : taker buy 0.477 · vol perp/spot 13.32×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
