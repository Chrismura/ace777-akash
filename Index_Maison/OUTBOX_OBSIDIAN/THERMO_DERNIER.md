# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-23T20:41Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `69/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81363.86 | prix |
| OI | 92321.583 | C13 |
| Funding | 7.4e-05 | C14 |
| Funding moy. ~30j | 3.202e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.088 | crowd |
| BTC 1h/4h/24h | 0.12 / -0.4 / 0.07 % | B7 |
| Dominance BTC | 59.45% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat ATTENTION (score 69/100).
- Funding maintenant 7.4e-05. Moyenne ~30j 3.202e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.088.
- BTC 24h 0.07% · 1h 0.12% · 4h -0.4%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 1604887$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.113 · OI 92321.583 (pas de dark pool free temps réel).
- Top traders L/S 2.147.
- Fear & Greed 50 (Neutral).
- Market cap crypto ≈ 2.74 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.45%).
- Liquidations 24h proxy ≈ 1.95 M$.
- ETF net inflow : BTC 64.89 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.576 · murC 95000 (+16.9%) · murP 75000 (-7.7%).
- Volumes cachés proxy : taker buy 0.505 · vol perp/spot 15.74×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
