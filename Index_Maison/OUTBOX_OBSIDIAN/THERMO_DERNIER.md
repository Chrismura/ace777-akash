# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-17T12:11Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `80/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 76590.95 | prix |
| OI | 108471.619 | C13 |
| Funding | 6.5e-05 | C14 |
| Funding moy. ~30j | 6.694e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.468 | crowd |
| BTC 1h/4h/24h | 0.18 / 0.05 / 0.63 % | B7 |
| Dominance BTC | 58.3% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat CALME (score 80/100).
- Funding maintenant 6.5e-05. Moyenne ~30j 6.694e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.468.
- BTC 24h 0.63% · 1h 0.18% · 4h 0.05%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.904 · OI 108471.619 (pas de dark pool free temps réel).
- Top traders L/S 1.535.
- Fear & Greed 50 (Neutral).
- Market cap crypto ≈ 2.63 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.3%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -173.45 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.558 · murC 90000 (+17.6%) · murP 70000 (-8.6%).
- Volumes cachés proxy : taker buy 0.478 · vol perp/spot 12.51×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
