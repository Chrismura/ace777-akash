# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-18T19:58Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `63/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81165.3 | prix |
| OI | 108954.369 | C13 |
| Funding | 6.1e-05 | C14 |
| Funding moy. ~30j | 6.827e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 0.929 | crowd |
| BTC 1h/4h/24h | 0.32 / 0.58 / 6.11 % | B7 |
| Dominance BTC | 58.38% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat ATTENTION (score 63/100).
- Funding maintenant 6.1e-05. Moyenne ~30j 6.827e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 0.929.
- BTC 24h 6.11% · 1h 0.32% · 4h 0.58%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.949 · OI 108954.369 (pas de dark pool free temps réel).
- Top traders L/S 1.007.
- Fear & Greed 56 (Greed).
- Market cap crypto ≈ 2.79 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.38%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -102.0 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.56 · murC 85000 (+4.7%) · murP 70000 (-13.8%).
- Volumes cachés proxy : taker buy 0.496 · vol perp/spot 13.18×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
