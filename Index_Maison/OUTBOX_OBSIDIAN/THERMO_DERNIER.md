# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-07T13:07Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `72/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83520.7 | prix |
| OI | 96705.371 | C13 |
| Funding | -4e-06 | C14 |
| Funding moy. ~30j | 4.493e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.484 | crowd |
| BTC 1h/4h/24h | 0.07 / -0.29 / -3.03 % | B7 |
| Dominance BTC | 58.81% | A3 |
| Alts ↓ 24h | 85.0% | B9 |

## Lecture
- Climat CALME (score 72/100).
- Funding maintenant -4e-06. Moyenne ~30j 4.493e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.484.
- BTC 24h -3.03% · 1h 0.07% · 4h -0.29%.
- Panier alts : 85.0% en baisse (17/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 766864$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.155 · OI 96705.371 (pas de dark pool free temps réel).
- Top traders L/S 1.577.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.85 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.81%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -87.99 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.529 · murC 95000 (+13.8%) · murP 80000 (-4.2%).
- Volumes cachés proxy : taker buy 0.455 · vol perp/spot 13.26×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
