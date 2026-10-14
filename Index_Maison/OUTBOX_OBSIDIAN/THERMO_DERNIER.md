# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-14T11:58Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `89/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83435.7 | prix |
| OI | 90930.568 | C13 |
| Funding | 3.3e-05 | C14 |
| Funding moy. ~30j | 3.554e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.329 | crowd |
| BTC 1h/4h/24h | 0.01 / -0.12 / 0.16 % | B7 |
| Dominance BTC | 59.82% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat CALME (score 89/100).
- Funding maintenant 3.3e-05. Moyenne ~30j 3.554e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.329.
- BTC 24h 0.16% · 1h 0.01% · 4h -0.12%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.714 · OI 90930.568 (pas de dark pool free temps réel).
- Top traders L/S 1.401.
- Fear & Greed 62 (Greed).
- Market cap crypto ≈ 2.80 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.82%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -96.84 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.592 · murC 95000 (+13.9%) · murP 78000 (-6.5%).
- Volumes cachés proxy : taker buy 0.467 · vol perp/spot 11.96×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
