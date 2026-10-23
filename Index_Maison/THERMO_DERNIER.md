# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-23T15:48Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `66/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81566.51 | prix |
| OI | 92596.899 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 3.105e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 2.1 | crowd |
| BTC 1h/4h/24h | -0.25 / -0.19 / 0.06 % | B7 |
| Dominance BTC | 59.41% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat ATTENTION (score 66/100).
- Funding maintenant 0.0001. Moyenne ~30j 3.105e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 2.1.
- BTC 24h 0.06% · 1h -0.25% · 4h -0.19%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.866 · OI 92596.899 (pas de dark pool free temps réel).
- Top traders L/S 2.162.
- Fear & Greed 50 (Neutral).
- Market cap crypto ≈ 2.75 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.41%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 65.05 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.576 · murC 95000 (+16.6%) · murP 75000 (-8.0%).
- Volumes cachés proxy : taker buy 0.529 · vol perp/spot 15.97×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
