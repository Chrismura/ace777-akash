# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-19T18:01Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `73/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81953.8 | prix |
| OI | 95503.059 | C13 |
| Funding | 9.7e-05 | C14 |
| Funding moy. ~30j | 3.239e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.579 | crowd |
| BTC 1h/4h/24h | 0.07 / -0.39 / 0.94 % | B7 |
| Dominance BTC | 59.64% | A3 |
| Alts ↓ 24h | 15.0% | B9 |

## Lecture
- Climat CALME (score 73/100).
- Funding maintenant 9.7e-05. Moyenne ~30j 3.239e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.579.
- BTC 24h 0.94% · 1h 0.07% · 4h -0.39%.
- Panier alts : 15.0% en baisse (3/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 613741$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.928 · OI 95503.059 (pas de dark pool free temps réel).
- Top traders L/S 1.701.
- Fear & Greed 59 (Greed).
- Market cap crypto ≈ 2.76 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.64%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -20.2 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.579 · murC 95000 (+16.0%) · murP 75000 (-8.4%).
- Volumes cachés proxy : taker buy 0.459 · vol perp/spot 13.1×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
