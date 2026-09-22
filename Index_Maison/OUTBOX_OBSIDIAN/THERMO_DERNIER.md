# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-22T19:13Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `93/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 86428.59 | prix |
| OI | 107961.038 | C13 |
| Funding | -2.3e-05 | C14 |
| Funding moy. ~30j | 6.654e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 0.914 | crowd |
| BTC 1h/4h/24h | 0.02 / 0.06 / 0.48 % | B7 |
| Dominance BTC | 58.84% | A3 |
| Alts ↓ 24h | 15.0% | B9 |

## Lecture
- Climat CALME (score 93/100).
- Funding maintenant -2.3e-05. Moyenne ~30j 6.654e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 0.914.
- BTC 24h 0.48% · 1h 0.02% · 4h 0.06%.
- Panier alts : 15.0% en baisse (3/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 599805$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.56 · OI 107961.038 (pas de dark pool free temps réel).
- Top traders L/S 1.038.
- Fear & Greed 78 (Extreme Greed).
- Market cap crypto ≈ 2.94 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.84%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -22.13 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.544 · murC 95000 (+9.8%) · murP 70000 (-19.1%).
- Volumes cachés proxy : taker buy 0.555 · vol perp/spot 12.33×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
