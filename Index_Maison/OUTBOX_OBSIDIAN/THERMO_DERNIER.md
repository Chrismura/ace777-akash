# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-12T22:49Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `74/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82528.59 | prix |
| OI | 93730.262 | C13 |
| Funding | 8.5e-05 | C14 |
| Funding moy. ~30j | 3.696e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.47 | crowd |
| BTC 1h/4h/24h | -0.01 / 0.15 / -1.32 % | B7 |
| Dominance BTC | 59.26% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat CALME (score 74/100).
- Funding maintenant 8.5e-05. Moyenne ~30j 3.696e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.47.
- BTC 24h -1.32% · 1h -0.01% · 4h 0.15%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.84 · OI 93730.262 (pas de dark pool free temps réel).
- Top traders L/S 1.585.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.79 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.26%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -219.23 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.582 · murC 95000 (+15.2%) · murP 80000 (-3.0%).
- Volumes cachés proxy : taker buy 0.504 · vol perp/spot 11.22×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
