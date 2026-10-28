# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-28T23:40Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `71/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81284.84 | prix |
| OI | 95838.046 | C13 |
| Funding | 6.8e-05 | C14 |
| Funding moy. ~30j | 4.02e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.903 | crowd |
| BTC 1h/4h/24h | 0.05 / -0.32 / 0.53 % | B7 |
| Dominance BTC | 59.48% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat CALME (score 71/100).
- Funding maintenant 6.8e-05. Moyenne ~30j 4.02e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.903.
- BTC 24h 0.53% · 1h 0.05% · 4h -0.32%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.933 · OI 95838.046 (pas de dark pool free temps réel).
- Top traders L/S 2.008.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.74 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.48%).
- Liquidations 24h proxy ≈ 4.19 M$.
- ETF net inflow : BTC 132.89 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.586 · murC 95000 (+16.9%) · murP 75000 (-7.7%).
- Volumes cachés proxy : taker buy 0.492 · vol perp/spot 13.78×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
