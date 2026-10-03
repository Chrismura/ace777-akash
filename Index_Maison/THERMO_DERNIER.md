# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-03T09:46Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `84/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84547.2 | prix |
| OI | 97693.509 | C13 |
| Funding | -6e-06 | C14 |
| Funding moy. ~30j | 4.843e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.211 | crowd |
| BTC 1h/4h/24h | -0.03 / -0.07 / -2.05 % | B7 |
| Dominance BTC | 59.17% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 84/100).
- Funding maintenant -6e-06. Moyenne ~30j 4.843e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.211.
- BTC 24h -2.05% · 1h -0.03% · 4h -0.07%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.141 · OI 97693.509 (pas de dark pool free temps réel).
- Top traders L/S 1.246.
- Fear & Greed 67 (Greed).
- Market cap crypto ≈ 2.87 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.17%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 8.15 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.508 · murC 95000 (+12.3%) · murP 75000 (-11.3%).
- Volumes cachés proxy : taker buy 0.477 · vol perp/spot 11.48×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
