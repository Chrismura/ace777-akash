# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-09T22:11Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `87/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77915.8 | prix |
| OI | 105183.845 | C13 |
| Funding | 4.5e-05 | C14 |
| Funding moy. ~30j | 6.74e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.199 | crowd |
| BTC 1h/4h/24h | -0.24 / -0.59 / -0.72 % | B7 |
| Dominance BTC | 58.57% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat CALME (score 87/100).
- Funding maintenant 4.5e-05. Moyenne ~30j 6.74e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.199.
- BTC 24h -0.72% · 1h -0.24% · 4h -0.59%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 5447761$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.919 · OI 105183.845 (pas de dark pool free temps réel).
- Top traders L/S 1.255.
- Fear & Greed 66 (Greed).
- Market cap crypto ≈ 2.66 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.57%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 147.45 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.534 · murC 81000 (+4.0%) · murP 70000 (-10.2%).
- Volumes cachés proxy : taker buy 0.484 · vol perp/spot 16.01×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
