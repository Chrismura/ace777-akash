# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-30T09:53Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `48/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77625.7 | prix |
| OI | 95509.126 | C13 |
| Funding | 6e-05 | C14 |
| Funding moy. ~30j | 4.13e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 2.294 | crowd |
| BTC 1h/4h/24h | -0.46 / -1.14 / -3.19 % | B7 |
| Dominance BTC | 59.28% | A3 |
| Alts ↓ 24h | 85.0% | B9 |

## Lecture
- Climat ATTENTION (score 48/100).
- Funding maintenant 6e-05. Moyenne ~30j 4.13e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 2.294.
- BTC 24h -3.19% · 1h -0.46% · 4h -1.14%.
- Panier alts : 85.0% en baisse (17/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.797 · OI 95509.126 (pas de dark pool free temps réel).
- Top traders L/S 2.428.
- Fear & Greed 30 (Fear).
- Market cap crypto ≈ 2.63 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.28%).
- Liquidations 24h proxy ≈ 2.10 M$.
- ETF net inflow : BTC 21.17 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.706 · murC 90000 (+16.1%) · murP 60000 (-22.6%).
- Volumes cachés proxy : taker buy 0.526 · vol perp/spot 10.55×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
