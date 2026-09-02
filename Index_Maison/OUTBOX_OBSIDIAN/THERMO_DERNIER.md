# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-02T00:28Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `76/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77273.5 | prix |
| OI | 108308.511 | C13 |
| Funding | 7.6e-05 | C14 |
| Funding moy. ~30j | 6.74e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.286 | crowd |
| BTC 1h/4h/24h | -0.16 / -0.18 / -2.01 % | B7 |
| Dominance BTC | 59.07% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat CALME (score 76/100).
- Funding maintenant 7.6e-05. Moyenne ~30j 6.74e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.286.
- BTC 24h -2.01% · 1h -0.16% · 4h -0.18%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 514785$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.028 · OI 108308.511 (pas de dark pool free temps réel).
- Top traders L/S 1.388.
- Fear & Greed 63 (Greed).
- Market cap crypto ≈ 2.62 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.07%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 59.43 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.567 · murC 82000 (+6.1%) · murP 70000 (-9.4%).
- Volumes cachés proxy : taker buy 0.521 · vol perp/spot 16.76×.
- ACE soft: LIVE=ACE_RADAR_ALIGNED_V4_60M_LIVE_COLOR.log · SKIP=375 · heat=10.9 · PnL sess=-3.6321 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
