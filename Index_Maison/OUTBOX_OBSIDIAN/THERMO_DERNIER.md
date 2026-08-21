# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-21T02:47Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `60/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 74501.14 | prix |
| OI | 107240.961 | C13 |
| Funding | 9.8e-05 | C14 |
| Funding moy. ~30j | 5.597e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.024 | crowd |
| BTC 1h/4h/24h | -0.74 / 2.61 / 7.47 % | B7 |
| Dominance BTC | 59.05% | A3 |
| Alts ↓ 24h | 10.0% | B9 |

## Lecture
- Climat ATTENTION (score 60/100).
- Funding maintenant 9.8e-05. Moyenne ~30j 5.597e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.024.
- BTC 24h 7.47% · 1h -0.74% · 4h 2.61%.
- Panier alts : 10.0% en baisse (2/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.241 · OI 107240.961 (pas de dark pool free temps réel).
- Top traders L/S 1.07.
- Fear & Greed 72 (Greed).
- Market cap crypto ≈ 2.53 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.05%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 82.05 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.569 · murC 78000 (+4.6%) · murP 60000 (-19.5%).
- Volumes cachés proxy : taker buy 0.516 · vol perp/spot 12.13×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=743 · heat=100.0 · PnL sess=240.4108 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
