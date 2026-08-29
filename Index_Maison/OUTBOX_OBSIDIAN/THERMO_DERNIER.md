# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-29T19:11Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `82/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78220.0 | prix |
| OI | 107873.747 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 6.564e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.21 | crowd |
| BTC 1h/4h/24h | 0.13 / 0.51 / 0.68 % | B7 |
| Dominance BTC | 59.02% | A3 |
| Alts ↓ 24h | 10.0% | B9 |

## Lecture
- Climat CALME (score 82/100).
- Funding maintenant 0.0001. Moyenne ~30j 6.564e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.21.
- BTC 24h 0.68% · 1h 0.13% · 4h 0.51%.
- Panier alts : 10.0% en baisse (2/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 2000236$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.512 · OI 107873.747 (pas de dark pool free temps réel).
- Top traders L/S 1.246.
- Fear & Greed 68 (Greed).
- Market cap crypto ≈ 2.66 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.02%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 214.36 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.572 · murC 82000 (+4.8%) · murP 70000 (-10.6%).
- Volumes cachés proxy : taker buy 0.478 · vol perp/spot 11.59×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
