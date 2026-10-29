# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-29T02:38Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `69/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79730.1 | prix |
| OI | 96345.411 | C13 |
| Funding | 1.9e-05 | C14 |
| Funding moy. ~30j | 4.046e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.982 | crowd |
| BTC 1h/4h/24h | -0.26 / -1.82 / -1.46 % | B7 |
| Dominance BTC | 59.49% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat ATTENTION (score 69/100).
- Funding maintenant 1.9e-05. Moyenne ~30j 4.046e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.982.
- BTC 24h -1.46% · 1h -0.26% · 4h -1.82%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 1085299$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.638 · OI 96345.411 (pas de dark pool free temps réel).
- Top traders L/S 2.101.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.69 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.49%).
- Liquidations 24h proxy ≈ 3.02 M$.
- ETF net inflow : BTC -0.93 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.592 · murC 95000 (+19.2%) · murP 75000 (-5.9%).
- Volumes cachés proxy : taker buy 0.492 · vol perp/spot 14.56×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
