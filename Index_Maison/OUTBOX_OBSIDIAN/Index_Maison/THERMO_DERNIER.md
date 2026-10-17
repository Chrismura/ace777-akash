# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-17T07:12Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `76/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81606.08 | prix |
| OI | 94130.858 | C13 |
| Funding | 4.6e-05 | C14 |
| Funding moy. ~30j | 3.376e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.721 | crowd |
| BTC 1h/4h/24h | 0.01 / 0.09 / -0.66 % | B7 |
| Dominance BTC | 59.31% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 76/100).
- Funding maintenant 4.6e-05. Moyenne ~30j 3.376e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.721.
- BTC 24h -0.66% · 1h 0.01% · 4h 0.09%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 779851$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.946 · OI 94130.858 (pas de dark pool free temps réel).
- Top traders L/S 1.838.
- Fear & Greed 55 (Greed).
- Market cap crypto ≈ 2.76 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.31%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -46.32 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.59 · murC 95000 (+16.5%) · murP 80000 (-1.9%).
- Volumes cachés proxy : taker buy 0.537 · vol perp/spot 12.47×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
