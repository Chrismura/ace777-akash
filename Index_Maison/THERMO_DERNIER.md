# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-20T12:41Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `60/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 71804.3 | prix |
| OI | 108480.63 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.502e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.032 | crowd |
| BTC 1h/4h/24h | -0.12 / 0.35 / 10.93 % | B7 |
| Dominance BTC | 58.69% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat ATTENTION (score 60/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.502e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.032.
- BTC 24h 10.93% · 1h -0.12% · 4h 0.35%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.055 · OI 108480.63 (pas de dark pool free temps réel).
- Top traders L/S 1.12.
- Fear & Greed 62 (Greed).
- Market cap crypto ≈ 2.45 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.69%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 643.39 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.554 · murC 75000 (+4.5%) · murP 60000 (-16.4%).
- Volumes cachés proxy : taker buy 0.493 · vol perp/spot 12.55×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=458 · heat=100.0 · PnL sess=238.567 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
