# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-27T20:32Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `90/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84548.63 | prix |
| OI | 94685.511 | C13 |
| Funding | 3e-05 | C14 |
| Funding moy. ~30j | 5.593e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.19 | crowd |
| BTC 1h/4h/24h | -0.18 / 0.17 / 0.59 % | B7 |
| Dominance BTC | 58.79% | A3 |
| Alts ↓ 24h | 5.0% | B9 |

## Lecture
- Climat CALME (score 90/100).
- Funding maintenant 3e-05. Moyenne ~30j 5.593e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.19.
- BTC 24h 0.59% · 1h -0.18% · 4h 0.17%.
- Panier alts : 5.0% en baisse (1/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 511915$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.576 · OI 94685.511 (pas de dark pool free temps réel).
- Top traders L/S 1.273.
- Fear & Greed 70 (Greed).
- Market cap crypto ≈ 2.89 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.79%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 293.03 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.46 · murC 95000 (+12.3%) · murP 75000 (-11.3%).
- Volumes cachés proxy : taker buy 0.492 · vol perp/spot 14.17×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
