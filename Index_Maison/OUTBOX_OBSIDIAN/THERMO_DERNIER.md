# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-22T09:23Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `75/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81797.2 | prix |
| OI | 93254.473 | C13 |
| Funding | -1.5e-05 | C14 |
| Funding moy. ~30j | 2.999e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.566 | crowd |
| BTC 1h/4h/24h | -0.02 / -1.18 / -2.04 % | B7 |
| Dominance BTC | 60.02% | A3 |
| Alts ↓ 24h | 90.0% | B9 |

## Lecture
- Climat CALME (score 75/100).
- Funding maintenant -1.5e-05. Moyenne ~30j 2.999e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.566.
- BTC 24h -2.04% · 1h -0.02% · 4h -1.18%.
- Panier alts : 90.0% en baisse (18/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 1235671$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.859 · OI 93254.473 (pas de dark pool free temps réel).
- Top traders L/S 1.717.
- Fear & Greed 68 (Greed).
- Market cap crypto ≈ 2.74 T$.
- Alt season proxy : Bitcoin season (BTC.D 60.02%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 67.55 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.587 · murC 95000 (+16.2%) · murP 75000 (-8.2%).
- Volumes cachés proxy : taker buy 0.4 · vol perp/spot 13.91×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
