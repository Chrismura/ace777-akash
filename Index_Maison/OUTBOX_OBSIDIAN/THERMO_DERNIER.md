# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-19T01:11Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `72/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82420.3 | prix |
| OI | 93875.165 | C13 |
| Funding | 6.7e-05 | C14 |
| Funding moy. ~30j | 3.261e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.706 | crowd |
| BTC 1h/4h/24h | 0.2 / 1.54 / 1.13 % | B7 |
| Dominance BTC | 60.14% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat CALME (score 72/100).
- Funding maintenant 6.7e-05. Moyenne ~30j 3.261e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.706.
- BTC 24h 1.13% · 1h 0.2% · 4h 1.54%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 661639$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.194 · OI 93875.165 (pas de dark pool free temps réel).
- Top traders L/S 1.786.
- Fear & Greed 59 (Greed).
- Market cap crypto ≈ 2.75 T$.
- Alt season proxy : Bitcoin season (BTC.D 60.14%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -20.32 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.589 · murC 95000 (+15.3%) · murP 80000 (-2.9%).
- Volumes cachés proxy : taker buy 0.455 · vol perp/spot 15.02×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
