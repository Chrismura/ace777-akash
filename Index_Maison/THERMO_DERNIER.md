# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-20T23:45Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `65/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 73024.47 | prix |
| OI | 107534.654 | C13 |
| Funding | 4.6e-05 | C14 |
| Funding moy. ~30j | 5.586e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 0.944 | crowd |
| BTC 1h/4h/24h | 0.55 / 0.55 / 5.39 % | B7 |
| Dominance BTC | 58.74% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat ATTENTION (score 65/100).
- Funding maintenant 4.6e-05. Moyenne ~30j 5.586e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 0.944.
- BTC 24h 5.39% · 1h 0.55% · 4h 0.55%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 780382$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.821 · OI 107534.654 (pas de dark pool free temps réel).
- Top traders L/S 1.04.
- Fear & Greed 62 (Greed).
- Market cap crypto ≈ 2.49 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.74%).
- Liquidations 24h proxy ≈ 0.03 B$.
- ETF net inflow : BTC 654.33 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.572 · murC 75000 (+2.7%) · murP 60000 (-17.9%).
- Volumes cachés proxy : taker buy 0.516 · vol perp/spot 11.43×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=743 · heat=100.0 · PnL sess=240.4108 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
