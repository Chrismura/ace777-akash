# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-12T05:31Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `85/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83872.98 | prix |
| OI | 93697.266 | C13 |
| Funding | 1.8e-05 | C14 |
| Funding moy. ~30j | 3.76e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.362 | crowd |
| BTC 1h/4h/24h | -0.29 / 0.27 / 1.02 % | B7 |
| Dominance BTC | 59.53% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat CALME (score 85/100).
- Funding maintenant 1.8e-05. Moyenne ~30j 3.76e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.362.
- BTC 24h 1.02% · 1h -0.29% · 4h 0.27%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.282 · OI 93697.266 (pas de dark pool free temps réel).
- Top traders L/S 1.453.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.83 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.53%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -72.28 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.558 · murC 95000 (+13.4%) · murP 80000 (-4.5%).
- Volumes cachés proxy : taker buy 0.476 · vol perp/spot 15.67×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
