# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-15T12:42Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `71/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 76886.75 | prix |
| OI | 105913.33 | C13 |
| Funding | 9.1e-05 | C14 |
| Funding moy. ~30j | 6.704e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.643 | crowd |
| BTC 1h/4h/24h | -0.01 / -0.1 / -1.19 % | B7 |
| Dominance BTC | 58.28% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat CALME (score 71/100).
- Funding maintenant 9.1e-05. Moyenne ~30j 6.704e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.643.
- BTC 24h -1.19% · 1h -0.01% · 4h -0.1%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 3434508$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.958 · OI 105913.33 (pas de dark pool free temps réel).
- Top traders L/S 1.725.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.64 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.28%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 103.73 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.55 · murC 85000 (+10.5%) · murP 70000 (-9.0%).
- Volumes cachés proxy : taker buy 0.511 · vol perp/spot 13.27×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
