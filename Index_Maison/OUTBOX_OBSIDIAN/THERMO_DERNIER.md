# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-16T08:56Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `73/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 75671.06 | prix |
| OI | 107342.883 | C13 |
| Funding | 7e-06 | C14 |
| Funding moy. ~30j | 6.71e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.817 | crowd |
| BTC 1h/4h/24h | -0.07 / -0.21 / -1.6 % | B7 |
| Dominance BTC | 58.49% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 73/100).
- Funding maintenant 7e-06. Moyenne ~30j 6.71e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.817.
- BTC 24h -1.6% · 1h -0.07% · 4h -0.21%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.756 · OI 107342.883 (pas de dark pool free temps réel).
- Top traders L/S 1.896.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.59 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.49%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -55.58 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.544 · murC 85000 (+12.4%) · murP 70000 (-7.5%).
- Volumes cachés proxy : taker buy 0.508 · vol perp/spot 13.2×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
