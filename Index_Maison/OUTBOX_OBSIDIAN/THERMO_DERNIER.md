# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-22T02:13Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `65/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78076.7 | prix |
| OI | 105909.818 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.811e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.045 | crowd |
| BTC 1h/4h/24h | 0.34 / -0.47 / 4.5 % | B7 |
| Dominance BTC | 58.76% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat ATTENTION (score 65/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.811e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.045.
- BTC 24h 4.5% · 1h 0.34% · 4h -0.47%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 516354$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.237 · OI 105909.818 (pas de dark pool free temps réel).
- Top traders L/S 1.09.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.65 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.76%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 229.28 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.616 · murC 80000 (+2.5%) · murP 60000 (-23.2%).
- Volumes cachés proxy : taker buy 0.534 · vol perp/spot 12.97×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1405 · heat=100.0 · PnL sess=309.1635 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
