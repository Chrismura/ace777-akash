# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-15T19:10Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `76/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82407.31 | prix |
| OI | 93765.016 | C13 |
| Funding | 7.6e-05 | C14 |
| Funding moy. ~30j | 3.318e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.537 | crowd |
| BTC 1h/4h/24h | 0.03 / 0.03 / 0.93 % | B7 |
| Dominance BTC | 59.33% | A3 |
| Alts ↓ 24h | 50.0% | B9 |

## Lecture
- Climat CALME (score 76/100).
- Funding maintenant 7.6e-05. Moyenne ~30j 3.318e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.537.
- BTC 24h 0.93% · 1h 0.03% · 4h 0.03%.
- Panier alts : 50.0% en baisse (10/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 612180$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.959 · OI 93765.016 (pas de dark pool free temps réel).
- Top traders L/S 1.613.
- Fear & Greed 53 (Neutral).
- Market cap crypto ≈ 2.79 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.33%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -266.56 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.614 · murC 95000 (+15.4%) · murP 78000 (-5.3%).
- Volumes cachés proxy : taker buy 0.555 · vol perp/spot 13.3×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
