# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-26T03:45Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `89/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83912.61 | prix |
| OI | 94866.218 | C13 |
| Funding | 2.6e-05 | C14 |
| Funding moy. ~30j | 5.896e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.302 | crowd |
| BTC 1h/4h/24h | -0.08 / -0.17 / -0.31 % | B7 |
| Dominance BTC | 58.27% | A3 |
| Alts ↓ 24h | 10.0% | B9 |

## Lecture
- Climat CALME (score 89/100).
- Funding maintenant 2.6e-05. Moyenne ~30j 5.896e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.302.
- BTC 24h -0.31% · 1h -0.08% · 4h -0.17%.
- Panier alts : 10.0% en baisse (2/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.891 · OI 94866.218 (pas de dark pool free temps réel).
- Top traders L/S 1.404.
- Fear & Greed 74 (Greed).
- Market cap crypto ≈ 2.89 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.27%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 290.83 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.47 · murC 95000 (+13.2%) · murP 78000 (-7.1%).
- Volumes cachés proxy : taker buy 0.484 · vol perp/spot 15.45×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
