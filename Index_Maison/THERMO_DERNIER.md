# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-31T02:10Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `89/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77749.9 | prix |
| OI | 106438.519 | C13 |
| Funding | 7.1e-05 | C14 |
| Funding moy. ~30j | 6.602e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.085 | crowd |
| BTC 1h/4h/24h | 0.18 / -0.82 / -0.41 % | B7 |
| Dominance BTC | 59.71% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 89/100).
- Funding maintenant 7.1e-05. Moyenne ~30j 6.602e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.085.
- BTC 24h -0.41% · 1h 0.18% · 4h -0.82%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 524248$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.981 · OI 106438.519 (pas de dark pool free temps réel).
- Top traders L/S 1.134.
- Fear & Greed 62 (Greed).
- Market cap crypto ≈ 2.60 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.71%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 119.88 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.581 · murC 82000 (+5.4%) · murP 70000 (-10.0%).
- Volumes cachés proxy : taker buy 0.469 · vol perp/spot 16.52×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
