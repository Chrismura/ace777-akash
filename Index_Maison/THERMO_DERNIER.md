# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-04T23:57Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `81/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 86448.93 | prix |
| OI | 97437.537 | C13 |
| Funding | 7.5e-05 | C14 |
| Funding moy. ~30j | 4.643e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.05 | crowd |
| BTC 1h/4h/24h | 0.05 / 1.24 / 2.06 % | B7 |
| Dominance BTC | 59.32% | A3 |
| Alts ↓ 24h | 10.0% | B9 |

## Lecture
- Climat CALME (score 81/100).
- Funding maintenant 7.5e-05. Moyenne ~30j 4.643e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.05.
- BTC 24h 2.06% · 1h 0.05% · 4h 1.24%.
- Panier alts : 10.0% en baisse (2/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.966 · OI 97437.537 (pas de dark pool free temps réel).
- Top traders L/S 1.084.
- Fear & Greed 65 (Greed).
- Market cap crypto ≈ 2.93 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.32%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC 8.34 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.517 · murC 95000 (+9.9%) · murP 80000 (-7.5%).
- Volumes cachés proxy : taker buy 0.486 · vol perp/spot 15.04×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
