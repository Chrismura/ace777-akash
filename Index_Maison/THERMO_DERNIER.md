# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-10T14:41Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `88/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82980.51 | prix |
| OI | 92446.7 | C13 |
| Funding | -3e-06 | C14 |
| Funding moy. ~30j | 4.064e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.516 | crowd |
| BTC 1h/4h/24h | 0.23 / 0.19 / -0.07 % | B7 |
| Dominance BTC | 59.07% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat CALME (score 88/100).
- Funding maintenant -3e-06. Moyenne ~30j 4.064e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.516.
- BTC 24h -0.07% · 1h 0.23% · 4h 0.19%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.974 · OI 92446.7 (pas de dark pool free temps réel).
- Top traders L/S 1.581.
- Fear & Greed 64 (Greed).
- Market cap crypto ≈ 2.82 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.07%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -31.9 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.575 · murC 95000 (+14.5%) · murP 80000 (-3.6%).
- Volumes cachés proxy : taker buy 0.476 · vol perp/spot 12.13×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
