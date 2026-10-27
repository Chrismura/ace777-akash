# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-27T13:06Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `62/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80201.63 | prix |
| OI | 97629.725 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 3.75e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 2.287 | crowd |
| BTC 1h/4h/24h | -0.17 / 0.57 / -0.02 % | B7 |
| Dominance BTC | 59.44% | A3 |
| Alts ↓ 24h | 10.0% | B9 |

## Lecture
- Climat ATTENTION (score 62/100).
- Funding maintenant 0.0001. Moyenne ~30j 3.75e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 2.287.
- BTC 24h -0.02% · 1h -0.17% · 4h 0.57%.
- Panier alts : 10.0% en baisse (2/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 522182$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.468 · OI 97629.725 (pas de dark pool free temps réel).
- Top traders L/S 2.414.
- Fear & Greed 48 (Neutral).
- Market cap crypto ≈ 2.71 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.44%).
- Liquidations 24h proxy ≈ 1.43 M$.
- ETF net inflow : BTC -54.97 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.594 · murC 95000 (+18.6%) · murP 75000 (-6.4%).
- Volumes cachés proxy : taker buy 0.5 · vol perp/spot 17.21×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
