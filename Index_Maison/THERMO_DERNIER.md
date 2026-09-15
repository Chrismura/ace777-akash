# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-15T01:41Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `84/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77940.7 | prix |
| OI | 103071.902 | C13 |
| Funding | 4.2e-05 | C14 |
| Funding moy. ~30j | 6.655e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.192 | crowd |
| BTC 1h/4h/24h | 0.02 / -1.0 / 1.46 % | B7 |
| Dominance BTC | 58.39% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat CALME (score 84/100).
- Funding maintenant 4.2e-05. Moyenne ~30j 6.655e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.192.
- BTC 24h 1.46% · 1h 0.02% · 4h -1.0%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 572533$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.897 · OI 103071.902 (pas de dark pool free temps réel).
- Top traders L/S 1.24.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.67 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.39%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -60.4 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.546 · murC 85000 (+9.0%) · murP 70000 (-10.2%).
- Volumes cachés proxy : taker buy 0.511 · vol perp/spot 13.18×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
