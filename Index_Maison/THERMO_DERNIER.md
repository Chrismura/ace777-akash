# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-16T09:02Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `73/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 75769.9 | prix |
| OI | 107399.863 | C13 |
| Funding | 8e-06 | C14 |
| Funding moy. ~30j | 6.71e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.829 | crowd |
| BTC 1h/4h/24h | 0.07 / -0.23 / -1.48 % | B7 |
| Dominance BTC | 58.49% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 73/100).
- Funding maintenant 8e-06. Moyenne ~30j 6.71e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.829.
- BTC 24h -1.48% · 1h 0.07% · 4h -0.23%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 6042123$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.756 · OI 107399.863 (pas de dark pool free temps réel).
- Top traders L/S 1.896.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.59 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.49%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -55.65 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.544 · murC 85000 (+12.2%) · murP 70000 (-7.6%).
- Volumes cachés proxy : taker buy 0.508 · vol perp/spot 13.2×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
