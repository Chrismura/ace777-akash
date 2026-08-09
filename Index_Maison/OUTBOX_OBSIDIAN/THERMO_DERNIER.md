# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-09T22:58Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `88/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 65065.0 | prix |
| OI | 107704.028 | C13 |
| Funding | 9e-05 | C14 |
| Funding moy. ~30j | 5.386e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.108 | crowd |
| BTC 1h/4h/24h | -0.15 / -0.16 / 0.21 % | B7 |
| Dominance BTC | 56.64% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 88/100).
- Funding maintenant 9e-05. Moyenne ~30j 5.386e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.108.
- BTC 24h 0.21% · 1h -0.15% · 4h -0.16%.
- Panier alts : 40.0% en baisse (2/5).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.094 · OI 107704.028 (pas de dark pool free temps réel).
- Top traders L/S 1.204.
- Fear & Greed 31 (Fear).
- Market cap crypto ≈ 2.30 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.64%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC 84.54 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.596 · murC 70000 (+7.6%) · murP 60000 (-7.7%).
- Volumes cachés proxy : taker buy 0.518 · vol perp/spot 20.31×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
