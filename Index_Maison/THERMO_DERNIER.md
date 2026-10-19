# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-19T12:58Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `79/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82523.99 | prix |
| OI | 94002.237 | C13 |
| Funding | 7.9e-05 | C14 |
| Funding moy. ~30j | 3.261e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.461 | crowd |
| BTC 1h/4h/24h | 0.25 / -0.32 / 0.7 % | B7 |
| Dominance BTC | 60.19% | A3 |
| Alts ↓ 24h | 10.0% | B9 |

## Lecture
- Climat CALME (score 79/100).
- Funding maintenant 7.9e-05. Moyenne ~30j 3.261e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.461.
- BTC 24h 0.7% · 1h 0.25% · 4h -0.32%.
- Panier alts : 10.0% en baisse (2/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.773 · OI 94002.237 (pas de dark pool free temps réel).
- Top traders L/S 1.574.
- Fear & Greed 59 (Greed).
- Market cap crypto ≈ 2.75 T$.
- Alt season proxy : Bitcoin season (BTC.D 60.19%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -20.35 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.573 · murC 95000 (+15.2%) · murP 75000 (-9.0%).
- Volumes cachés proxy : taker buy 0.455 · vol perp/spot 12.88×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
