# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-10T06:26Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `87/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 65146.8 | prix |
| OI | 106916.902 | C13 |
| Funding | 6.7e-05 | C14 |
| Funding moy. ~30j | 5.358e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.163 | crowd |
| BTC 1h/4h/24h | 0.05 / 0.11 / 0.52 % | B7 |
| Dominance BTC | 56.69% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 87/100).
- Funding maintenant 6.7e-05. Moyenne ~30j 5.358e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.163.
- BTC 24h 0.52% · 1h 0.05% · 4h 0.11%.
- Panier alts : 40.0% en baisse (2/5).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.499 · OI 106916.902 (pas de dark pool free temps réel).
- Top traders L/S 1.243.
- Fear & Greed 30 (Fear).
- Market cap crypto ≈ 2.31 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.69%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC 69.31 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.597 · murC 70000 (+7.5%) · murP 60000 (-7.9%).
- Volumes cachés proxy : taker buy 0.518 · vol perp/spot 18.46×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
