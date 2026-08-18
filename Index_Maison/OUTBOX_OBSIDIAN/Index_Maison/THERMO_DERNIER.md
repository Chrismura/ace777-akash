# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-18T00:29Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `70/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64442.67 | prix |
| OI | 106433.21 | C13 |
| Funding | 5.1e-05 | C14 |
| Funding moy. ~30j | 5.495e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.484 | crowd |
| BTC 1h/4h/24h | -0.1 / 0.12 / 2.59 % | B7 |
| Dominance BTC | 56.55% | A3 |
| Alts ↓ 24h | 0.0% | B9 |

## Lecture
- Climat CALME (score 70/100).
- Funding maintenant 5.1e-05. Moyenne ~30j 5.495e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.484.
- BTC 24h 2.59% · 1h -0.1% · 4h 0.12%.
- Panier alts : 0.0% en baisse (0/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.484 · OI 106433.21 (pas de dark pool free temps réel).
- Top traders L/S 1.538.
- Fear & Greed 41 (Fear).
- Market cap crypto ≈ 2.29 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.55%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC -25.79 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.561 · murC 70000 (+8.7%) · murP 60000 (-6.9%).
- Volumes cachés proxy : taker buy 0.555 · vol perp/spot 15.49×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=544 · heat=100.0 · PnL sess=178.1494 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
