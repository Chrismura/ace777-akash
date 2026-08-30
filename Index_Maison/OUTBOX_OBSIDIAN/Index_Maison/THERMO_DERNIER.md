# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-30T20:10Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `88/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78842.3 | prix |
| OI | 107093.438 | C13 |
| Funding | 6.3e-05 | C14 |
| Funding moy. ~30j | 6.567e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.059 | crowd |
| BTC 1h/4h/24h | 0.02 / -0.59 / 0.81 % | B7 |
| Dominance BTC | 59.47% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat CALME (score 88/100).
- Funding maintenant 6.3e-05. Moyenne ~30j 6.567e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.059.
- BTC 24h 0.81% · 1h 0.02% · 4h -0.59%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 630567$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.766 · OI 107093.438 (pas de dark pool free temps réel).
- Top traders L/S 1.107.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.66 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.47%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC -295.09 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.574 · murC 82000 (+4.0%) · murP 70000 (-11.2%).
- Volumes cachés proxy : taker buy 0.469 · vol perp/spot 15.58×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
