# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-10T18:53Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `85/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82997.5 | prix |
| OI | 92481.843 | C13 |
| Funding | 2e-06 | C14 |
| Funding moy. ~30j | 3.989e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.516 | crowd |
| BTC 1h/4h/24h | -0.09 / 0.05 / 0.64 % | B7 |
| Dominance BTC | 59.1% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat CALME (score 85/100).
- Funding maintenant 2e-06. Moyenne ~30j 3.989e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.516.
- BTC 24h 0.64% · 1h -0.09% · 4h 0.05%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 702690$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.533 · OI 92481.843 (pas de dark pool free temps réel).
- Top traders L/S 1.569.
- Fear & Greed 64 (Greed).
- Market cap crypto ≈ 2.81 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.1%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -31.91 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.574 · murC 95000 (+14.5%) · murP 80000 (-3.6%).
- Volumes cachés proxy : taker buy 0.511 · vol perp/spot 10.74×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
