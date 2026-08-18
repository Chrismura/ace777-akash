# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-18T15:12Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `80/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64719.65 | prix |
| OI | 106419.962 | C13 |
| Funding | 4.4e-05 | C14 |
| Funding moy. ~30j | 5.474e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.396 | crowd |
| BTC 1h/4h/24h | 0.04 / 0.6 / 1.24 % | B7 |
| Dominance BTC | 56.65% | A3 |
| Alts ↓ 24h | 70.0% | B9 |

## Lecture
- Climat CALME (score 80/100).
- Funding maintenant 4.4e-05. Moyenne ~30j 5.474e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.396.
- BTC 24h 1.24% · 1h 0.04% · 4h 0.6%.
- Panier alts : 70.0% en baisse (14/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.195 · OI 106419.962 (pas de dark pool free temps réel).
- Top traders L/S 1.498.
- Fear & Greed 41 (Fear).
- Market cap crypto ≈ 2.29 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.65%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC -87.03 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.56 · murC 70000 (+8.2%) · murP 60000 (-7.3%).
- Volumes cachés proxy : taker buy 0.555 · vol perp/spot 14.03×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1017 · heat=100.0 · PnL sess=265.4896 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
