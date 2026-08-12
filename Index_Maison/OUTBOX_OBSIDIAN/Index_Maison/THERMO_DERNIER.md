# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-12T06:20Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `74/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63668.5 | prix |
| OI | 108779.859 | C13 |
| Funding | 7.5e-05 | C14 |
| Funding moy. ~30j | 5.473e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.739 | crowd |
| BTC 1h/4h/24h | -0.22 / -0.08 / -0.48 % | B7 |
| Dominance BTC | 56.28% | A3 |
| Alts ↓ 24h | 0.0% | B9 |

## Lecture
- Climat CALME (score 74/100).
- Funding maintenant 7.5e-05. Moyenne ~30j 5.473e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.739.
- BTC 24h -0.48% · 1h -0.22% · 4h -0.08%.
- Panier alts : 0.0% en baisse (0/5).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1003875$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.939 · OI 108779.859 (pas de dark pool free temps réel).
- Top traders L/S 1.821.
- Fear & Greed 27 (Fear).
- Market cap crypto ≈ 2.27 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.28%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC 37.32 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.577 · murC 70000 (+10.0%) · murP 60000 (-5.7%).
- Volumes cachés proxy : taker buy 0.498 · vol perp/spot 12.19×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
