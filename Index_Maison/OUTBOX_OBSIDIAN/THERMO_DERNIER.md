# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-02T21:43Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `90/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84491.67 | prix |
| OI | 98630.563 | C13 |
| Funding | 6.7e-05 | C14 |
| Funding moy. ~30j | 4.934e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.152 | crowd |
| BTC 1h/4h/24h | 0.09 / -0.3 / 0.04 % | B7 |
| Dominance BTC | 58.83% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 90/100).
- Funding maintenant 6.7e-05. Moyenne ~30j 4.934e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.152.
- BTC 24h 0.04% · 1h 0.09% · 4h -0.3%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 943267$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.046 · OI 98630.563 (pas de dark pool free temps réel).
- Top traders L/S 1.229.
- Fear & Greed 72 (Greed).
- Market cap crypto ≈ 2.88 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.83%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 6.71 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.518 · murC 95000 (+12.4%) · murP 80000 (-5.3%).
- Volumes cachés proxy : taker buy 0.477 · vol perp/spot 11.03×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
