# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-16T07:22Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `75/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63035.24 | prix |
| OI | 111334.543 | C13 |
| Funding | 1.3e-05 | C14 |
| Funding moy. ~30j | 5.375e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 2.058 | crowd |
| BTC 1h/4h/24h | -0.0 / -0.1 / -0.04 % | B7 |
| Dominance BTC | 56.17% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat CALME (score 75/100).
- Funding maintenant 1.3e-05. Moyenne ~30j 5.375e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 2.058.
- BTC 24h -0.04% · 1h -0.0% · 4h -0.1%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 1142261$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.935 · OI 111334.543 (pas de dark pool free temps réel).
- Top traders L/S 2.125.
- Fear & Greed 34 (Fear).
- Market cap crypto ≈ 2.25 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.17%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -37.87 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.554 · murC 70000 (+11.1%) · murP 60000 (-4.8%).
- Volumes cachés proxy : taker buy 0.483 · vol perp/spot 14.37×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1210 · heat=100.0 · PnL sess=183.2742 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
