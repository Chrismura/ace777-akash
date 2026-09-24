# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-24T23:37Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `95/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84423.77 | prix |
| OI | 95794.319 | C13 |
| Funding | -1e-06 | C14 |
| Funding moy. ~30j | 6.134e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.219 | crowd |
| BTC 1h/4h/24h | 0.22 / 0.06 / -0.03 % | B7 |
| Dominance BTC | 58.58% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 95/100).
- Funding maintenant -1e-06. Moyenne ~30j 6.134e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.219.
- BTC 24h -0.03% · 1h 0.22% · 4h 0.06%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 556237$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.749 · OI 95794.319 (pas de dark pool free temps réel).
- Top traders L/S 1.314.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.89 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.58%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 292.6 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.646 · murC 95000 (+12.5%) · murP 70000 (-17.1%).
- Volumes cachés proxy : taker buy 0.464 · vol perp/spot 11.49×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
