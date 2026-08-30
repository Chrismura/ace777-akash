# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-30T23:04Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `91/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78287.71 | prix |
| OI | 106655.181 | C13 |
| Funding | 8.1e-05 | C14 |
| Funding moy. ~30j | 6.567e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.053 | crowd |
| BTC 1h/4h/24h | -0.13 / -0.69 / 0.1 % | B7 |
| Dominance BTC | 59.58% | A3 |
| Alts ↓ 24h | 65.0% | B9 |

## Lecture
- Climat CALME (score 91/100).
- Funding maintenant 8.1e-05. Moyenne ~30j 6.567e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.053.
- BTC 24h 0.1% · 1h -0.13% · 4h -0.69%.
- Panier alts : 65.0% en baisse (13/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.918 · OI 106655.181 (pas de dark pool free temps réel).
- Top traders L/S 1.109.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.63 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.58%).
- Liquidations 24h proxy ≈ 0.03 B$.
- ETF net inflow : BTC -293.02 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.574 · murC 82000 (+4.7%) · murP 70000 (-10.6%).
- Volumes cachés proxy : taker buy 0.469 · vol perp/spot 16.57×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
