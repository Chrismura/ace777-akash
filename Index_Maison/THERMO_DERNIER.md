# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-11-01T08:08Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `56/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77922.03 | prix |
| OI | 97400.346 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.366e-05 (n=90) | Cortana |
| Funding mois préc. | 4.436e-05 (n=93) | Cortana |
| L/S 1h | 2.499 | crowd |
| BTC 1h/4h/24h | -0.01 / 0.19 / 0.82 % | B7 |
| Dominance BTC | 59.3% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat ATTENTION (score 56/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.366e-05 (90 pts). Mois précédent 4.436e-05 (93 pts).
- Long/Short 2.499.
- BTC 24h 0.82% · 1h -0.01% · 4h 0.19%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 617362$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.784 · OI 97400.346 (pas de dark pool free temps réel).
- Top traders L/S 2.621.
- Fear & Greed 34 (Fear).
- Market cap crypto ≈ 2.64 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.3%).
- Liquidations 24h proxy ≈ 1.53 M$.
- ETF net inflow : BTC 58.8 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.659 · murC 90000 (+15.6%) · murP 60000 (-22.9%).
- Volumes cachés proxy : taker buy 0.537 · vol perp/spot 7.76×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
