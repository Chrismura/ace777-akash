# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-22T16:52Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `90/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77352.02 | prix |
| OI | 106633.829 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.937e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 0.992 | crowd |
| BTC 1h/4h/24h | 0.47 / 0.08 / -0.18 % | B7 |
| Dominance BTC | 58.86% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat CALME (score 90/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.937e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 0.992.
- BTC 24h -0.18% · 1h 0.47% · 4h 0.08%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1498500$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.019 · OI 106633.829 (pas de dark pool free temps réel).
- Top traders L/S 1.116.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.64 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.86%).
- Liquidations 24h proxy ≈ 0.04 B$.
- ETF net inflow : BTC 227.15 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.614 · murC 78000 (+0.9%) · murP 60000 (-22.4%).
- Volumes cachés proxy : taker buy 0.5 · vol perp/spot 10.76×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1354 · heat=100.0 · PnL sess=319.4899 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
