# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-18T17:18Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `84/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64743.8 | prix |
| OI | 107144.669 | C13 |
| Funding | 3.1e-05 | C14 |
| Funding moy. ~30j | 5.457e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.359 | crowd |
| BTC 1h/4h/24h | -0.1 / 0.86 / 1.02 % | B7 |
| Dominance BTC | 56.67% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 84/100).
- Funding maintenant 3.1e-05. Moyenne ~30j 5.457e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.359.
- BTC 24h 1.02% · 1h -0.1% · 4h 0.86%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1134121$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.938 · OI 107144.669 (pas de dark pool free temps réel).
- Top traders L/S 1.463.
- Fear & Greed 41 (Fear).
- Market cap crypto ≈ 2.29 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.67%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC -87.06 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.562 · murC 70000 (+8.1%) · murP 60000 (-7.3%).
- Volumes cachés proxy : taker buy 0.502 · vol perp/spot 13.38×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1071 · heat=100.0 · PnL sess=268.1651 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
