# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-07T23:57Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `88/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64884.97 | prix |
| OI | 106977.599 | C13 |
| Funding | 5.6e-05 | C14 |
| Funding moy. ~30j | 5.481e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.099 | crowd |
| BTC 1h/4h/24h | 0.04 / -0.07 / 0.92 % | B7 |
| Dominance BTC | 56.77% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat CALME (score 88/100).
- Funding maintenant 5.6e-05. Moyenne ~30j 5.481e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.099.
- BTC 24h 0.92% · 1h 0.04% · 4h -0.07%.
- Panier alts : 20.0% en baisse (1/5).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.739 · OI 106977.599 (pas de dark pool free temps réel).
- Top traders L/S 1.167.
- Fear & Greed 29 (Fear).
- Market cap crypto ≈ 2.29 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.77%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC 277.58 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.601 · murC 70000 (+7.9%) · murP 60000 (-7.5%).
- Volumes cachés proxy : taker buy 0.522 · vol perp/spot 19.24×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
