# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-13T07:31Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `75/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63869.34 | prix |
| OI | 110489.094 | C13 |
| Funding | 8.1e-05 | C14 |
| Funding moy. ~30j | 5.458e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.723 | crowd |
| BTC 1h/4h/24h | -0.07 / 0.39 / 0.24 % | B7 |
| Dominance BTC | 56.3% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 75/100).
- Funding maintenant 8.1e-05. Moyenne ~30j 5.458e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.723.
- BTC 24h 0.24% · 1h -0.07% · 4h 0.39%.
- Panier alts : 40.0% en baisse (2/5).
- Whales proxy : 1 gros print(s) ≥500k$ (max 869590$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.685 · OI 110489.094 (pas de dark pool free temps réel).
- Top traders L/S 1.752.
- Fear & Greed 29 (Fear).
- Market cap crypto ≈ 2.28 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.3%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC 14.77 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.556 · murC 70000 (+9.7%) · murP 60000 (-6.0%).
- Volumes cachés proxy : taker buy 0.494 · vol perp/spot 19.4×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1120 · heat=100.0 · PnL sess=124.17 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
