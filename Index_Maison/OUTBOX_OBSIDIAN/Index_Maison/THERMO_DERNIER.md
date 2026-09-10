# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-10T17:12Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `71/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77178.8 | prix |
| OI | 107706.998 | C13 |
| Funding | 5.4e-05 | C14 |
| Funding moy. ~30j | 6.807e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.575 | crowd |
| BTC 1h/4h/24h | 0.02 / 0.07 / -2.03 % | B7 |
| Dominance BTC | 58.54% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat CALME (score 71/100).
- Funding maintenant 5.4e-05. Moyenne ~30j 6.807e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.575.
- BTC 24h -2.03% · 1h 0.02% · 4h 0.07%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 1150282$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.977 · OI 107706.998 (pas de dark pool free temps réel).
- Top traders L/S 1.662.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.64 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.54%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -137.06 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.538 · murC 90000 (+16.6%) · murP 70000 (-9.3%).
- Volumes cachés proxy : taker buy 0.447 · vol perp/spot 14.64×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
