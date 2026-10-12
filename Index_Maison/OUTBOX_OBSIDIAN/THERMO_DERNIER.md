# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-12T13:28Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `81/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82506.7 | prix |
| OI | 94104.57 | C13 |
| Funding | 7.4e-05 | C14 |
| Funding moy. ~30j | 3.732e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.38 | crowd |
| BTC 1h/4h/24h | -0.23 / -1.17 / -0.7 % | B7 |
| Dominance BTC | 58.93% | A3 |
| Alts ↓ 24h | 50.0% | B9 |

## Lecture
- Climat CALME (score 81/100).
- Funding maintenant 7.4e-05. Moyenne ~30j 3.732e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.38.
- BTC 24h -0.7% · 1h -0.23% · 4h -1.17%.
- Panier alts : 50.0% en baisse (10/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.636 · OI 94104.57 (pas de dark pool free temps réel).
- Top traders L/S 1.492.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.81 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.93%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -219.17 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.57 · murC 95000 (+15.2%) · murP 80000 (-3.0%).
- Volumes cachés proxy : taker buy 0.476 · vol perp/spot 12.52×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
