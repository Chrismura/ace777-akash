# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-22T12:21Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `87/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77314.67 | prix |
| OI | 106312.284 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.919e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 0.998 | crowd |
| BTC 1h/4h/24h | 0.23 / 0.16 / 0.65 % | B7 |
| Dominance BTC | 58.76% | A3 |
| Alts ↓ 24h | 15.0% | B9 |

## Lecture
- Climat CALME (score 87/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.919e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 0.998.
- BTC 24h 0.65% · 1h 0.23% · 4h 0.16%.
- Panier alts : 15.0% en baisse (3/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1140640$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.272 · OI 106312.284 (pas de dark pool free temps réel).
- Top traders L/S 1.116.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.63 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.76%).
- Liquidations 24h proxy ≈ 0.04 B$.
- ETF net inflow : BTC 227.04 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.611 · murC 78000 (+0.9%) · murP 60000 (-22.4%).
- Volumes cachés proxy : taker buy 0.534 · vol perp/spot 10.83×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1370 · heat=100.0 · PnL sess=314.2916 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
