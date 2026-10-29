# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-29T23:51Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `46/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77920.8 | prix |
| OI | 94405.42 | C13 |
| Funding | 3.6e-05 | C14 |
| Funding moy. ~30j | 4.125e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.276 | crowd |
| BTC 1h/4h/24h | -1.36 / -3.6 / -4.11 % | B7 |
| Dominance BTC | 59.36% | A3 |
| Alts ↓ 24h | 85.0% | B9 |

## Lecture
- Climat ATTENTION (score 46/100).
- Funding maintenant 3.6e-05. Moyenne ~30j 4.125e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.276.
- BTC 24h -4.11% · 1h -1.36% · 4h -3.6%.
- Panier alts : 85.0% en baisse (17/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.049 · OI 94405.42 (pas de dark pool free temps réel).
- Top traders L/S 2.5.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.62 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.36%).
- Liquidations 24h proxy ≈ 2.20 M$.
- ETF net inflow : BTC 143.28 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.621 · murC 95000 (+22.2%) · murP 75000 (-3.6%).
- Volumes cachés proxy : taker buy 0.526 · vol perp/spot 14.08×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
