# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-11T09:16Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `77/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77257.3 | prix |
| OI | 106635.723 | C13 |
| Funding | 4.4e-05 | C14 |
| Funding moy. ~30j | 6.702e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.604 | crowd |
| BTC 1h/4h/24h | -0.09 / 0.05 / -1.1 % | B7 |
| Dominance BTC | 58.48% | A3 |
| Alts ↓ 24h | 65.0% | B9 |

## Lecture
- Climat CALME (score 77/100).
- Funding maintenant 4.4e-05. Moyenne ~30j 6.702e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.604.
- BTC 24h -1.1% · 1h -0.09% · 4h 0.05%.
- Panier alts : 65.0% en baisse (13/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 924604$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.108 · OI 106635.723 (pas de dark pool free temps réel).
- Top traders L/S 1.617.
- Fear & Greed 56 (Greed).
- Market cap crypto ≈ 2.65 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.48%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 75.36 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.532 · murC 90000 (+16.5%) · murP 70000 (-9.4%).
- Volumes cachés proxy : taker buy 0.447 · vol perp/spot 14.43×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
