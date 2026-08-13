# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-13T22:21Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `71/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63553.2 | prix |
| OI | 109696.791 | C13 |
| Funding | 9.8e-05 | C14 |
| Funding moy. ~30j | 5.524e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.884 | crowd |
| BTC 1h/4h/24h | 0.17 / 0.42 / 0.12 % | B7 |
| Dominance BTC | 56.27% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat CALME (score 71/100).
- Funding maintenant 9.8e-05. Moyenne ~30j 5.524e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.884.
- BTC 24h 0.12% · 1h 0.17% · 4h 0.42%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 726350$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.367 · OI 109696.791 (pas de dark pool free temps réel).
- Top traders L/S 1.939.
- Fear & Greed 29 (Fear).
- Market cap crypto ≈ 2.27 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.27%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC 14.7 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.554 · murC 70000 (+10.2%) · murP 60000 (-5.5%).
- Volumes cachés proxy : taker buy 0.544 · vol perp/spot 13.36×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1125 · heat=100.0 · PnL sess=115.7714 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
