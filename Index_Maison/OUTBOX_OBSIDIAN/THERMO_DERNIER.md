# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-17T08:42Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `70/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63353.05 | prix |
| OI | 110003.006 | C13 |
| Funding | 6.5e-05 | C14 |
| Funding moy. ~30j | 5.377e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.963 | crowd |
| BTC 1h/4h/24h | -0.22 / -0.25 / 0.49 % | B7 |
| Dominance BTC | 56.21% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat CALME (score 70/100).
- Funding maintenant 6.5e-05. Moyenne ~30j 5.377e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.963.
- BTC 24h 0.49% · 1h -0.22% · 4h -0.25%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.771 · OI 110003.006 (pas de dark pool free temps réel).
- Top traders L/S 1.995.
- Fear & Greed 31 (Fear).
- Market cap crypto ≈ 2.26 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.21%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -55.86 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.554 · murC 70000 (+10.6%) · murP 60000 (-5.2%).
- Volumes cachés proxy : taker buy 0.488 · vol perp/spot 15.38×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1105 · heat=100.0 · PnL sess=180.3019 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
