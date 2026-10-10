# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-10T21:48Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `85/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83052.73 | prix |
| OI | 92660.831 | C13 |
| Funding | 1e-06 | C14 |
| Funding moy. ~30j | 3.989e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.5 | crowd |
| BTC 1h/4h/24h | 0.07 / -0.02 / 0.64 % | B7 |
| Dominance BTC | 59.11% | A3 |
| Alts ↓ 24h | 15.0% | B9 |

## Lecture
- Climat CALME (score 85/100).
- Funding maintenant 1e-06. Moyenne ~30j 3.989e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.5.
- BTC 24h 0.64% · 1h 0.07% · 4h -0.02%.
- Panier alts : 15.0% en baisse (3/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.392 · OI 92660.831 (pas de dark pool free temps réel).
- Top traders L/S 1.554.
- Fear & Greed 64 (Greed).
- Market cap crypto ≈ 2.82 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.11%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -31.93 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.574 · murC 95000 (+14.4%) · murP 80000 (-3.6%).
- Volumes cachés proxy : taker buy 0.511 · vol perp/spot 10.19×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
