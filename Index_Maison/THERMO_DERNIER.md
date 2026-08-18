# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-18T23:36Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `88/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64725.1 | prix |
| OI | 106309.945 | C13 |
| Funding | 1.6e-05 | C14 |
| Funding moy. ~30j | 5.457e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.392 | crowd |
| BTC 1h/4h/24h | 0.18 / 0.16 / 0.38 % | B7 |
| Dominance BTC | 56.64% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 88/100).
- Funding maintenant 1.6e-05. Moyenne ~30j 5.457e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.392.
- BTC 24h 0.38% · 1h 0.18% · 4h 0.16%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 1485790$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.394 · OI 106309.945 (pas de dark pool free temps réel).
- Top traders L/S 1.496.
- Fear & Greed 41 (Fear).
- Market cap crypto ≈ 2.29 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.64%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -87.04 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.562 · murC 70000 (+8.2%) · murP 60000 (-7.3%).
- Volumes cachés proxy : taker buy 0.502 · vol perp/spot 13.58×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1186 · heat=100.0 · PnL sess=268.415 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
