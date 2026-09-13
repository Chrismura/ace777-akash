# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-13T22:38Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `77/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 76829.99 | prix |
| OI | 104883.791 | C13 |
| Funding | 6.5e-05 | C14 |
| Funding moy. ~30j | 6.618e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.638 | crowd |
| BTC 1h/4h/24h | -0.6 / -0.65 / -0.45 % | B7 |
| Dominance BTC | 58.9% | A3 |
| Alts ↓ 24h | 70.0% | B9 |

## Lecture
- Climat CALME (score 77/100).
- Funding maintenant 6.5e-05. Moyenne ~30j 6.618e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.638.
- BTC 24h -0.45% · 1h -0.6% · 4h -0.65%.
- Panier alts : 70.0% en baisse (14/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 781852$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.147 · OI 104883.791 (pas de dark pool free temps réel).
- Top traders L/S 1.724.
- Fear & Greed 61 (Greed).
- Market cap crypto ≈ 2.61 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.9%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 6.06 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.556 · murC 90000 (+17.2%) · murP 70000 (-8.9%).
- Volumes cachés proxy : taker buy 0.513 · vol perp/spot 15.48×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
