# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-24T16:25Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `61/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79629.6 | prix |
| OI | 95629.185 | C13 |
| Funding | 1e-06 | C14 |
| Funding moy. ~30j | 3.224e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.228 | crowd |
| BTC 1h/4h/24h | -0.17 / -1.38 / -2.25 % | B7 |
| Dominance BTC | 59.57% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat ATTENTION (score 61/100).
- Funding maintenant 1e-06. Moyenne ~30j 3.224e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.228.
- BTC 24h -2.25% · 1h -0.17% · 4h -1.38%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 506495$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.765 · OI 95629.185 (pas de dark pool free temps réel).
- Top traders L/S 2.378.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.69 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.57%).
- Liquidations 24h proxy ≈ 1.63 M$.
- ETF net inflow : BTC 63.5 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.571 · murC 95000 (+19.4%) · murP 75000 (-5.7%).
- Volumes cachés proxy : taker buy 0.536 · vol perp/spot 15.93×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
