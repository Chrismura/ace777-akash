# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-22T15:54Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `88/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 76976.2 | prix |
| OI | 106468.13 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.919e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 0.991 | crowd |
| BTC 1h/4h/24h | -0.06 / -0.21 / -0.47 % | B7 |
| Dominance BTC | 58.94% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat CALME (score 88/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.919e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 0.991.
- BTC 24h -0.47% · 1h -0.06% · 4h -0.21%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.936 · OI 106468.13 (pas de dark pool free temps réel).
- Top traders L/S 1.113.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.62 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.94%).
- Liquidations 24h proxy ≈ 0.04 B$.
- ETF net inflow : BTC 226.05 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.614 · murC 78000 (+1.4%) · murP 60000 (-22.0%).
- Volumes cachés proxy : taker buy 0.534 · vol perp/spot 10.76×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1348 · heat=100.0 · PnL sess=318.1163 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
