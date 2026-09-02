# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-02T21:56Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `91/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77288.2 | prix |
| OI | 108013.938 | C13 |
| Funding | 4.3e-05 | C14 |
| Funding moy. ~30j | 6.773e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.214 | crowd |
| BTC 1h/4h/24h | -0.1 / -0.08 / 0.08 % | B7 |
| Dominance BTC | 59.07% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat CALME (score 91/100).
- Funding maintenant 4.3e-05. Moyenne ~30j 6.773e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.214.
- BTC 24h 0.08% · 1h -0.1% · 4h -0.08%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.233 · OI 108013.938 (pas de dark pool free temps réel).
- Top traders L/S 1.288.
- Fear & Greed 63 (Greed).
- Market cap crypto ≈ 2.62 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.07%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 59.44 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.549 · murC 82000 (+6.1%) · murP 70000 (-9.4%).
- Volumes cachés proxy : taker buy 0.581 · vol perp/spot 14.51×.
- ACE soft: LIVE=ACE_RADAR_ALIGNED_V4_60M_LIVE_COLOR.log · SKIP=705 · heat=27.4 · PnL sess=-9.1224 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
