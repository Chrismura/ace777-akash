# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-28T12:27Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `70/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80936.8 | prix |
| OI | 95920.761 | C13 |
| Funding | 6.5e-05 | C14 |
| Funding moy. ~30j | 4.003e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.827 | crowd |
| BTC 1h/4h/24h | -0.44 / -0.63 / 1.06 % | B7 |
| Dominance BTC | 59.46% | A3 |
| Alts ↓ 24h | 10.0% | B9 |

## Lecture
- Climat CALME (score 70/100).
- Funding maintenant 6.5e-05. Moyenne ~30j 4.003e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.827.
- BTC 24h 1.06% · 1h -0.44% · 4h -0.63%.
- Panier alts : 10.0% en baisse (2/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.813 · OI 95920.761 (pas de dark pool free temps réel).
- Top traders L/S 1.92.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.73 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.46%).
- Liquidations 24h proxy ≈ 1.99 M$.
- ETF net inflow : BTC 132.32 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.586 · murC 95000 (+17.5%) · murP 75000 (-7.2%).
- Volumes cachés proxy : taker buy 0.513 · vol perp/spot 14.55×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
