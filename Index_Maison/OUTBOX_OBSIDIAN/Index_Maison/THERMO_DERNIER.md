# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-11-01T19:11Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `62/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77727.9 | prix |
| OI | 96419.125 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.463e-05 (n=90) | Cortana |
| Funding mois préc. | 4.469e-05 (n=93) | Cortana |
| L/S 1h | 2.263 | crowd |
| BTC 1h/4h/24h | -0.16 / -0.28 / 0.15 % | B7 |
| Dominance BTC | 60.02% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat ATTENTION (score 62/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.463e-05 (90 pts). Mois précédent 4.469e-05 (93 pts).
- Long/Short 2.263.
- BTC 24h 0.15% · 1h -0.16% · 4h -0.28%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.765 · OI 96419.125 (pas de dark pool free temps réel).
- Top traders L/S 2.369.
- Fear & Greed 34 (Fear).
- Market cap crypto ≈ 2.60 T$.
- Alt season proxy : Bitcoin season (BTC.D 60.02%).
- Liquidations 24h proxy ≈ 1.57 M$.
- ETF net inflow : BTC 58.65 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.663 · murC 90000 (+15.9%) · murP 60000 (-22.7%).
- Volumes cachés proxy : taker buy 0.528 · vol perp/spot 7.4×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
