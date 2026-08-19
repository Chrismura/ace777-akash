# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-19T00:39Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `88/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64611.1 | prix |
| OI | 106381.228 | C13 |
| Funding | 1.8e-05 | C14 |
| Funding moy. ~30j | 5.42e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.378 | crowd |
| BTC 1h/4h/24h | -0.13 / 0.1 / 0.3 % | B7 |
| Dominance BTC | 56.63% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 88/100).
- Funding maintenant 1.8e-05. Moyenne ~30j 5.42e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.378.
- BTC 24h 0.3% · 1h -0.13% · 4h 0.1%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.067 · OI 106381.228 (pas de dark pool free temps réel).
- Top traders L/S 1.483.
- Fear & Greed 46 (Fear).
- Market cap crypto ≈ 2.29 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.63%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -37.68 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.562 · murC 70000 (+8.4%) · murP 60000 (-7.1%).
- Volumes cachés proxy : taker buy 0.502 · vol perp/spot 14.06×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1174 · heat=100.0 · PnL sess=268.7693 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
