# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-22T08:26Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `90/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77239.0 | prix |
| OI | 105699.573 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.919e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.02 | crowd |
| BTC 1h/4h/24h | -0.08 / -1.57 / 0.03 % | B7 |
| Dominance BTC | 58.65% | A3 |
| Alts ↓ 24h | 15.0% | B9 |

## Lecture
- Climat CALME (score 90/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.919e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.02.
- BTC 24h 0.03% · 1h -0.08% · 4h -1.57%.
- Panier alts : 15.0% en baisse (3/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 621431$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.911 · OI 105699.573 (pas de dark pool free temps réel).
- Top traders L/S 1.124.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.64 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.65%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 226.82 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.609 · murC 78000 (+1.0%) · murP 60000 (-22.3%).
- Volumes cachés proxy : taker buy 0.534 · vol perp/spot 12.0×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1363 · heat=100.0 · PnL sess=313.9962 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
