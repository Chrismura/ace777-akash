# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-15T09:40Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `68/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 62981.7 | prix |
| OI | 111923.322 | C13 |
| Funding | 6.6e-05 | C14 |
| Funding moy. ~30j | 5.458e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 2.074 | crowd |
| BTC 1h/4h/24h | 0.11 / -0.12 / 0.41 % | B7 |
| Dominance BTC | 56.1% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat ATTENTION (score 68/100).
- Funding maintenant 6.6e-05. Moyenne ~30j 5.458e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 2.074.
- BTC 24h 0.41% · 1h 0.11% · 4h -0.12%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 683161$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.543 · OI 111923.322 (pas de dark pool free temps réel).
- Top traders L/S 2.142.
- Fear & Greed 34 (Fear).
- Market cap crypto ≈ 2.25 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.1%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -26.46 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.554 · murC 70000 (+11.2%) · murP 60000 (-4.7%).
- Volumes cachés proxy : taker buy 0.538 · vol perp/spot 14.86×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1227 · heat=100.0 · PnL sess=180.7211 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
