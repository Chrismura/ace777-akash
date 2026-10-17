# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-17T21:22Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `79/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81554.33 | prix |
| OI | 93803.497 | C13 |
| Funding | 4.6e-05 | C14 |
| Funding moy. ~30j | 3.327e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.709 | crowd |
| BTC 1h/4h/24h | -0.08 / 0.26 / -0.24 % | B7 |
| Dominance BTC | 59.39% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 79/100).
- Funding maintenant 4.6e-05. Moyenne ~30j 3.327e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.709.
- BTC 24h -0.24% · 1h -0.08% · 4h 0.26%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 535915$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.57 · OI 93803.497 (pas de dark pool free temps réel).
- Top traders L/S 1.827.
- Fear & Greed 55 (Greed).
- Market cap crypto ≈ 2.76 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.39%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -46.29 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.583 · murC 95000 (+16.6%) · murP 75000 (-8.0%).
- Volumes cachés proxy : taker buy 0.531 · vol perp/spot 17.01×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
