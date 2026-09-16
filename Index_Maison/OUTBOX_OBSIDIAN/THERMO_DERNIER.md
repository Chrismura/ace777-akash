# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-16T15:08Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `74/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 75610.02 | prix |
| OI | 107358.921 | C13 |
| Funding | 5e-05 | C14 |
| Funding moy. ~30j | 6.71e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.818 | crowd |
| BTC 1h/4h/24h | -0.07 / -0.79 / -0.52 % | B7 |
| Dominance BTC | 58.54% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat CALME (score 74/100).
- Funding maintenant 5e-05. Moyenne ~30j 6.71e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.818.
- BTC 24h -0.52% · 1h -0.07% · 4h -0.79%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 824363$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.939 · OI 107358.921 (pas de dark pool free temps réel).
- Top traders L/S 1.902.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.59 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.54%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -352.63 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.542 · murC 85000 (+12.5%) · murP 70000 (-7.4%).
- Volumes cachés proxy : taker buy 0.508 · vol perp/spot 12.53×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
