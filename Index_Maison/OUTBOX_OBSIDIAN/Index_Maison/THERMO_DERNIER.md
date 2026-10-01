# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-01T07:49Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `86/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83530.1 | prix |
| OI | 96138.492 | C13 |
| Funding | 5e-05 | C14 |
| Funding moy. ~30j | 5.025e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.36 | crowd |
| BTC 1h/4h/24h | -0.65 / -0.22 / 0.2 % | B7 |
| Dominance BTC | 58.29% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 86/100).
- Funding maintenant 5e-05. Moyenne ~30j 5.025e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.36.
- BTC 24h 0.2% · 1h -0.65% · 4h -0.22%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.598 · OI 96138.492 (pas de dark pool free temps réel).
- Top traders L/S 1.411.
- Fear & Greed 74 (Greed).
- Market cap crypto ≈ 2.87 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.29%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 74.88 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.541 · murC 95000 (+13.7%) · murP 80000 (-4.2%).
- Volumes cachés proxy : taker buy 0.467 · vol perp/spot 11.47×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
