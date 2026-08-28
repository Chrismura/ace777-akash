# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-28T11:22Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `91/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79680.4 | prix |
| OI | 108016.013 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 6.481e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 0.996 | crowd |
| BTC 1h/4h/24h | 0.19 / 0.04 / 0.0 % | B7 |
| Dominance BTC | 59.17% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 91/100).
- Funding maintenant 0.0001. Moyenne ~30j 6.481e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 0.996.
- BTC 24h 0.0% · 1h 0.19% · 4h 0.04%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.096 · OI 108016.013 (pas de dark pool free temps réel).
- Top traders L/S 1.09.
- Fear & Greed 73 (Greed).
- Market cap crypto ≈ 2.70 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.17%).
- Liquidations 24h proxy ≈ 0.03 B$.
- ETF net inflow : BTC 522.28 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.53 · murC 82000 (+2.9%) · murP 70000 (-12.2%).
- Volumes cachés proxy : taker buy 0.496 · vol perp/spot 12.68×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
