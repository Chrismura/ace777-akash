# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-27T11:07Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `60/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80060.81 | prix |
| OI | 98144.061 | C13 |
| Funding | 9.1e-05 | C14 |
| Funding moy. ~30j | 3.75e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 2.383 | crowd |
| BTC 1h/4h/24h | 0.14 / 0.35 / -0.3 % | B7 |
| Dominance BTC | 60.03% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat ATTENTION (score 60/100).
- Funding maintenant 9.1e-05. Moyenne ~30j 3.75e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 2.383.
- BTC 24h -0.3% · 1h 0.14% · 4h 0.35%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 3678183$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.864 · OI 98144.061 (pas de dark pool free temps réel).
- Top traders L/S 2.52.
- Fear & Greed 48 (Neutral).
- Market cap crypto ≈ 2.67 T$.
- Alt season proxy : Bitcoin season (BTC.D 60.03%).
- Liquidations 24h proxy ≈ 1.33 M$.
- ETF net inflow : BTC -54.87 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.593 · murC 95000 (+18.8%) · murP 75000 (-6.2%).
- Volumes cachés proxy : taker buy 0.5 · vol perp/spot 16.56×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
