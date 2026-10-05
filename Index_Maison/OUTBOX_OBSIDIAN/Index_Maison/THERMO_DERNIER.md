# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-05T13:33Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `94/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 85836.1 | prix |
| OI | 96777.198 | C13 |
| Funding | 1.9e-05 | C14 |
| Funding moy. ~30j | 4.763e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 0.996 | crowd |
| BTC 1h/4h/24h | -0.02 / -0.12 / 0.68 % | B7 |
| Dominance BTC | 59.21% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat CALME (score 94/100).
- Funding maintenant 1.9e-05. Moyenne ~30j 4.763e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 0.996.
- BTC 24h 0.68% · 1h -0.02% · 4h -0.12%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.777 · OI 96777.198 (pas de dark pool free temps réel).
- Top traders L/S 1.088.
- Fear & Greed 70 (Greed).
- Market cap crypto ≈ 2.92 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.21%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC 8.28 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.519 · murC 95000 (+10.7%) · murP 80000 (-6.8%).
- Volumes cachés proxy : taker buy 0.486 · vol perp/spot 12.06×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
