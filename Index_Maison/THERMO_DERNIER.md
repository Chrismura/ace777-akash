# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-01T04:47Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `82/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84078.81 | prix |
| OI | 95736.044 | C13 |
| Funding | 4.4e-05 | C14 |
| Funding moy. ~30j | 5.025e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.395 | crowd |
| BTC 1h/4h/24h | 0.4 / 0.72 / 0.96 % | B7 |
| Dominance BTC | 58.29% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat CALME (score 82/100).
- Funding maintenant 4.4e-05. Moyenne ~30j 5.025e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.395.
- BTC 24h 0.96% · 1h 0.4% · 4h 0.72%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.107 · OI 95736.044 (pas de dark pool free temps réel).
- Top traders L/S 1.447.
- Fear & Greed 74 (Greed).
- Market cap crypto ≈ 2.89 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.29%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 75.37 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.54 · murC 95000 (+13.0%) · murP 80000 (-4.8%).
- Volumes cachés proxy : taker buy 0.467 · vol perp/spot 11.11×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
