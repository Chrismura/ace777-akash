# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-06T17:35Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `98/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 85573.56 | prix |
| OI | 95889.564 | C13 |
| Funding | -0.0 | C14 |
| Funding moy. ~30j | 4.607e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 0.981 | crowd |
| BTC 1h/4h/24h | 0.04 / -0.82 / 0.34 % | B7 |
| Dominance BTC | 58.74% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 98/100).
- Funding maintenant -0.0. Moyenne ~30j 4.607e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 0.981.
- BTC 24h 0.34% · 1h 0.04% · 4h -0.82%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 817629$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.946 · OI 95889.564 (pas de dark pool free temps réel).
- Top traders L/S 1.051.
- Fear & Greed 73 (Greed).
- Market cap crypto ≈ 2.92 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.74%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 23.94 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.519 · murC 95000 (+11.0%) · murP 80000 (-6.6%).
- Volumes cachés proxy : taker buy 0.455 · vol perp/spot 13.06×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
