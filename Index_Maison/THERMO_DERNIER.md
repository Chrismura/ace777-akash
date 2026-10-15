# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-15T03:27Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `63/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81104.35 | prix |
| OI | 92307.527 | C13 |
| Funding | -2.5e-05 | C14 |
| Funding moy. ~30j | 3.402e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.785 | crowd |
| BTC 1h/4h/24h | -0.52 / -0.69 / -3.09 % | B7 |
| Dominance BTC | 59.5% | A3 |
| Alts ↓ 24h | 90.0% | B9 |

## Lecture
- Climat ATTENTION (score 63/100).
- Funding maintenant -2.5e-05. Moyenne ~30j 3.402e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.785.
- BTC 24h -3.09% · 1h -0.52% · 4h -0.69%.
- Panier alts : 90.0% en baisse (18/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.768 · OI 92307.527 (pas de dark pool free temps réel).
- Top traders L/S 1.855.
- Fear & Greed 53 (Neutral).
- Market cap crypto ≈ 2.74 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.5%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -22.7 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.616 · murC 95000 (+17.3%) · murP 78000 (-3.7%).
- Volumes cachés proxy : taker buy 0.507 · vol perp/spot 13.64×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
