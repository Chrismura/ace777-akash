# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-20T06:39Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `60/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 69716.2 | prix |
| OI | 109686.309 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.49e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.022 | crowd |
| BTC 1h/4h/24h | 0.42 / 0.6 / 8.51 % | B7 |
| Dominance BTC | 58.28% | A3 |
| Alts ↓ 24h | 15.0% | B9 |

## Lecture
- Climat ATTENTION (score 60/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.49e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.022.
- BTC 24h 8.51% · 1h 0.42% · 4h 0.6%.
- Panier alts : 15.0% en baisse (3/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.879 · OI 109686.309 (pas de dark pool free temps réel).
- Top traders L/S 1.154.
- Fear & Greed 62 (Greed).
- Market cap crypto ≈ 2.39 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.28%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC -43.44 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.573 · murC 70000 (+0.5%) · murP 60000 (-13.9%).
- Volumes cachés proxy : taker buy 0.493 · vol perp/spot 12.47×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=458 · heat=100.0 · PnL sess=238.567 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
