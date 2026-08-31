# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-31T18:16Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `91/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78957.1 | prix |
| OI | 107307.146 | C13 |
| Funding | 7.8e-05 | C14 |
| Funding moy. ~30j | 6.75e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.027 | crowd |
| BTC 1h/4h/24h | 0.12 / 0.42 / 0.14 % | B7 |
| Dominance BTC | 59.21% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 91/100).
- Funding maintenant 7.8e-05. Moyenne ~30j 6.75e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.027.
- BTC 24h 0.14% · 1h 0.12% · 4h 0.42%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 1165018$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.143 · OI 107307.146 (pas de dark pool free temps réel).
- Top traders L/S 1.084.
- Fear & Greed 62 (Greed).
- Market cap crypto ≈ 2.67 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.21%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 120.62 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.573 · murC 82000 (+3.8%) · murP 70000 (-11.4%).
- Volumes cachés proxy : taker buy 0.502 · vol perp/spot 13.88×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
