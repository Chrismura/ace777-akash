# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-17T14:17Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `76/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81449.8 | prix |
| OI | 94443.718 | C13 |
| Funding | 3.9e-05 | C14 |
| Funding moy. ~30j | 3.38e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.689 | crowd |
| BTC 1h/4h/24h | -0.01 / -0.2 / -1.0 % | B7 |
| Dominance BTC | 59.36% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 76/100).
- Funding maintenant 3.9e-05. Moyenne ~30j 3.38e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.689.
- BTC 24h -1.0% · 1h -0.01% · 4h -0.2%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 854423$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.801 · OI 94443.718 (pas de dark pool free temps réel).
- Top traders L/S 1.804.
- Fear & Greed 55 (Greed).
- Market cap crypto ≈ 2.75 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.36%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -46.23 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.582 · murC 95000 (+16.7%) · murP 75000 (-7.8%).
- Volumes cachés proxy : taker buy 0.537 · vol perp/spot 13.24×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
