# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-20T20:02Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `94/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81182.5 | prix |
| OI | 107354.685 | C13 |
| Funding | 4.4e-05 | C14 |
| Funding moy. ~30j | 6.875e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 0.972 | crowd |
| BTC 1h/4h/24h | 0.04 / -0.15 / -0.2 % | B7 |
| Dominance BTC | 58.73% | A3 |
| Alts ↓ 24h | 50.0% | B9 |

## Lecture
- Climat CALME (score 94/100).
- Funding maintenant 4.4e-05. Moyenne ~30j 6.875e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 0.972.
- BTC 24h -0.2% · 1h 0.04% · 4h -0.15%.
- Panier alts : 50.0% en baisse (10/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.817 · OI 107354.685 (pas de dark pool free temps réel).
- Top traders L/S 1.12.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.78 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.73%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -119.17 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.564 · murC 85000 (+4.7%) · murP 70000 (-13.8%).
- Volumes cachés proxy : taker buy 0.478 · vol perp/spot 14.54×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
