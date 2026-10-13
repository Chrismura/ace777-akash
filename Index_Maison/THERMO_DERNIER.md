# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-13T02:53Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `80/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82880.0 | prix |
| OI | 93056.475 | C13 |
| Funding | 2.2e-05 | C14 |
| Funding moy. ~30j | 3.718e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.56 | crowd |
| BTC 1h/4h/24h | 0.57 / 0.92 / -1.09 % | B7 |
| Dominance BTC | 59.37% | A3 |
| Alts ↓ 24h | 85.0% | B9 |

## Lecture
- Climat CALME (score 80/100).
- Funding maintenant 2.2e-05. Moyenne ~30j 3.718e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.56.
- BTC 24h -1.09% · 1h 0.57% · 4h 0.92%.
- Panier alts : 85.0% en baisse (17/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.538 · OI 93056.475 (pas de dark pool free temps réel).
- Top traders L/S 1.684.
- Fear & Greed 57 (Greed).
- Market cap crypto ≈ 2.80 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.37%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -98.04 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.583 · murC 95000 (+14.7%) · murP 80000 (-3.4%).
- Volumes cachés proxy : taker buy 0.504 · vol perp/spot 11.92×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
