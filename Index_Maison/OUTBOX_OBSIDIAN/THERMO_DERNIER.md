# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-28T17:36Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `68/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80645.8 | prix |
| OI | 96928.628 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.02e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.014 | crowd |
| BTC 1h/4h/24h | 0.07 / -0.08 / -0.09 % | B7 |
| Dominance BTC | 59.48% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat ATTENTION (score 68/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.02e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.014.
- BTC 24h -0.09% · 1h 0.07% · 4h -0.08%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 698417$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.037 · OI 96928.628 (pas de dark pool free temps réel).
- Top traders L/S 2.141.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.72 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.48%).
- Liquidations 24h proxy ≈ 2.31 M$.
- ETF net inflow : BTC 131.85 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.583 · murC 95000 (+17.9%) · murP 75000 (-6.9%).
- Volumes cachés proxy : taker buy 0.492 · vol perp/spot 12.94×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
