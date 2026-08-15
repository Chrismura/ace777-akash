# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-15T20:13Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `73/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63050.8 | prix |
| OI | 111589.291 | C13 |
| Funding | 2.9e-05 | C14 |
| Funding moy. ~30j | 5.449e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 2.08 | crowd |
| BTC 1h/4h/24h | -0.07 / -0.02 / 0.12 % | B7 |
| Dominance BTC | 56.11% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat CALME (score 73/100).
- Funding maintenant 2.9e-05. Moyenne ~30j 5.449e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 2.08.
- BTC 24h 0.12% · 1h -0.07% · 4h -0.02%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1025412$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.24 · OI 111589.291 (pas de dark pool free temps réel).
- Top traders L/S 2.144.
- Fear & Greed 34 (Fear).
- Market cap crypto ≈ 2.25 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.11%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -26.49 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.555 · murC 70000 (+11.1%) · murP 60000 (-4.8%).
- Volumes cachés proxy : taker buy 0.483 · vol perp/spot 13.96×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1215 · heat=100.0 · PnL sess=182.8797 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
