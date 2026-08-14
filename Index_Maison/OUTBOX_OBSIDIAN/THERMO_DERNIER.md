# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-14T15:29Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `67/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 62803.6 | prix |
| OI | 114925.886 | C13 |
| Funding | 5e-06 | C14 |
| Funding moy. ~30j | 5.464e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 2.182 | crowd |
| BTC 1h/4h/24h | 0.37 / -0.04 / -1.27 % | B7 |
| Dominance BTC | None% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat ATTENTION (score 67/100).
- Funding maintenant 5e-06. Moyenne ~30j 5.464e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 2.182.
- BTC 24h -1.27% · 1h 0.37% · 4h -0.04%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.721 · OI 114925.886 (pas de dark pool free temps réel).
- Top traders L/S 2.276.
- Fear & Greed 29 (Fear).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC -199.53 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.531 · murC 70000 (+11.5%) · murP 60000 (-4.5%).
- Volumes cachés proxy : taker buy 0.544 · vol perp/spot 11.06×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1096 · heat=100.0 · PnL sess=126.3719 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
