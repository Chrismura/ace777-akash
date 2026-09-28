# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-28T15:23Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `75/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82775.92 | prix |
| OI | 94934.88 | C13 |
| Funding | 6.2e-05 | C14 |
| Funding moy. ~30j | 5.364e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.342 | crowd |
| BTC 1h/4h/24h | -0.27 / -0.34 / -2.11 % | B7 |
| Dominance BTC | 58.25% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat CALME (score 75/100).
- Funding maintenant 6.2e-05. Moyenne ~30j 5.364e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.342.
- BTC 24h -2.11% · 1h -0.27% · 4h -0.34%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 1273029$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.722 · OI 94934.88 (pas de dark pool free temps réel).
- Top traders L/S 1.441.
- Fear & Greed 74 (Greed).
- Market cap crypto ≈ 2.86 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.25%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 286.89 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.489 · murC 95000 (+14.7%) · murP 78000 (-5.8%).
- Volumes cachés proxy : taker buy 0.492 · vol perp/spot 10.33×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
