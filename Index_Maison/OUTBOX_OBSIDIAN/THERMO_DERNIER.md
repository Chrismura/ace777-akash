# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-13T14:54Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `74/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63865.87 | prix |
| OI | 110760.426 | C13 |
| Funding | 7.3e-05 | C14 |
| Funding moy. ~30j | 5.499e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.744 | crowd |
| BTC 1h/4h/24h | 0.25 / 0.37 / 0.59 % | B7 |
| Dominance BTC | 56.34% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat CALME (score 74/100).
- Funding maintenant 7.3e-05. Moyenne ~30j 5.499e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.744.
- BTC 24h 0.59% · 1h 0.25% · 4h 0.37%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 943628$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.004 · OI 110760.426 (pas de dark pool free temps réel).
- Top traders L/S 1.777.
- Fear & Greed 29 (Fear).
- Market cap crypto ≈ 2.28 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.34%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC 14.77 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.549 · murC 70000 (+9.7%) · murP 60000 (-6.0%).
- Volumes cachés proxy : taker buy 0.494 · vol perp/spot 12.75×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1041 · heat=100.0 · PnL sess=125.1698 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
