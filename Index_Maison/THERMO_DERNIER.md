# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-31T21:16Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `89/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78803.1 | prix |
| OI | 107444.245 | C13 |
| Funding | 9.3e-05 | C14 |
| Funding moy. ~30j | 6.75e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 0.994 | crowd |
| BTC 1h/4h/24h | -0.04 / -0.08 / 0.37 % | B7 |
| Dominance BTC | 59.2% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 89/100).
- Funding maintenant 9.3e-05. Moyenne ~30j 6.75e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 0.994.
- BTC 24h 0.37% · 1h -0.04% · 4h -0.08%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.857 · OI 107444.245 (pas de dark pool free temps réel).
- Top traders L/S 1.053.
- Fear & Greed 62 (Greed).
- Market cap crypto ≈ 2.67 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.2%).
- Liquidations 24h proxy ≈ 0.04 B$.
- ETF net inflow : BTC 120.39 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.574 · murC 82000 (+4.0%) · murP 70000 (-11.2%).
- Volumes cachés proxy : taker buy 0.502 · vol perp/spot 13.33×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
