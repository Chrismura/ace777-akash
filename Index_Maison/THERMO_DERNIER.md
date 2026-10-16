# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-16T04:21Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `76/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82060.0 | prix |
| OI | 94345.752 | C13 |
| Funding | 6.2e-05 | C14 |
| Funding moy. ~30j | 3.335e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.515 | crowd |
| BTC 1h/4h/24h | -0.03 / -0.29 / 1.17 % | B7 |
| Dominance BTC | 59.28% | A3 |
| Alts ↓ 24h | 5.0% | B9 |

## Lecture
- Climat CALME (score 76/100).
- Funding maintenant 6.2e-05. Moyenne ~30j 3.335e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.515.
- BTC 24h 1.17% · 1h -0.03% · 4h -0.29%.
- Panier alts : 5.0% en baisse (1/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.956 · OI 94345.752 (pas de dark pool free temps réel).
- Top traders L/S 1.629.
- Fear & Greed 63 (Greed).
- Market cap crypto ≈ 2.78 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.28%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -48.9 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.617 · murC 95000 (+15.9%) · murP 78000 (-4.9%).
- Volumes cachés proxy : taker buy 0.555 · vol perp/spot 13.01×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
