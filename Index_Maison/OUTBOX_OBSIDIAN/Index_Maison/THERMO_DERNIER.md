# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-14T13:59Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `84/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82375.82 | prix |
| OI | 92156.525 | C13 |
| Funding | 2.4e-05 | C14 |
| Funding moy. ~30j | 3.554e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.383 | crowd |
| BTC 1h/4h/24h | -0.4 / -1.02 / -0.97 % | B7 |
| Dominance BTC | 59.33% | A3 |
| Alts ↓ 24h | 65.0% | B9 |

## Lecture
- Climat CALME (score 84/100).
- Funding maintenant 2.4e-05. Moyenne ~30j 3.554e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.383.
- BTC 24h -0.97% · 1h -0.4% · 4h -1.02%.
- Panier alts : 65.0% en baisse (13/20).
- Whales proxy : 4 gros print(s) ≥500k$ (max 731045$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.01 · OI 92156.525 (pas de dark pool free temps réel).
- Top traders L/S 1.475.
- Fear & Greed 62 (Greed).
- Market cap crypto ≈ 2.79 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.33%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 150.49 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.598 · murC 95000 (+15.4%) · murP 78000 (-5.2%).
- Volumes cachés proxy : taker buy 0.467 · vol perp/spot 13.56×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
