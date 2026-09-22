# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-22T00:05Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `61/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 86443.1 | prix |
| OI | 108998.081 | C13 |
| Funding | 7.5e-05 | C14 |
| Funding moy. ~30j | 6.734e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 0.892 | crowd |
| BTC 1h/4h/24h | -0.16 / -0.6 / 6.26 % | B7 |
| Dominance BTC | 58.91% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat ATTENTION (score 61/100).
- Funding maintenant 7.5e-05. Moyenne ~30j 6.734e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 0.892.
- BTC 24h 6.26% · 1h -0.16% · 4h -0.6%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.09 · OI 108998.081 (pas de dark pool free temps réel).
- Top traders L/S 0.963.
- Fear & Greed 78 (Extreme Greed).
- Market cap crypto ≈ 2.94 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.91%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -22.13 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.511 · murC 95000 (+9.9%) · murP 70000 (-19.0%).
- Volumes cachés proxy : taker buy 0.54 · vol perp/spot 11.83×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
