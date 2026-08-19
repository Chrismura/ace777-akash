# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-19T14:33Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `81/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 65369.5 | prix |
| OI | 108998.798 | C13 |
| Funding | 6.6e-05 | C14 |
| Funding moy. ~30j | 5.404e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.379 | crowd |
| BTC 1h/4h/24h | 0.59 / 1.47 / 0.81 % | B7 |
| Dominance BTC | 56.72% | A3 |
| Alts ↓ 24h | 50.0% | B9 |

## Lecture
- Climat CALME (score 81/100).
- Funding maintenant 6.6e-05. Moyenne ~30j 5.404e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.379.
- BTC 24h 0.81% · 1h 0.59% · 4h 1.47%.
- Panier alts : 50.0% en baisse (10/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 801698$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.049 · OI 108998.798 (pas de dark pool free temps réel).
- Top traders L/S 1.473.
- Fear & Greed 46 (Fear).
- Market cap crypto ≈ 2.31 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.72%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC -38.12 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.556 · murC 70000 (+7.1%) · murP 60000 (-8.2%).
- Volumes cachés proxy : taker buy 0.502 · vol perp/spot 14.53×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=466 · heat=100.0 · PnL sess=291.6661 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
