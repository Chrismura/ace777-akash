# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-22T18:30Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `49/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81137.9 | prix |
| OI | 95481.323 | C13 |
| Funding | 5.7e-05 | C14 |
| Funding moy. ~30j | 2.982e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.013 | crowd |
| BTC 1h/4h/24h | -0.05 / -0.85 / -4.21 % | B7 |
| Dominance BTC | 59.48% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat ATTENTION (score 49/100).
- Funding maintenant 5.7e-05. Moyenne ~30j 2.982e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.013.
- BTC 24h -4.21% · 1h -0.05% · 4h -0.85%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.924 · OI 95481.323 (pas de dark pool free temps réel).
- Top traders L/S 2.176.
- Fear & Greed 68 (Greed).
- Market cap crypto ≈ 2.74 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.48%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 67.01 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.594 · murC 95000 (+17.2%) · murP 75000 (-7.5%).
- Volumes cachés proxy : taker buy 0.529 · vol perp/spot 14.66×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
