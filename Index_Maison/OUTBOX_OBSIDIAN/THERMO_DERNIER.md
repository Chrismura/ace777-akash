# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-15T02:20Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `70/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81678.01 | prix |
| OI | 93342.171 | C13 |
| Funding | -2.3e-05 | C14 |
| Funding moy. ~30j | 3.402e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.791 | crowd |
| BTC 1h/4h/24h | 0.1 / 0.07 / -1.9 % | B7 |
| Dominance BTC | 59.37% | A3 |
| Alts ↓ 24h | 85.0% | B9 |

## Lecture
- Climat CALME (score 70/100).
- Funding maintenant -2.3e-05. Moyenne ~30j 3.402e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.791.
- BTC 24h -1.9% · 1h 0.1% · 4h 0.07%.
- Panier alts : 85.0% en baisse (17/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 1829331$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.89 · OI 93342.171 (pas de dark pool free temps réel).
- Top traders L/S 1.885.
- Fear & Greed 53 (Neutral).
- Market cap crypto ≈ 2.75 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.37%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -22.86 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.615 · murC 95000 (+16.4%) · murP 78000 (-4.4%).
- Volumes cachés proxy : taker buy 0.507 · vol perp/spot 13.42×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
