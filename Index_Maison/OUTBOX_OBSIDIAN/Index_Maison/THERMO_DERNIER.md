# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-14T18:53Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `72/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 62896.06 | prix |
| OI | 112324.826 | C13 |
| Funding | 2.4e-05 | C14 |
| Funding moy. ~30j | 5.421e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 2.052 | crowd |
| BTC 1h/4h/24h | -0.15 / 0.5 / -0.56 % | B7 |
| Dominance BTC | 56.15% | A3 |
| Alts ↓ 24h | 50.0% | B9 |

## Lecture
- Climat CALME (score 72/100).
- Funding maintenant 2.4e-05. Moyenne ~30j 5.421e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 2.052.
- BTC 24h -0.56% · 1h -0.15% · 4h 0.5%.
- Panier alts : 50.0% en baisse (10/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 772225$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.725 · OI 112324.826 (pas de dark pool free temps réel).
- Top traders L/S 2.148.
- Fear & Greed 29 (Fear).
- Market cap crypto ≈ 2.25 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.15%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -199.83 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.533 · murC 70000 (+11.4%) · murP 60000 (-4.6%).
- Volumes cachés proxy : taker buy 0.538 · vol perp/spot 10.82×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1244 · heat=100.0 · PnL sess=162.5801 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
