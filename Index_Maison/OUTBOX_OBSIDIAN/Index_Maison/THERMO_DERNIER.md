# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-28T08:24Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `62/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81195.22 | prix |
| OI | 96478.976 | C13 |
| Funding | 8.9e-05 | C14 |
| Funding moy. ~30j | 4.003e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.949 | crowd |
| BTC 1h/4h/24h | 0.18 / 0.28 / 1.66 % | B7 |
| Dominance BTC | 59.43% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat ATTENTION (score 62/100).
- Funding maintenant 8.9e-05. Moyenne ~30j 4.003e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.949.
- BTC 24h 1.66% · 1h 0.18% · 4h 0.28%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 803642$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.496 · OI 96478.976 (pas de dark pool free temps réel).
- Top traders L/S 2.068.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.74 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.43%).
- Liquidations 24h proxy ≈ 1.60 M$.
- ETF net inflow : BTC -22.68 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.587 · murC 95000 (+17.1%) · murP 75000 (-7.5%).
- Volumes cachés proxy : taker buy 0.513 · vol perp/spot 14.68×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
