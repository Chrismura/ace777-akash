# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-15T02:32Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `63/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80644.3 | prix |
| OI | 92468.741 | C13 |
| Funding | -2.3e-05 | C14 |
| Funding moy. ~30j | 3.402e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.791 | crowd |
| BTC 1h/4h/24h | -1.21 / -1.24 / -3.09 % | B7 |
| Dominance BTC | 59.42% | A3 |
| Alts ↓ 24h | 85.0% | B9 |

## Lecture
- Climat ATTENTION (score 63/100).
- Funding maintenant -2.3e-05. Moyenne ~30j 3.402e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.791.
- BTC 24h -3.09% · 1h -1.21% · 4h -1.24%.
- Panier alts : 85.0% en baisse (17/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.89 · OI 92468.741 (pas de dark pool free temps réel).
- Top traders L/S 1.885.
- Fear & Greed 53 (Neutral).
- Market cap crypto ≈ 2.71 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.42%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -22.57 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.616 · murC 95000 (+17.9%) · murP 78000 (-3.2%).
- Volumes cachés proxy : taker buy 0.507 · vol perp/spot 13.58×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
