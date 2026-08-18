# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-18T07:51Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `78/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64151.2 | prix |
| OI | 105927.627 | C13 |
| Funding | 4.8e-05 | C14 |
| Funding moy. ~30j | 5.495e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.518 | crowd |
| BTC 1h/4h/24h | -0.23 / 0.01 / 1.03 % | B7 |
| Dominance BTC | 56.54% | A3 |
| Alts ↓ 24h | 65.0% | B9 |

## Lecture
- Climat CALME (score 78/100).
- Funding maintenant 4.8e-05. Moyenne ~30j 5.495e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.518.
- BTC 24h 1.03% · 1h -0.23% · 4h 0.01%.
- Panier alts : 65.0% en baisse (13/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 620278$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.08 · OI 105927.627 (pas de dark pool free temps réel).
- Top traders L/S 1.644.
- Fear & Greed 41 (Fear).
- Market cap crypto ≈ 2.28 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.54%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC -86.26 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.565 · murC 70000 (+9.2%) · murP 60000 (-6.4%).
- Volumes cachés proxy : taker buy 0.555 · vol perp/spot 15.33×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=522 · heat=100.0 · PnL sess=214.0591 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
