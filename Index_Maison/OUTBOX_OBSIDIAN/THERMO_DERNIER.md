# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-21T21:09Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `60/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77379.67 | prix |
| OI | 105996.245 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.696e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.026 | crowd |
| BTC 1h/4h/24h | -0.11 / 0.01 / 6.67 % | B7 |
| Dominance BTC | 59.2% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat ATTENTION (score 60/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.696e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.026.
- BTC 24h 6.67% · 1h -0.11% · 4h 0.01%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.05 · OI 105996.245 (pas de dark pool free temps réel).
- Top traders L/S 1.085.
- Fear & Greed 72 (Greed).
- Market cap crypto ≈ 2.62 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.2%).
- Liquidations 24h proxy ≈ 0.04 B$.
- ETF net inflow : BTC 993.6 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.614 · murC 78000 (+0.8%) · murP 60000 (-22.5%).
- Volumes cachés proxy : taker buy 0.534 · vol perp/spot 13.26×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1001 · heat=100.0 · PnL sess=282.4794 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
