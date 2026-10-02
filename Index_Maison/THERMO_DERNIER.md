# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-02T03:17Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `84/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 85271.7 | prix |
| OI | 98097.087 | C13 |
| Funding | 3.9e-05 | C14 |
| Funding moy. ~30j | 4.941e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.015 | crowd |
| BTC 1h/4h/24h | 0.11 / 0.5 / 2.16 % | B7 |
| Dominance BTC | 58.69% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat CALME (score 84/100).
- Funding maintenant 3.9e-05. Moyenne ~30j 4.941e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.015.
- BTC 24h 2.16% · 1h 0.11% · 4h 0.5%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 816222$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.315 · OI 98097.087 (pas de dark pool free temps réel).
- Top traders L/S 1.089.
- Fear & Greed 72 (Greed).
- Market cap crypto ≈ 2.91 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.69%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 9.38 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.555 · murC 95000 (+11.4%) · murP 80000 (-6.1%).
- Volumes cachés proxy : taker buy 0.526 · vol perp/spot 12.76×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
