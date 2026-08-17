# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-17T19:15Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `74/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64325.76 | prix |
| OI | 106465.511 | C13 |
| Funding | 3.1e-05 | C14 |
| Funding moy. ~30j | 5.442e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.578 | crowd |
| BTC 1h/4h/24h | -0.1 / 0.26 / 1.86 % | B7 |
| Dominance BTC | 56.53% | A3 |
| Alts ↓ 24h | 0.0% | B9 |

## Lecture
- Climat CALME (score 74/100).
- Funding maintenant 3.1e-05. Moyenne ~30j 5.442e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.578.
- BTC 24h 1.86% · 1h -0.1% · 4h 0.26%.
- Panier alts : 0.0% en baisse (0/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 814082$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.337 · OI 106465.511 (pas de dark pool free temps réel).
- Top traders L/S 1.621.
- Fear & Greed 31 (Fear).
- Market cap crypto ≈ 2.28 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.53%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC -56.72 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.558 · murC 70000 (+8.8%) · murP 60000 (-6.7%).
- Volumes cachés proxy : taker buy 0.555 · vol perp/spot 17.08×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=919 · heat=100.0 · PnL sess=174.1862 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
