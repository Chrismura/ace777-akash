# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-10T12:37Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `84/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82784.45 | prix |
| OI | 92664.07 | C13 |
| Funding | -2.2e-05 | C14 |
| Funding moy. ~30j | 4.064e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.524 | crowd |
| BTC 1h/4h/24h | -0.06 / -0.02 / -0.36 % | B7 |
| Dominance BTC | 59.62% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 84/100).
- Funding maintenant -2.2e-05. Moyenne ~30j 4.064e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.524.
- BTC 24h -0.36% · 1h -0.06% · 4h -0.02%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 1221535$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.018 · OI 92664.07 (pas de dark pool free temps réel).
- Top traders L/S 1.587.
- Fear & Greed 64 (Greed).
- Market cap crypto ≈ 2.79 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.62%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -31.83 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.574 · murC 95000 (+14.8%) · murP 80000 (-3.3%).
- Volumes cachés proxy : taker buy 0.476 · vol perp/spot 13.32×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
