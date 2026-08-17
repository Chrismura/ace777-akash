# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-17T04:31Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `65/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63445.5 | prix |
| OI | 110367.483 | C13 |
| Funding | 8.6e-05 | C14 |
| Funding moy. ~30j | 5.375e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 2.107 | crowd |
| BTC 1h/4h/24h | 0.06 / 0.89 / 0.51 % | B7 |
| Dominance BTC | 56.22% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat ATTENTION (score 65/100).
- Funding maintenant 8.6e-05. Moyenne ~30j 5.375e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 2.107.
- BTC 24h 0.51% · 1h 0.06% · 4h 0.89%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : 4 gros print(s) ≥500k$ (max 2636238$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.908 · OI 110367.483 (pas de dark pool free temps réel).
- Top traders L/S 2.141.
- Fear & Greed 31 (Fear).
- Market cap crypto ≈ 2.27 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.22%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -55.94 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.558 · murC 70000 (+10.4%) · murP 60000 (-5.4%).
- Volumes cachés proxy : taker buy 0.488 · vol perp/spot 15.84×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1152 · heat=100.0 · PnL sess=182.0032 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
