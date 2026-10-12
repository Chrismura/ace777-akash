# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-12T23:06Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `70/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81880.1 | prix |
| OI | 93240.62 | C13 |
| Funding | 8.3e-05 | C14 |
| Funding moy. ~30j | 3.696e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.47 | crowd |
| BTC 1h/4h/24h | -0.29 / -1.14 / -2.2 % | B7 |
| Dominance BTC | 59.23% | A3 |
| Alts ↓ 24h | 85.0% | B9 |

## Lecture
- Climat CALME (score 70/100).
- Funding maintenant 8.3e-05. Moyenne ~30j 3.696e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.47.
- BTC 24h -2.2% · 1h -0.29% · 4h -1.14%.
- Panier alts : 85.0% en baisse (17/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 522613$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.738 · OI 93240.62 (pas de dark pool free temps réel).
- Top traders L/S 1.592.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.78 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.23%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -217.51 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.582 · murC 95000 (+16.2%) · murP 80000 (-2.1%).
- Volumes cachés proxy : taker buy 0.504 · vol perp/spot 11.21×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
