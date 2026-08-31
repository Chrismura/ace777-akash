# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-31T19:14Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `91/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79223.98 | prix |
| OI | 107349.318 | C13 |
| Funding | 7.6e-05 | C14 |
| Funding moy. ~30j | 6.75e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.024 | crowd |
| BTC 1h/4h/24h | 0.3 / 0.85 / 0.28 % | B7 |
| Dominance BTC | 59.22% | A3 |
| Alts ↓ 24h | 65.0% | B9 |

## Lecture
- Climat CALME (score 91/100).
- Funding maintenant 7.6e-05. Moyenne ~30j 6.75e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.024.
- BTC 24h 0.28% · 1h 0.3% · 4h 0.85%.
- Panier alts : 65.0% en baisse (13/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.096 · OI 107349.318 (pas de dark pool free temps réel).
- Top traders L/S 1.077.
- Fear & Greed 62 (Greed).
- Market cap crypto ≈ 2.68 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.22%).
- Liquidations 24h proxy ≈ 0.04 B$.
- ETF net inflow : BTC 121.03 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.574 · murC 82000 (+3.5%) · murP 70000 (-11.7%).
- Volumes cachés proxy : taker buy 0.502 · vol perp/spot 13.58×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
