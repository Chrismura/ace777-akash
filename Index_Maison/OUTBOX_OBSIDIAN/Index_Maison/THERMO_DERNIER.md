# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-18T08:26Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `75/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77990.0 | prix |
| OI | 108317.256 | C13 |
| Funding | 7.5e-05 | C14 |
| Funding moy. ~30j | 6.862e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.344 | crowd |
| BTC 1h/4h/24h | 0.28 / 0.57 / 1.94 % | B7 |
| Dominance BTC | 58.11% | A3 |
| Alts ↓ 24h | 10.0% | B9 |

## Lecture
- Climat CALME (score 75/100).
- Funding maintenant 7.5e-05. Moyenne ~30j 6.862e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.344.
- BTC 24h 1.94% · 1h 0.28% · 4h 0.57%.
- Panier alts : 10.0% en baisse (2/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.242 · OI 108317.256 (pas de dark pool free temps réel).
- Top traders L/S 1.407.
- Fear & Greed 56 (Greed).
- Market cap crypto ≈ 2.68 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.11%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -107.13 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.552 · murC 90000 (+15.4%) · murP 70000 (-10.2%).
- Volumes cachés proxy : taker buy 0.514 · vol perp/spot 12.31×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
