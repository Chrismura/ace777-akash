# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-13T08:35Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `79/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63748.8 | prix |
| OI | 110385.421 | C13 |
| Funding | 5.6e-05 | C14 |
| Funding moy. ~30j | 5.499e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.698 | crowd |
| BTC 1h/4h/24h | -0.12 / 0.13 / -0.03 % | B7 |
| Dominance BTC | 56.29% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat CALME (score 79/100).
- Funding maintenant 5.6e-05. Moyenne ~30j 5.499e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.698.
- BTC 24h -0.03% · 1h -0.12% · 4h 0.13%.
- Panier alts : 80.0% en baisse (4/5).
- Whales proxy : 1 gros print(s) ≥500k$ (max 908402$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.66 · OI 110385.421 (pas de dark pool free temps réel).
- Top traders L/S 1.732.
- Fear & Greed 29 (Fear).
- Market cap crypto ≈ 2.27 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.29%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC 14.74 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.551 · murC 70000 (+9.8%) · murP 60000 (-5.8%).
- Volumes cachés proxy : taker buy 0.494 · vol perp/spot 19.61×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1215 · heat=100.0 · PnL sess=124.2031 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
