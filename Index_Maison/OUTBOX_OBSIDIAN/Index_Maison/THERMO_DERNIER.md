# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-25T15:39Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `87/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83485.3 | prix |
| OI | 95747.526 | C13 |
| Funding | -1.1e-05 | C14 |
| Funding moy. ~30j | 6.023e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.32 | crowd |
| BTC 1h/4h/24h | -0.59 / -1.25 / -0.95 % | B7 |
| Dominance BTC | 58.25% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat CALME (score 87/100).
- Funding maintenant -1.1e-05. Moyenne ~30j 6.023e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.32.
- BTC 24h -0.95% · 1h -0.59% · 4h -1.25%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 924105$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.952 · OI 95747.526 (pas de dark pool free temps réel).
- Top traders L/S 1.425.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.88 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.25%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 289.35 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.47 · murC 95000 (+13.8%) · murP 78000 (-6.6%).
- Volumes cachés proxy : taker buy 0.464 · vol perp/spot 15.32×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
