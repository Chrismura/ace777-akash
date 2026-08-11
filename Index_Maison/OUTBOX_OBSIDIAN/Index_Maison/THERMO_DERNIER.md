# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-11T22:59Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `70/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63641.7 | prix |
| OI | 109187.142 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.379e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.809 | crowd |
| BTC 1h/4h/24h | 0.0 / 0.46 / -0.53 % | B7 |
| Dominance BTC | 56.27% | A3 |
| Alts ↓ 24h | 0.0% | B9 |

## Lecture
- Climat CALME (score 70/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.379e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.809.
- BTC 24h -0.53% · 1h 0.0% · 4h 0.46%.
- Panier alts : 0.0% en baisse (0/5).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.787 · OI 109187.142 (pas de dark pool free temps réel).
- Top traders L/S 1.909.
- Fear & Greed 29 (Fear).
- Market cap crypto ≈ 2.27 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.27%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC 119.67 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.577 · murC 70000 (+10.0%) · murP 60000 (-5.7%).
- Volumes cachés proxy : taker buy 0.498 · vol perp/spot 17.34×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
