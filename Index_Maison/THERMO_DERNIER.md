# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-20T19:44Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `67/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 72716.3 | prix |
| OI | 107800.181 | C13 |
| Funding | 2.6e-05 | C14 |
| Funding moy. ~30j | 5.586e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 0.965 | crowd |
| BTC 1h/4h/24h | 0.44 / 0.4 / 6.37 % | B7 |
| Dominance BTC | 58.69% | A3 |
| Alts ↓ 24h | 5.0% | B9 |

## Lecture
- Climat ATTENTION (score 67/100).
- Funding maintenant 2.6e-05. Moyenne ~30j 5.586e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 0.965.
- BTC 24h 6.37% · 1h 0.44% · 4h 0.4%.
- Panier alts : 5.0% en baisse (1/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.888 · OI 107800.181 (pas de dark pool free temps réel).
- Top traders L/S 1.059.
- Fear & Greed 62 (Greed).
- Market cap crypto ≈ 2.48 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.69%).
- Liquidations 24h proxy ≈ 0.04 B$.
- ETF net inflow : BTC 651.57 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.568 · murC 75000 (+3.2%) · murP 60000 (-17.5%).
- Volumes cachés proxy : taker buy 0.516 · vol perp/spot 11.47×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=743 · heat=100.0 · PnL sess=240.4108 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
