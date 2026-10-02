# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-02T09:16Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `72/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 86180.7 | prix |
| OI | 99588.553 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.963e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 0.913 | crowd |
| BTC 1h/4h/24h | -0.04 / 0.24 / 3.03 % | B7 |
| Dominance BTC | 58.73% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 72/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.963e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 0.913.
- BTC 24h 3.03% · 1h -0.04% · 4h 0.24%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.136 · OI 99588.553 (pas de dark pool free temps réel).
- Top traders L/S 0.975.
- Fear & Greed 72 (Greed).
- Market cap crypto ≈ 2.94 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.73%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC 6.84 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.502 · murC 95000 (+10.2%) · murP 75000 (-13.0%).
- Volumes cachés proxy : taker buy 0.526 · vol perp/spot 11.02×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
