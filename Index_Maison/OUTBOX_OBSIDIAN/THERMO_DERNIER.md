# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-19T12:33Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `82/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64477.4 | prix |
| OI | 104695.751 | C13 |
| Funding | 3.7e-05 | C14 |
| Funding moy. ~30j | 5.404e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.587 | crowd |
| BTC 1h/4h/24h | 0.01 / 0.16 / 0.31 % | B7 |
| Dominance BTC | 56.48% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat CALME (score 82/100).
- Funding maintenant 3.7e-05. Moyenne ~30j 5.404e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.587.
- BTC 24h 0.31% · 1h 0.01% · 4h 0.16%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.907 · OI 104695.751 (pas de dark pool free temps réel).
- Top traders L/S 1.695.
- Fear & Greed 46 (Fear).
- Market cap crypto ≈ 2.29 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.48%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -37.6 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.559 · murC 70000 (+8.6%) · murP 60000 (-6.9%).
- Volumes cachés proxy : taker buy 0.502 · vol perp/spot 14.38×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1140 · heat=100.0 · PnL sess=287.2257 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
