# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-11T19:18Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `88/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77151.78 | prix |
| OI | 103546.985 | C13 |
| Funding | 9e-06 | C14 |
| Funding moy. ~30j | 6.669e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.489 | crowd |
| BTC 1h/4h/24h | 0.16 / -0.69 / 0.05 % | B7 |
| Dominance BTC | 58.2% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat CALME (score 88/100).
- Funding maintenant 9e-06. Moyenne ~30j 6.669e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.489.
- BTC 24h 0.05% · 1h 0.16% · 4h -0.69%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.767 · OI 103546.985 (pas de dark pool free temps réel).
- Top traders L/S 1.534.
- Fear & Greed 56 (Greed).
- Market cap crypto ≈ 2.66 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.2%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC 75.25 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.537 · murC 90000 (+16.6%) · murP 70000 (-9.3%).
- Volumes cachés proxy : taker buy 0.495 · vol perp/spot 14.33×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
