# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-31T01:14Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `88/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77603.6 | prix |
| OI | 106330.326 | C13 |
| Funding | 7.3e-05 | C14 |
| Funding moy. ~30j | 6.602e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.081 | crowd |
| BTC 1h/4h/24h | -0.39 / -1.3 / -0.56 % | B7 |
| Dominance BTC | 59.67% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 88/100).
- Funding maintenant 7.3e-05. Moyenne ~30j 6.602e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.081.
- BTC 24h -0.56% · 1h -0.39% · 4h -1.3%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.006 · OI 106330.326 (pas de dark pool free temps réel).
- Top traders L/S 1.153.
- Fear & Greed 62 (Greed).
- Market cap crypto ≈ 2.61 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.67%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 119.66 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.58 · murC 82000 (+5.6%) · murP 70000 (-9.8%).
- Volumes cachés proxy : taker buy 0.469 · vol perp/spot 16.58×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
