# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-18T01:32Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `75/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64306.25 | prix |
| OI | 106743.341 | C13 |
| Funding | 5.3e-05 | C14 |
| Funding moy. ~30j | 5.495e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.463 | crowd |
| BTC 1h/4h/24h | -0.08 / -0.07 / 1.75 % | B7 |
| Dominance BTC | 56.52% | A3 |
| Alts ↓ 24h | 0.0% | B9 |

## Lecture
- Climat CALME (score 75/100).
- Funding maintenant 5.3e-05. Moyenne ~30j 5.495e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.463.
- BTC 24h 1.75% · 1h -0.08% · 4h -0.07%.
- Panier alts : 0.0% en baisse (0/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 615270$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.713 · OI 106743.341 (pas de dark pool free temps réel).
- Top traders L/S 1.516.
- Fear & Greed 41 (Fear).
- Market cap crypto ≈ 2.28 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.52%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC -25.73 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.562 · murC 70000 (+8.9%) · murP 60000 (-6.7%).
- Volumes cachés proxy : taker buy 0.555 · vol perp/spot 16.0×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=537 · heat=100.0 · PnL sess=181.3888 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
