# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-30T03:52Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `57/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78081.9 | prix |
| OI | 97324.672 | C13 |
| Funding | 1.2e-05 | C14 |
| Funding moy. ~30j | 4.08e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 2.698 | crowd |
| BTC 1h/4h/24h | 0.89 / 0.14 / -2.16 % | B7 |
| Dominance BTC | 59.29% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat ATTENTION (score 57/100).
- Funding maintenant 1.2e-05. Moyenne ~30j 4.08e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 2.698.
- BTC 24h -2.16% · 1h 0.89% · 4h 0.14%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 624882$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.089 · OI 97324.672 (pas de dark pool free temps réel).
- Top traders L/S 2.867.
- Fear & Greed 30 (Fear).
- Market cap crypto ≈ 2.64 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.29%).
- Liquidations 24h proxy ≈ 4.87 M$.
- ETF net inflow : BTC 21.29 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.621 · murC 95000 (+21.9%) · murP 70000 (-10.1%).
- Volumes cachés proxy : taker buy 0.526 · vol perp/spot 12.29×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
