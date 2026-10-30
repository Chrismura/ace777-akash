# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-30T00:48Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `hot` · **Score :** `38/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 76875.49 | prix |
| OI | 94313.146 | C13 |
| Funding | 3.8e-05 | C14 |
| Funding moy. ~30j | 4.08e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 2.366 | crowd |
| BTC 1h/4h/24h | -1.38 / -2.45 / -5.25 % | B7 |
| Dominance BTC | 59.43% | A3 |
| Alts ↓ 24h | 85.0% | B9 |

## Lecture
- Climat CHAUD (score 38/100).
- Funding maintenant 3.8e-05. Moyenne ~30j 4.08e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 2.366.
- BTC 24h -5.25% · 1h -1.38% · 4h -2.45%.
- Panier alts : 85.0% en baisse (17/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.823 · OI 94313.146 (pas de dark pool free temps réel).
- Top traders L/S 2.631.
- Fear & Greed 30 (Fear).
- Market cap crypto ≈ 2.63 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.43%).
- Liquidations 24h proxy ≈ 3.23 M$.
- ETF net inflow : BTC 20.97 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.621 · murC 95000 (+23.7%) · murP 75000 (-2.4%).
- Volumes cachés proxy : taker buy 0.526 · vol perp/spot 13.6×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
