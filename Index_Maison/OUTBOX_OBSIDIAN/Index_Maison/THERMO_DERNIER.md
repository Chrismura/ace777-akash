# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-30T21:12Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `90/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78462.41 | prix |
| OI | 106924.061 | C13 |
| Funding | 7.1e-05 | C14 |
| Funding moy. ~30j | 6.567e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.05 | crowd |
| BTC 1h/4h/24h | -0.13 / -0.67 / 0.46 % | B7 |
| Dominance BTC | 59.54% | A3 |
| Alts ↓ 24h | 50.0% | B9 |

## Lecture
- Climat CALME (score 90/100).
- Funding maintenant 7.1e-05. Moyenne ~30j 6.567e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.05.
- BTC 24h 0.46% · 1h -0.13% · 4h -0.67%.
- Panier alts : 50.0% en baisse (10/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.529 · OI 106924.061 (pas de dark pool free temps réel).
- Top traders L/S 1.103.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.64 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.54%).
- Liquidations 24h proxy ≈ 0.03 B$.
- ETF net inflow : BTC -293.67 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.575 · murC 82000 (+4.5%) · murP 70000 (-10.8%).
- Volumes cachés proxy : taker buy 0.469 · vol perp/spot 15.71×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
