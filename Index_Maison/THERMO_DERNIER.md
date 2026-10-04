# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-04T14:58Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `91/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 85239.17 | prix |
| OI | 98844.433 | C13 |
| Funding | 3.1e-05 | C14 |
| Funding moy. ~30j | 4.65e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.165 | crowd |
| BTC 1h/4h/24h | 0.05 / 0.02 / 0.52 % | B7 |
| Dominance BTC | 59.11% | A3 |
| Alts ↓ 24h | 15.0% | B9 |

## Lecture
- Climat CALME (score 91/100).
- Funding maintenant 3.1e-05. Moyenne ~30j 4.65e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.165.
- BTC 24h 0.52% · 1h 0.05% · 4h 0.02%.
- Panier alts : 15.0% en baisse (3/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 691440$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.05 · OI 98844.433 (pas de dark pool free temps réel).
- Top traders L/S 1.196.
- Fear & Greed 65 (Greed).
- Market cap crypto ≈ 2.89 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.11%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 8.22 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.517 · murC 95000 (+11.4%) · murP 80000 (-6.2%).
- Volumes cachés proxy : taker buy 0.491 · vol perp/spot 12.37×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
