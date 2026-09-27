# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-27T22:09Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `93/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84344.3 | prix |
| OI | 94576.62 | C13 |
| Funding | 3.5e-05 | C14 |
| Funding moy. ~30j | 5.593e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.17 | crowd |
| BTC 1h/4h/24h | -0.33 / -0.49 / 0.05 % | B7 |
| Dominance BTC | 58.81% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 93/100).
- Funding maintenant 3.5e-05. Moyenne ~30j 5.593e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.17.
- BTC 24h 0.05% · 1h -0.33% · 4h -0.49%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 926648$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.984 · OI 94576.62 (pas de dark pool free temps réel).
- Top traders L/S 1.249.
- Fear & Greed 70 (Greed).
- Market cap crypto ≈ 2.89 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.81%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 292.32 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.46 · murC 95000 (+12.6%) · murP 75000 (-11.1%).
- Volumes cachés proxy : taker buy 0.492 · vol perp/spot 13.83×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
