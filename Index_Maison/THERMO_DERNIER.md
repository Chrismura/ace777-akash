# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-14T20:24Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `73/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81912.9 | prix |
| OI | 92962.433 | C13 |
| Funding | -2.1e-05 | C14 |
| Funding moy. ~30j | 3.488e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.74 | crowd |
| BTC 1h/4h/24h | 0.15 / -0.07 / -1.52 % | B7 |
| Dominance BTC | 59.34% | A3 |
| Alts ↓ 24h | 85.0% | B9 |

## Lecture
- Climat CALME (score 73/100).
- Funding maintenant -2.1e-05. Moyenne ~30j 3.488e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.74.
- BTC 24h -1.52% · 1h 0.15% · 4h -0.07%.
- Panier alts : 85.0% en baisse (17/20).
- Whales proxy : 4 gros print(s) ≥500k$ (max 1366548$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.892 · OI 92962.433 (pas de dark pool free temps réel).
- Top traders L/S 1.835.
- Fear & Greed 62 (Greed).
- Market cap crypto ≈ 2.77 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.34%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 149.65 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.612 · murC 95000 (+16.0%) · murP 78000 (-4.7%).
- Volumes cachés proxy : taker buy 0.507 · vol perp/spot 13.66×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
