# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-25T17:02Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `63/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80750.1 | prix |
| OI | 93641.488 | C13 |
| Funding | 7.7e-05 | C14 |
| Funding moy. ~30j | 3.449e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.145 | crowd |
| BTC 1h/4h/24h | -0.03 / 0.5 / 0.75 % | B7 |
| Dominance BTC | 60.05% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat ATTENTION (score 63/100).
- Funding maintenant 7.7e-05. Moyenne ~30j 3.449e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.145.
- BTC 24h 0.75% · 1h -0.03% · 4h 0.5%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.879 · OI 93641.488 (pas de dark pool free temps réel).
- Top traders L/S 2.282.
- Fear & Greed 54 (Neutral).
- Market cap crypto ≈ 2.70 T$.
- Alt season proxy : Bitcoin season (BTC.D 60.05%).
- Liquidations 24h proxy ≈ 2.34 M$.
- ETF net inflow : BTC -237.11 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.594 · murC 95000 (+17.8%) · murP 75000 (-7.0%).
- Volumes cachés proxy : taker buy 0.481 · vol perp/spot 17.72×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
