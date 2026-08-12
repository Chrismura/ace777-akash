# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-12T09:30Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `75/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63974.3 | prix |
| OI | 108453.286 | C13 |
| Funding | 8.3e-05 | C14 |
| Funding moy. ~30j | 5.514e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.724 | crowd |
| BTC 1h/4h/24h | 0.32 / 0.26 / -0.3 % | B7 |
| Dominance BTC | 56.33% | A3 |
| Alts ↓ 24h | 0.0% | B9 |

## Lecture
- Climat CALME (score 75/100).
- Funding maintenant 8.3e-05. Moyenne ~30j 5.514e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.724.
- BTC 24h -0.3% · 1h 0.32% · 4h 0.26%.
- Panier alts : 0.0% en baisse (0/5).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.115 · OI 108453.286 (pas de dark pool free temps réel).
- Top traders L/S 1.807.
- Fear & Greed 27 (Fear).
- Market cap crypto ≈ 2.28 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.33%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC 37.5 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.573 · murC 70000 (+9.5%) · murP 60000 (-6.2%).
- Volumes cachés proxy : taker buy 0.498 · vol perp/spot 11.56×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
