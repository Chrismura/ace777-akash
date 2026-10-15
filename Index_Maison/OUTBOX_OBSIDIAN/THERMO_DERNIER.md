# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-15T20:14Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `78/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82269.4 | prix |
| OI | 93635.569 | C13 |
| Funding | 8.3e-05 | C14 |
| Funding moy. ~30j | 3.318e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.52 | crowd |
| BTC 1h/4h/24h | -0.1 / 0.23 / 0.52 % | B7 |
| Dominance BTC | 59.29% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 78/100).
- Funding maintenant 8.3e-05. Moyenne ~30j 3.318e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.52.
- BTC 24h 0.52% · 1h -0.1% · 4h 0.23%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 1819482$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.008 · OI 93635.569 (pas de dark pool free temps réel).
- Top traders L/S 1.595.
- Fear & Greed 53 (Neutral).
- Market cap crypto ≈ 2.78 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.29%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -266.12 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.614 · murC 95000 (+15.5%) · murP 78000 (-5.1%).
- Volumes cachés proxy : taker buy 0.555 · vol perp/spot 13.36×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
