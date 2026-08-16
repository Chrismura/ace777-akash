# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-16T20:10Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `70/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63100.19 | prix |
| OI | 111426.464 | C13 |
| Funding | 5.3e-05 | C14 |
| Funding moy. ~30j | 5.367e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 2.141 | crowd |
| BTC 1h/4h/24h | 0.03 / -0.21 / 0.06 % | B7 |
| Dominance BTC | 56.14% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 70/100).
- Funding maintenant 5.3e-05. Moyenne ~30j 5.367e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 2.141.
- BTC 24h 0.06% · 1h 0.03% · 4h -0.21%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1384535$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.383 · OI 111426.464 (pas de dark pool free temps réel).
- Top traders L/S 2.203.
- Fear & Greed 34 (Fear).
- Market cap crypto ≈ 2.25 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.14%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -37.91 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.557 · murC 70000 (+11.0%) · murP 60000 (-4.9%).
- Volumes cachés proxy : taker buy 0.488 · vol perp/spot 15.48×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1311 · heat=100.0 · PnL sess=181.5234 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
