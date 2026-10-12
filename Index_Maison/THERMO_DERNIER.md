# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-12T11:28Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `84/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83393.0 | prix |
| OI | 94900.63 | C13 |
| Funding | 5.6e-05 | C14 |
| Funding moy. ~30j | 3.732e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.384 | crowd |
| BTC 1h/4h/24h | -0.09 / -0.68 / 0.46 % | B7 |
| Dominance BTC | 59.51% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 84/100).
- Funding maintenant 5.6e-05. Moyenne ~30j 3.732e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.384.
- BTC 24h 0.46% · 1h -0.09% · 4h -0.68%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 688472$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.04 · OI 94900.63 (pas de dark pool free temps réel).
- Top traders L/S 1.468.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.81 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.51%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -221.53 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.568 · murC 95000 (+14.0%) · murP 80000 (-4.0%).
- Volumes cachés proxy : taker buy 0.476 · vol perp/spot 12.14×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
