# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-07T22:36Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `86/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78996.24 | prix |
| OI | 107047.553 | C13 |
| Funding | 4.4e-05 | C14 |
| Funding moy. ~30j | 6.719e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.154 | crowd |
| BTC 1h/4h/24h | -0.16 / -0.2 / -1.14 % | B7 |
| Dominance BTC | 59.12% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat CALME (score 86/100).
- Funding maintenant 4.4e-05. Moyenne ~30j 6.719e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.154.
- BTC 24h -1.14% · 1h -0.16% · 4h -0.2%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 2951706$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.857 · OI 107047.553 (pas de dark pool free temps réel).
- Top traders L/S 1.262.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.68 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.12%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 122.65 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.525 · murC 90000 (+13.9%) · murP 70000 (-11.4%).
- Volumes cachés proxy : taker buy 0.473 · vol perp/spot 12.31×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_1H30_LIVE_COLOR.log · SKIP=921 · heat=2.7 · PnL sess=-0.9066 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
