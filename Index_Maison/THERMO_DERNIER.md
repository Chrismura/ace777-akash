# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-13T05:09Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `81/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83467.04 | prix |
| OI | 93222.621 | C13 |
| Funding | 5.2e-05 | C14 |
| Funding moy. ~30j | 3.718e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.424 | crowd |
| BTC 1h/4h/24h | 0.06 / 1.29 / -0.84 % | B7 |
| Dominance BTC | 59.3% | A3 |
| Alts ↓ 24h | 85.0% | B9 |

## Lecture
- Climat CALME (score 81/100).
- Funding maintenant 5.2e-05. Moyenne ~30j 3.718e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.424.
- BTC 24h -0.84% · 1h 0.06% · 4h 1.29%.
- Panier alts : 85.0% en baisse (17/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.26 · OI 93222.621 (pas de dark pool free temps réel).
- Top traders L/S 1.462.
- Fear & Greed 57 (Greed).
- Market cap crypto ≈ 2.82 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.3%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -98.73 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.584 · murC 95000 (+13.9%) · murP 80000 (-4.1%).
- Volumes cachés proxy : taker buy 0.504 · vol perp/spot 11.86×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
