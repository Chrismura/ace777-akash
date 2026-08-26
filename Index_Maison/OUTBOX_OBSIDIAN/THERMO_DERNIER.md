# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-26T05:23Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `83/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78869.9 | prix |
| OI | 106021.423 | C13 |
| Funding | 5.3e-05 | C14 |
| Funding moy. ~30j | 6.392e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.009 | crowd |
| BTC 1h/4h/24h | 0.1 / 0.11 / -2.1 % | B7 |
| Dominance BTC | None% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat CALME (score 83/100).
- Funding maintenant 5.3e-05. Moyenne ~30j 6.392e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.009.
- BTC 24h -2.1% · 1h 0.1% · 4h 0.11%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.754 · OI 106021.423 (pas de dark pool free temps réel).
- Top traders L/S 1.051.
- Fear & Greed 65 (Greed).
- Liquidations 24h proxy ≈ 0.03 B$.
- ETF net inflow : BTC 298.76 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.625 · murC 82000 (+3.9%) · murP 70000 (-11.3%).
- Volumes cachés proxy : taker buy 0.542 · vol perp/spot 12.92×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
