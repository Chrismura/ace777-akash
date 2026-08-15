# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-14T23:32Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `65/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 62927.4 | prix |
| OI | 112047.141 | C13 |
| Funding | 6.8e-05 | C14 |
| Funding moy. ~30j | 5.421e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 2.11 | crowd |
| BTC 1h/4h/24h | 0.11 / -0.01 / -0.83 % | B7 |
| Dominance BTC | 56.12% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat ATTENTION (score 65/100).
- Funding maintenant 6.8e-05. Moyenne ~30j 5.421e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 2.11.
- BTC 24h -0.83% · 1h 0.11% · 4h -0.01%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 599030$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.097 · OI 112047.141 (pas de dark pool free temps réel).
- Top traders L/S 2.203.
- Fear & Greed 29 (Fear).
- Market cap crypto ≈ 2.25 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.12%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -199.93 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.533 · murC 70000 (+11.3%) · murP 60000 (-4.6%).
- Volumes cachés proxy : taker buy 0.538 · vol perp/spot 10.82×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1251 · heat=100.0 · PnL sess=172.9004 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
