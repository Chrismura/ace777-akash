# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-13T19:12Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `72/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63437.52 | prix |
| OI | 110163.499 | C13 |
| Funding | 8.4e-05 | C14 |
| Funding moy. ~30j | 5.524e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.885 | crowd |
| BTC 1h/4h/24h | 0.23 / 0.07 / 0.05 % | B7 |
| Dominance BTC | 56.18% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat CALME (score 72/100).
- Funding maintenant 8.4e-05. Moyenne ~30j 5.524e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.885.
- BTC 24h 0.05% · 1h 0.23% · 4h 0.07%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 624994$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.188 · OI 110163.499 (pas de dark pool free temps réel).
- Top traders L/S 1.941.
- Fear & Greed 29 (Fear).
- Market cap crypto ≈ 2.26 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.18%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC 14.67 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.552 · murC 70000 (+10.4%) · murP 60000 (-5.3%).
- Volumes cachés proxy : taker buy 0.544 · vol perp/spot 13.6×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1052 · heat=100.0 · PnL sess=115.8262 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
