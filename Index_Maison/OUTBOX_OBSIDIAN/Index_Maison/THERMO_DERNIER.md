# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-20T12:55Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `85/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80433.0 | prix |
| OI | 108824.218 | C13 |
| Funding | 8.9e-05 | C14 |
| Funding moy. ~30j | 6.902e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 0.958 | crowd |
| BTC 1h/4h/24h | -0.02 / 0.25 / -1.07 % | B7 |
| Dominance BTC | 58.91% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 85/100).
- Funding maintenant 8.9e-05. Moyenne ~30j 6.902e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 0.958.
- BTC 24h -1.07% · 1h -0.02% · 4h 0.25%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 957716$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.819 · OI 108824.218 (pas de dark pool free temps réel).
- Top traders L/S 1.108.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.74 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.91%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -118.07 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.561 · murC 85000 (+5.7%) · murP 70000 (-13.0%).
- Volumes cachés proxy : taker buy 0.532 · vol perp/spot 14.87×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
