# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-23T08:37Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `66/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81782.86 | prix |
| OI | 94988.19 | C13 |
| Funding | 7.2e-05 | C14 |
| Funding moy. ~30j | 3.105e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 2.198 | crowd |
| BTC 1h/4h/24h | 0.28 / 0.26 / -0.17 % | B7 |
| Dominance BTC | 59.41% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat ATTENTION (score 66/100).
- Funding maintenant 7.2e-05. Moyenne ~30j 3.105e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 2.198.
- BTC 24h -0.17% · 1h 0.28% · 4h 0.26%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.075 · OI 94988.19 (pas de dark pool free temps réel).
- Top traders L/S 2.248.
- Fear & Greed 50 (Neutral).
- Market cap crypto ≈ 2.76 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.41%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 65.22 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.567 · murC 95000 (+16.3%) · murP 75000 (-8.2%).
- Volumes cachés proxy : taker buy 0.529 · vol perp/spot 16.47×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
