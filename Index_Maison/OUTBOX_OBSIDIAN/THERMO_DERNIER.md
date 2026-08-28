# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-28T04:17Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `82/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79923.22 | prix |
| OI | 109728.36 | C13 |
| Funding | 9.3e-05 | C14 |
| Funding moy. ~30j | 6.481e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 0.926 | crowd |
| BTC 1h/4h/24h | 0.17 / -0.77 / 1.35 % | B7 |
| Dominance BTC | 59.26% | A3 |
| Alts ↓ 24h | 50.0% | B9 |

## Lecture
- Climat CALME (score 82/100).
- Funding maintenant 9.3e-05. Moyenne ~30j 6.481e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 0.926.
- BTC 24h 1.35% · 1h 0.17% · 4h -0.77%.
- Panier alts : 50.0% en baisse (10/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 2398571$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.308 · OI 109728.36 (pas de dark pool free temps réel).
- Top traders L/S 1.012.
- Fear & Greed 73 (Greed).
- Market cap crypto ≈ 2.70 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.26%).
- Liquidations 24h proxy ≈ 0.04 B$.
- ETF net inflow : BTC 144.27 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.653 · murC 82000 (+2.5%) · murP 70000 (-12.5%).
- Volumes cachés proxy : taker buy 0.496 · vol perp/spot 13.67×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
