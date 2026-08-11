# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-11T20:53Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `69/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63671.1 | prix |
| OI | 108811.906 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.379e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.815 | crowd |
| BTC 1h/4h/24h | 0.27 / 0.3 / -0.72 % | B7 |
| Dominance BTC | 56.32% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat ATTENTION (score 69/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.379e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.815.
- BTC 24h -0.72% · 1h 0.27% · 4h 0.3%.
- Panier alts : 40.0% en baisse (2/5).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.343 · OI 108811.906 (pas de dark pool free temps réel).
- Top traders L/S 1.921.
- Fear & Greed 29 (Fear).
- Market cap crypto ≈ 2.27 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.32%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC 119.73 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.578 · murC 70000 (+10.0%) · murP 60000 (-5.7%).
- Volumes cachés proxy : taker buy 0.498 · vol perp/spot 17.6×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
