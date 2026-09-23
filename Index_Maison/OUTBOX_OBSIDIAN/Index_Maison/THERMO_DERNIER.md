# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-23T18:18Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `81/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84157.8 | prix |
| OI | 99183.395 | C13 |
| Funding | -1e-05 | C14 |
| Funding moy. ~30j | 6.35e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.132 | crowd |
| BTC 1h/4h/24h | -0.14 / -0.38 / -2.82 % | B7 |
| Dominance BTC | 58.85% | A3 |
| Alts ↓ 24h | 85.0% | B9 |

## Lecture
- Climat CALME (score 81/100).
- Funding maintenant -1e-05. Moyenne ~30j 6.35e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.132.
- BTC 24h -2.82% · 1h -0.14% · 4h -0.38%.
- Panier alts : 85.0% en baisse (17/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1590243$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.042 · OI 99183.395 (pas de dark pool free temps réel).
- Top traders L/S 1.283.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.87 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.85%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 1659.56 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.593 · murC 95000 (+12.8%) · murP 70000 (-16.9%).
- Volumes cachés proxy : taker buy 0.499 · vol perp/spot 13.1×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
