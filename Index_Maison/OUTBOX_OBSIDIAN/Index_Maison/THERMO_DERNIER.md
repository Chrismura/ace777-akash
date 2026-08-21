# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-21T03:48Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `61/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 74761.6 | prix |
| OI | 108023.771 | C13 |
| Funding | 9.2e-05 | C14 |
| Funding moy. ~30j | 5.597e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.021 | crowd |
| BTC 1h/4h/24h | 0.51 / 2.45 / 8.03 % | B7 |
| Dominance BTC | 59.0% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat ATTENTION (score 61/100).
- Funding maintenant 9.2e-05. Moyenne ~30j 5.597e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.021.
- BTC 24h 8.03% · 1h 0.51% · 4h 2.45%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1306322$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.903 · OI 108023.771 (pas de dark pool free temps réel).
- Top traders L/S 1.079.
- Fear & Greed 72 (Greed).
- Market cap crypto ≈ 2.53 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.0%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 82.34 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.569 · murC 78000 (+4.3%) · murP 60000 (-19.8%).
- Volumes cachés proxy : taker buy 0.516 · vol perp/spot 12.32×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=743 · heat=100.0 · PnL sess=240.4108 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
