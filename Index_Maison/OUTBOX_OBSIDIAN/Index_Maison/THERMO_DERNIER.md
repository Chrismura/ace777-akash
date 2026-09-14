# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-14T23:43Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `82/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78304.44 | prix |
| OI | 103495.915 | C13 |
| Funding | 3.7e-05 | C14 |
| Funding moy. ~30j | 6.627e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.141 | crowd |
| BTC 1h/4h/24h | -0.27 / -0.82 / 2.01 % | B7 |
| Dominance BTC | 58.47% | A3 |
| Alts ↓ 24h | 70.0% | B9 |

## Lecture
- Climat CALME (score 82/100).
- Funding maintenant 3.7e-05. Moyenne ~30j 6.627e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.141.
- BTC 24h 2.01% · 1h -0.27% · 4h -0.82%.
- Panier alts : 70.0% en baisse (14/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.959 · OI 103495.915 (pas de dark pool free temps réel).
- Top traders L/S 1.188.
- Fear & Greed 57 (Greed).
- Market cap crypto ≈ 2.68 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.47%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -363.59 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.546 · murC 85000 (+8.5%) · murP 70000 (-10.6%).
- Volumes cachés proxy : taker buy 0.511 · vol perp/spot 13.06×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
