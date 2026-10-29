# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-29T00:44Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `73/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81157.0 | prix |
| OI | 95939.315 | C13 |
| Funding | 5.2e-05 | C14 |
| Funding moy. ~30j | 4.046e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.889 | crowd |
| BTC 1h/4h/24h | -0.19 / -0.17 / 0.54 % | B7 |
| Dominance BTC | 59.47% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat CALME (score 73/100).
- Funding maintenant 5.2e-05. Moyenne ~30j 4.046e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.889.
- BTC 24h 0.54% · 1h -0.19% · 4h -0.17%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 926408$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.941 · OI 95939.315 (pas de dark pool free temps réel).
- Top traders L/S 1.995.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.73 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.47%).
- Liquidations 24h proxy ≈ 4.18 M$.
- ETF net inflow : BTC -0.95 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.586 · murC 95000 (+17.2%) · murP 75000 (-7.5%).
- Volumes cachés proxy : taker buy 0.492 · vol perp/spot 13.68×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
