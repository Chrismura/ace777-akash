# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-18T14:01Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `77/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81461.51 | prix |
| OI | 92922.505 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 3.291e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.614 | crowd |
| BTC 1h/4h/24h | -0.05 / -0.74 / -0.01 % | B7 |
| Dominance BTC | 59.53% | A3 |
| Alts ↓ 24h | 85.0% | B9 |

## Lecture
- Climat CALME (score 77/100).
- Funding maintenant 0.0001. Moyenne ~30j 3.291e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.614.
- BTC 24h -0.01% · 1h -0.05% · 4h -0.74%.
- Panier alts : 85.0% en baisse (17/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 661220$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.738 · OI 92922.505 (pas de dark pool free temps réel).
- Top traders L/S 1.768.
- Fear & Greed 53 (Neutral).
- Market cap crypto ≈ 2.74 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.53%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -46.24 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.584 · murC 95000 (+16.7%) · murP 75000 (-7.8%).
- Volumes cachés proxy : taker buy 0.531 · vol perp/spot 19.04×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
