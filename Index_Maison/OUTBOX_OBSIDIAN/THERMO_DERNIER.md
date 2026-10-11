# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-11T11:51Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `88/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83077.0 | prix |
| OI | 93163.355 | C13 |
| Funding | -8e-06 | C14 |
| Funding moy. ~30j | 3.846e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.442 | crowd |
| BTC 1h/4h/24h | 0.14 / 0.11 / 0.27 % | B7 |
| Dominance BTC | 59.64% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 88/100).
- Funding maintenant -8e-06. Moyenne ~30j 3.846e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.442.
- BTC 24h 0.27% · 1h 0.14% · 4h 0.11%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 777621$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.796 · OI 93163.355 (pas de dark pool free temps réel).
- Top traders L/S 1.525.
- Fear & Greed 61 (Greed).
- Market cap crypto ≈ 2.79 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.64%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -31.94 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.564 · murC 95000 (+14.4%) · murP 80000 (-3.7%).
- Volumes cachés proxy : taker buy 0.511 · vol perp/spot 9.96×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
