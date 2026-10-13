# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-13T06:51Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `83/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83735.8 | prix |
| OI | 93571.489 | C13 |
| Funding | 7.9e-05 | C14 |
| Funding moy. ~30j | 3.718e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.378 | crowd |
| BTC 1h/4h/24h | 0.11 / 1.02 / -0.29 % | B7 |
| Dominance BTC | 59.18% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat CALME (score 83/100).
- Funding maintenant 7.9e-05. Moyenne ~30j 3.718e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.378.
- BTC 24h -0.29% · 1h 0.11% · 4h 1.02%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 623669$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.214 · OI 93571.489 (pas de dark pool free temps réel).
- Top traders L/S 1.419.
- Fear & Greed 57 (Greed).
- Market cap crypto ≈ 2.83 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.18%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -99.05 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.584 · murC 95000 (+13.5%) · murP 80000 (-4.4%).
- Volumes cachés proxy : taker buy 0.504 · vol perp/spot 11.79×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
