# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-20T10:55Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `83/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80316.8 | prix |
| OI | 109010.822 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 6.902e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 0.944 | crowd |
| BTC 1h/4h/24h | -0.17 / 0.02 / -1.19 % | B7 |
| Dominance BTC | 58.94% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 83/100).
- Funding maintenant 0.0001. Moyenne ~30j 6.902e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 0.944.
- BTC 24h -1.19% · 1h -0.17% · 4h 0.02%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.431 · OI 109010.822 (pas de dark pool free temps réel).
- Top traders L/S 1.093.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.73 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.94%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -117.9 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.561 · murC 85000 (+5.9%) · murP 70000 (-12.8%).
- Volumes cachés proxy : taker buy 0.532 · vol perp/spot 14.5×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
