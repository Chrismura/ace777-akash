# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-11-02T03:14Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `59/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78492.12 | prix |
| OI | 95231.227 | C13 |
| Funding | 9.7e-05 | C14 |
| Funding moy. ~30j | 4.523e-05 (n=90) | Cortana |
| Funding mois préc. | 4.378e-05 (n=93) | Cortana |
| L/S 1h | 2.224 | crowd |
| BTC 1h/4h/24h | 0.08 / 0.23 / 0.95 % | B7 |
| Dominance BTC | 60.02% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat ATTENTION (score 59/100).
- Funding maintenant 9.7e-05. Moyenne ~30j 4.523e-05 (90 pts). Mois précédent 4.378e-05 (93 pts).
- Long/Short 2.224.
- BTC 24h 0.95% · 1h 0.08% · 4h 0.23%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.371 · OI 95231.227 (pas de dark pool free temps réel).
- Top traders L/S 2.349.
- Fear & Greed 37 (Fear).
- Market cap crypto ≈ 2.62 T$.
- Alt season proxy : Bitcoin season (BTC.D 60.02%).
- Liquidations 24h proxy ≈ 2.15 M$.
- ETF net inflow : BTC 63.79 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.665 · murC 90000 (+14.8%) · murP 74000 (-5.6%).
- Volumes cachés proxy : taker buy 0.528 · vol perp/spot 7.97×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
