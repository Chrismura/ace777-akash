# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-16T23:18Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `68/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 62832.64 | prix |
| OI | 110900.42 | C13 |
| Funding | 3.3e-05 | C14 |
| Funding moy. ~30j | 5.367e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 2.222 | crowd |
| BTC 1h/4h/24h | -0.08 / -0.4 / -0.42 % | B7 |
| Dominance BTC | 56.17% | A3 |
| Alts ↓ 24h | 65.0% | B9 |

## Lecture
- Climat ATTENTION (score 68/100).
- Funding maintenant 3.3e-05. Moyenne ~30j 5.367e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 2.222.
- BTC 24h -0.42% · 1h -0.08% · 4h -0.4%.
- Panier alts : 65.0% en baisse (13/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.954 · OI 110900.42 (pas de dark pool free temps réel).
- Top traders L/S 2.285.
- Fear & Greed 34 (Fear).
- Market cap crypto ≈ 2.25 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.17%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -37.74 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.557 · murC 70000 (+11.5%) · murP 60000 (-4.5%).
- Volumes cachés proxy : taker buy 0.488 · vol perp/spot 16.82×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1177 · heat=100.0 · PnL sess=183.0297 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
