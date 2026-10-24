# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-24T19:27Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `66/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80512.0 | prix |
| OI | 96291.043 | C13 |
| Funding | 3e-05 | C14 |
| Funding moy. ~30j | 3.224e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.197 | crowd |
| BTC 1h/4h/24h | 0.0 / 0.94 / -0.94 % | B7 |
| Dominance BTC | 59.58% | A3 |
| Alts ↓ 24h | 70.0% | B9 |

## Lecture
- Climat ATTENTION (score 66/100).
- Funding maintenant 3e-05. Moyenne ~30j 3.224e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.197.
- BTC 24h -0.94% · 1h 0.0% · 4h 0.94%.
- Panier alts : 70.0% en baisse (14/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 805780$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.559 · OI 96291.043 (pas de dark pool free temps réel).
- Top traders L/S 2.325.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.71 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.58%).
- Liquidations 24h proxy ≈ 1.95 M$.
- ETF net inflow : BTC 64.21 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.57 · murC 95000 (+18.1%) · murP 75000 (-6.8%).
- Volumes cachés proxy : taker buy 0.536 · vol perp/spot 15.97×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
