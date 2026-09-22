# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-22T03:04Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `60/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 85681.6 | prix |
| OI | 109102.602 | C13 |
| Funding | 8.8e-05 | C14 |
| Funding moy. ~30j | 6.734e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 0.863 | crowd |
| BTC 1h/4h/24h | -0.0 / -1.04 / 5.25 % | B7 |
| Dominance BTC | 58.86% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat ATTENTION (score 60/100).
- Funding maintenant 8.8e-05. Moyenne ~30j 6.734e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 0.863.
- BTC 24h 5.25% · 1h -0.0% · 4h -1.04%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 564418$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.132 · OI 109102.602 (pas de dark pool free temps réel).
- Top traders L/S 0.99.
- Fear & Greed 78 (Extreme Greed).
- Market cap crypto ≈ 2.92 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.86%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -21.93 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.518 · murC 95000 (+10.9%) · murP 70000 (-18.3%).
- Volumes cachés proxy : taker buy 0.54 · vol perp/spot 11.68×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
