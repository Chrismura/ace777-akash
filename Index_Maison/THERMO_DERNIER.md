# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-26T08:16Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `60/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79737.64 | prix |
| OI | 93955.108 | C13 |
| Funding | 7.3e-05 | C14 |
| Funding moy. ~30j | 3.493e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 2.226 | crowd |
| BTC 1h/4h/24h | -0.36 / -0.48 / -1.05 % | B7 |
| Dominance BTC | 60.06% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat ATTENTION (score 60/100).
- Funding maintenant 7.3e-05. Moyenne ~30j 3.493e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 2.226.
- BTC 24h -1.05% · 1h -0.36% · 4h -0.48%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 503242$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.11 · OI 93955.108 (pas de dark pool free temps réel).
- Top traders L/S 2.348.
- Fear & Greed 50 (Neutral).
- Market cap crypto ≈ 2.66 T$.
- Alt season proxy : Bitcoin season (BTC.D 60.06%).
- Liquidations 24h proxy ≈ 1.27 M$.
- ETF net inflow : BTC 30.22 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.592 · murC 95000 (+19.3%) · murP 75000 (-5.8%).
- Volumes cachés proxy : taker buy 0.481 · vol perp/spot 17.42×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
