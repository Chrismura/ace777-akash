# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-17T00:00Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `75/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 76203.76 | prix |
| OI | 107943.359 | C13 |
| Funding | 9.4e-05 | C14 |
| Funding moy. ~30j | 6.713e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.521 | crowd |
| BTC 1h/4h/24h | 0.03 / 0.07 / 0.8 % | B7 |
| Dominance BTC | 58.38% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat CALME (score 75/100).
- Funding maintenant 9.4e-05. Moyenne ~30j 6.713e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.521.
- BTC 24h 0.8% · 1h 0.03% · 4h 0.07%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 990927$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.899 · OI 107943.359 (pas de dark pool free temps réel).
- Top traders L/S 1.585.
- Fear & Greed 50 (Neutral).
- Market cap crypto ≈ 2.62 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.38%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -355.4 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.549 · murC 90000 (+18.1%) · murP 70000 (-8.1%).
- Volumes cachés proxy : taker buy 0.478 · vol perp/spot 12.64×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
