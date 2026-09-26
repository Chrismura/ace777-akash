# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-26T23:31Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `88/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84367.31 | prix |
| OI | 94250.413 | C13 |
| Funding | 4.1e-05 | C14 |
| Funding moy. ~30j | 5.763e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.289 | crowd |
| BTC 1h/4h/24h | 0.13 / 0.45 / 0.38 % | B7 |
| Dominance BTC | 58.29% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat CALME (score 88/100).
- Funding maintenant 4.1e-05. Moyenne ~30j 5.763e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.289.
- BTC 24h 0.38% · 1h 0.13% · 4h 0.45%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.235 · OI 94250.413 (pas de dark pool free temps réel).
- Top traders L/S 1.39.
- Fear & Greed 74 (Greed).
- Market cap crypto ≈ 2.90 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.29%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 292.4 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.461 · murC 95000 (+12.6%) · murP 78000 (-7.5%).
- Volumes cachés proxy : taker buy 0.544 · vol perp/spot 8.49×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
