# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-28T17:31Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `68/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80565.1 | prix |
| OI | 96976.842 | C13 |
| Funding | 9.9e-05 | C14 |
| Funding moy. ~30j | 4.02e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.014 | crowd |
| BTC 1h/4h/24h | -0.03 / -0.18 / -0.17 % | B7 |
| Dominance BTC | 59.47% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat ATTENTION (score 68/100).
- Funding maintenant 9.9e-05. Moyenne ~30j 4.02e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.014.
- BTC 24h -0.17% · 1h -0.03% · 4h -0.18%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.037 · OI 96976.842 (pas de dark pool free temps réel).
- Top traders L/S 2.141.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.72 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.47%).
- Liquidations 24h proxy ≈ 2.31 M$.
- ETF net inflow : BTC 131.72 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.583 · murC 95000 (+18.0%) · murP 75000 (-6.8%).
- Volumes cachés proxy : taker buy 0.492 · vol perp/spot 12.9×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
