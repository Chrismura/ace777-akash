# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-27T02:34Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `60/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79900.5 | prix |
| OI | 96047.45 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 3.669e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 2.255 | crowd |
| BTC 1h/4h/24h | -0.18 / -0.1 / 0.47 % | B7 |
| Dominance BTC | 59.44% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat ATTENTION (score 60/100).
- Funding maintenant 0.0001. Moyenne ~30j 3.669e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 2.255.
- BTC 24h 0.47% · 1h -0.18% · 4h -0.1%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.91 · OI 96047.45 (pas de dark pool free temps réel).
- Top traders L/S 2.378.
- Fear & Greed 48 (Neutral).
- Market cap crypto ≈ 2.70 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.44%).
- Liquidations 24h proxy ≈ 2.27 M$.
- ETF net inflow : BTC -54.76 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.596 · murC 95000 (+19.1%) · murP 75000 (-6.0%).
- Volumes cachés proxy : taker buy 0.5 · vol perp/spot 15.58×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
