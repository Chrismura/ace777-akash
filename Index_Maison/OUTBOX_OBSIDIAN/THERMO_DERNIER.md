# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-23T16:45Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `65/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81741.8 | prix |
| OI | 92150.355 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 3.202e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.078 | crowd |
| BTC 1h/4h/24h | 0.13 / 0.06 / 0.43 % | B7 |
| Dominance BTC | 59.44% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat ATTENTION (score 65/100).
- Funding maintenant 0.0001. Moyenne ~30j 3.202e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.078.
- BTC 24h 0.43% · 1h 0.13% · 4h 0.06%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 2136046$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.319 · OI 92150.355 (pas de dark pool free temps réel).
- Top traders L/S 2.13.
- Fear & Greed 50 (Neutral).
- Market cap crypto ≈ 2.76 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.44%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 65.19 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.576 · murC 95000 (+16.2%) · murP 75000 (-8.3%).
- Volumes cachés proxy : taker buy 0.505 · vol perp/spot 15.98×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
