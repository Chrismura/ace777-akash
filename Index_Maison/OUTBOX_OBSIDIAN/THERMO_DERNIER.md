# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-10T07:29Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `86/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 65312.14 | prix |
| OI | 107251.903 | C13 |
| Funding | 7.5e-05 | C14 |
| Funding moy. ~30j | 5.358e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.134 | crowd |
| BTC 1h/4h/24h | 0.05 / 0.56 / 0.77 % | B7 |
| Dominance BTC | 56.7% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat CALME (score 86/100).
- Funding maintenant 7.5e-05. Moyenne ~30j 5.358e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.134.
- BTC 24h 0.77% · 1h 0.05% · 4h 0.56%.
- Panier alts : 20.0% en baisse (1/5).
- Whales proxy : 2 gros print(s) ≥500k$ (max 795028$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.232 · OI 107251.903 (pas de dark pool free temps réel).
- Top traders L/S 1.211.
- Fear & Greed 30 (Fear).
- Market cap crypto ≈ 2.31 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.7%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC 69.48 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.595 · murC 70000 (+7.2%) · murP 60000 (-8.1%).
- Volumes cachés proxy : taker buy 0.518 · vol perp/spot 18.2×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
