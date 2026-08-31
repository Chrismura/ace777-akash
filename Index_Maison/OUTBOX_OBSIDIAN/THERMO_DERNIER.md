# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-31T04:14Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `86/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77552.9 | prix |
| OI | 106634.091 | C13 |
| Funding | 8.2e-05 | C14 |
| Funding moy. ~30j | 6.602e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.093 | crowd |
| BTC 1h/4h/24h | -0.22 / -0.45 / -0.73 % | B7 |
| Dominance BTC | 59.67% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 86/100).
- Funding maintenant 8.2e-05. Moyenne ~30j 6.602e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.093.
- BTC 24h -0.73% · 1h -0.22% · 4h -0.45%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.152 · OI 106634.091 (pas de dark pool free temps réel).
- Top traders L/S 1.144.
- Fear & Greed 62 (Greed).
- Market cap crypto ≈ 2.60 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.67%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 119.58 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.583 · murC 82000 (+5.7%) · murP 70000 (-9.8%).
- Volumes cachés proxy : taker buy 0.469 · vol perp/spot 16.52×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
