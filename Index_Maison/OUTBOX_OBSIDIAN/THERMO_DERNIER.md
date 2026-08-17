# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-17T00:21Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `68/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 62838.96 | prix |
| OI | 111050.161 | C13 |
| Funding | 3.9e-05 | C14 |
| Funding moy. ~30j | 5.375e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 2.222 | crowd |
| BTC 1h/4h/24h | -0.08 / -0.34 / -0.3 % | B7 |
| Dominance BTC | 56.15% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat ATTENTION (score 68/100).
- Funding maintenant 3.9e-05. Moyenne ~30j 5.375e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 2.222.
- BTC 24h -0.3% · 1h -0.08% · 4h -0.34%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 550620$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.08 · OI 111050.161 (pas de dark pool free temps réel).
- Top traders L/S 2.289.
- Fear & Greed 31 (Fear).
- Market cap crypto ≈ 2.25 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.15%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -55.41 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.558 · murC 70000 (+11.5%) · murP 60000 (-4.4%).
- Volumes cachés proxy : taker buy 0.488 · vol perp/spot 16.82×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1181 · heat=100.0 · PnL sess=182.6451 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
