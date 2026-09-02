# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-02T00:22Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `76/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77329.8 | prix |
| OI | 108365.827 | C13 |
| Funding | 7.9e-05 | C14 |
| Funding moy. ~30j | 6.74e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.286 | crowd |
| BTC 1h/4h/24h | -0.09 / -0.11 / -1.84 % | B7 |
| Dominance BTC | 59.06% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat CALME (score 76/100).
- Funding maintenant 7.9e-05. Moyenne ~30j 6.74e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.286.
- BTC 24h -1.84% · 1h -0.09% · 4h -0.11%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.028 · OI 108365.827 (pas de dark pool free temps réel).
- Top traders L/S 1.388.
- Fear & Greed 63 (Greed).
- Market cap crypto ≈ 2.62 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.06%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 59.47 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.567 · murC 82000 (+6.0%) · murP 70000 (-9.5%).
- Volumes cachés proxy : taker buy 0.521 · vol perp/spot 16.75×.
- ACE soft: LIVE=ACE_RADAR_ALIGNED_V4_60M_LIVE_COLOR.log · SKIP=298 · heat=10.9 · PnL sess=-3.6172 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
