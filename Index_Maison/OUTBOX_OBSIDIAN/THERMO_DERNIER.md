# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-21T05:49Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `65/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 75232.26 | prix |
| OI | 109297.222 | C13 |
| Funding | 5.1e-05 | C14 |
| Funding moy. ~30j | 5.597e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.028 | crowd |
| BTC 1h/4h/24h | 0.33 / 0.18 / 8.39 % | B7 |
| Dominance BTC | 59.18% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat ATTENTION (score 65/100).
- Funding maintenant 5.1e-05. Moyenne ~30j 5.597e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.028.
- BTC 24h 8.39% · 1h 0.33% · 4h 0.18%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.075 · OI 109297.222 (pas de dark pool free temps réel).
- Top traders L/S 1.082.
- Fear & Greed 72 (Greed).
- Market cap crypto ≈ 2.55 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.18%).
- Liquidations 24h proxy ≈ 0.04 B$.
- ETF net inflow : BTC 82.86 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.568 · murC 78000 (+3.7%) · murP 60000 (-20.3%).
- Volumes cachés proxy : taker buy 0.516 · vol perp/spot 12.58×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=743 · heat=100.0 · PnL sess=240.4108 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
