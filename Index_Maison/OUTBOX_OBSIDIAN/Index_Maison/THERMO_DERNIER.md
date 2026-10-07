# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-07T02:38Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `83/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83817.33 | prix |
| OI | 96313.364 | C13 |
| Funding | -2.9e-05 | C14 |
| Funding moy. ~30j | 4.568e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.15 | crowd |
| BTC 1h/4h/24h | -0.62 / -1.97 / -2.07 % | B7 |
| Dominance BTC | 58.7% | A3 |
| Alts ↓ 24h | 70.0% | B9 |

## Lecture
- Climat CALME (score 83/100).
- Funding maintenant -2.9e-05. Moyenne ~30j 4.568e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.15.
- BTC 24h -2.07% · 1h -0.62% · 4h -1.97%.
- Panier alts : 70.0% en baisse (14/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 551906$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.507 · OI 96313.364 (pas de dark pool free temps réel).
- Top traders L/S 1.219.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.87 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.7%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 23.44 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.531 · murC 95000 (+13.3%) · murP 80000 (-4.6%).
- Volumes cachés proxy : taker buy 0.455 · vol perp/spot 13.27×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
