# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-16T19:09Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `79/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 75928.4 | prix |
| OI | 108781.571 | C13 |
| Funding | 8.9e-05 | C14 |
| Funding moy. ~30j | 6.667e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.579 | crowd |
| BTC 1h/4h/24h | 0.45 / 0.24 / -0.06 % | B7 |
| Dominance BTC | 58.43% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat CALME (score 79/100).
- Funding maintenant 8.9e-05. Moyenne ~30j 6.667e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.579.
- BTC 24h -0.06% · 1h 0.45% · 4h 0.24%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 944558$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.972 · OI 108781.571 (pas de dark pool free temps réel).
- Top traders L/S 1.645.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.62 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.43%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -354.11 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.541 · murC 90000 (+18.6%) · murP 70000 (-7.8%).
- Volumes cachés proxy : taker buy 0.478 · vol perp/spot 12.3×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
