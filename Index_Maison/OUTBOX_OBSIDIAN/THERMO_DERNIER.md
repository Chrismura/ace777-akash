# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-17T01:23Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `67/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63081.86 | prix |
| OI | 111110.829 | C13 |
| Funding | 5.7e-05 | C14 |
| Funding moy. ~30j | 5.375e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 2.223 | crowd |
| BTC 1h/4h/24h | 0.31 / 0.29 / 0.06 % | B7 |
| Dominance BTC | 56.15% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat ATTENTION (score 67/100).
- Funding maintenant 5.7e-05. Moyenne ~30j 5.375e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 2.223.
- BTC 24h 0.06% · 1h 0.31% · 4h 0.29%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.25 · OI 111110.829 (pas de dark pool free temps réel).
- Top traders L/S 2.286.
- Fear & Greed 31 (Fear).
- Market cap crypto ≈ 2.25 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.15%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -55.62 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.558 · murC 70000 (+11.0%) · murP 60000 (-4.8%).
- Volumes cachés proxy : taker buy 0.488 · vol perp/spot 16.5×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1147 · heat=100.0 · PnL sess=181.0905 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
