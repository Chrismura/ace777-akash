# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-26T02:48Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `90/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83993.0 | prix |
| OI | 94910.399 | C13 |
| Funding | 1.5e-05 | C14 |
| Funding moy. ~30j | 5.896e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.305 | crowd |
| BTC 1h/4h/24h | -0.06 / -0.05 / -0.3 % | B7 |
| Dominance BTC | 58.25% | A3 |
| Alts ↓ 24h | 5.0% | B9 |

## Lecture
- Climat CALME (score 90/100).
- Funding maintenant 1.5e-05. Moyenne ~30j 5.896e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.305.
- BTC 24h -0.3% · 1h -0.06% · 4h -0.05%.
- Panier alts : 5.0% en baisse (1/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 727622$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.022 · OI 94910.399 (pas de dark pool free temps réel).
- Top traders L/S 1.408.
- Fear & Greed 74 (Greed).
- Market cap crypto ≈ 2.89 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.25%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 291.11 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.47 · murC 95000 (+13.1%) · murP 78000 (-7.2%).
- Volumes cachés proxy : taker buy 0.484 · vol perp/spot 15.47×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
