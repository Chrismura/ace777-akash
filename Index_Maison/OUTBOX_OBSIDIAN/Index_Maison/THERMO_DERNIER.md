# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-08T19:17Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `66/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81539.07 | prix |
| OI | 93165.925 | C13 |
| Funding | 2.3e-05 | C14 |
| Funding moy. ~30j | 4.254e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.901 | crowd |
| BTC 1h/4h/24h | 0.09 / 0.68 / -2.2 % | B7 |
| Dominance BTC | 59.16% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat ATTENTION (score 66/100).
- Funding maintenant 2.3e-05. Moyenne ~30j 4.254e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.901.
- BTC 24h -2.2% · 1h 0.09% · 4h 0.68%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.388 · OI 93165.925 (pas de dark pool free temps réel).
- Top traders L/S 2.036.
- Fear & Greed 64 (Greed).
- Market cap crypto ≈ 2.76 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.16%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -329.17 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.598 · murC 95000 (+16.5%) · murP 80000 (-1.9%).
- Volumes cachés proxy : taker buy 0.504 · vol perp/spot 10.87×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
