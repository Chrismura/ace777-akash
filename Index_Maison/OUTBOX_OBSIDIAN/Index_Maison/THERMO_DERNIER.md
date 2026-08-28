# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-28T20:05Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `71/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77481.07 | prix |
| OI | 107145.863 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 6.506e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.143 | crowd |
| BTC 1h/4h/24h | -0.09 / -0.36 / -2.98 % | B7 |
| Dominance BTC | 58.98% | A3 |
| Alts ↓ 24h | 90.0% | B9 |

## Lecture
- Climat CALME (score 71/100).
- Funding maintenant 0.0001. Moyenne ~30j 6.506e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.143.
- BTC 24h -2.98% · 1h -0.09% · 4h -0.36%.
- Panier alts : 90.0% en baisse (18/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.025 · OI 107145.863 (pas de dark pool free temps réel).
- Top traders L/S 1.271.
- Fear & Greed 73 (Greed).
- Market cap crypto ≈ 2.63 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.98%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 507.87 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.57 · murC 82000 (+5.8%) · murP 70000 (-9.7%).
- Volumes cachés proxy : taker buy 0.495 · vol perp/spot 14.41×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
