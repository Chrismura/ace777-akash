# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-13T16:04Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `87/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83503.38 | prix |
| OI | 94337.884 | C13 |
| Funding | 3.5e-05 | C14 |
| Funding moy. ~30j | 3.718e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.245 | crowd |
| BTC 1h/4h/24h | 0.11 / 0.19 / 0.8 % | B7 |
| Dominance BTC | 59.28% | A3 |
| Alts ↓ 24h | 95.0% | B9 |

## Lecture
- Climat CALME (score 87/100).
- Funding maintenant 3.5e-05. Moyenne ~30j 3.718e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.245.
- BTC 24h 0.8% · 1h 0.11% · 4h 0.19%.
- Panier alts : 95.0% en baisse (19/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 1894213$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.903 · OI 94337.884 (pas de dark pool free temps réel).
- Top traders L/S 1.305.
- Fear & Greed 57 (Greed).
- Market cap crypto ≈ 2.83 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.28%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -102.91 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.583 · murC 95000 (+13.9%) · murP 80000 (-4.1%).
- Volumes cachés proxy : taker buy 0.504 · vol perp/spot 13.11×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
