# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-22T13:10Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `64/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81611.4 | prix |
| OI | 93520.025 | C13 |
| Funding | -3.7e-05 | C14 |
| Funding moy. ~30j | 2.999e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.855 | crowd |
| BTC 1h/4h/24h | -0.04 / -0.37 / -2.54 % | B7 |
| Dominance BTC | 59.44% | A3 |
| Alts ↓ 24h | 90.0% | B9 |

## Lecture
- Climat ATTENTION (score 64/100).
- Funding maintenant -3.7e-05. Moyenne ~30j 2.999e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.855.
- BTC 24h -2.54% · 1h -0.04% · 4h -0.37%.
- Panier alts : 90.0% en baisse (18/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 2102198$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.922 · OI 93520.025 (pas de dark pool free temps réel).
- Top traders L/S 1.998.
- Fear & Greed 68 (Greed).
- Market cap crypto ≈ 2.75 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.44%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 67.4 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.588 · murC 95000 (+16.4%) · murP 75000 (-8.1%).
- Volumes cachés proxy : taker buy 0.4 · vol perp/spot 14.37×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
