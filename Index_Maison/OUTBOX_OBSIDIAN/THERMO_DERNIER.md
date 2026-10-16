# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-16T05:18Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `75/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82207.2 | prix |
| OI | 94261.672 | C13 |
| Funding | 7e-05 | C14 |
| Funding moy. ~30j | 3.335e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.53 | crowd |
| BTC 1h/4h/24h | 0.09 / 0.19 / 1.23 % | B7 |
| Dominance BTC | 59.28% | A3 |
| Alts ↓ 24h | 5.0% | B9 |

## Lecture
- Climat CALME (score 75/100).
- Funding maintenant 7e-05. Moyenne ~30j 3.335e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.53.
- BTC 24h 1.23% · 1h 0.09% · 4h 0.19%.
- Panier alts : 5.0% en baisse (1/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 822483$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.918 · OI 94261.672 (pas de dark pool free temps réel).
- Top traders L/S 1.643.
- Fear & Greed 63 (Greed).
- Market cap crypto ≈ 2.78 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.28%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -48.99 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.615 · murC 95000 (+15.7%) · murP 78000 (-5.0%).
- Volumes cachés proxy : taker buy 0.555 · vol perp/spot 12.84×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
