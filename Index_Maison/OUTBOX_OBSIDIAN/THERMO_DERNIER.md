# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-19T08:44Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `73/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82880.1 | prix |
| OI | 95054.63 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 3.261e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.446 | crowd |
| BTC 1h/4h/24h | 0.19 / 0.13 / 1.46 % | B7 |
| Dominance BTC | 60.17% | A3 |
| Alts ↓ 24h | 15.0% | B9 |

## Lecture
- Climat CALME (score 73/100).
- Funding maintenant 0.0001. Moyenne ~30j 3.261e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.446.
- BTC 24h 1.46% · 1h 0.19% · 4h 0.13%.
- Panier alts : 15.0% en baisse (3/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 500586$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.23 · OI 95054.63 (pas de dark pool free temps réel).
- Top traders L/S 1.545.
- Fear & Greed 59 (Greed).
- Market cap crypto ≈ 2.77 T$.
- Alt season proxy : Bitcoin season (BTC.D 60.17%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -20.43 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.578 · murC 95000 (+14.8%) · murP 75000 (-9.4%).
- Volumes cachés proxy : taker buy 0.455 · vol perp/spot 13.82×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
