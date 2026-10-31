# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-31T12:54Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `60/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77528.37 | prix |
| OI | 96792.476 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.251e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 2.666 | crowd |
| BTC 1h/4h/24h | -0.06 / 0.27 / 0.21 % | B7 |
| Dominance BTC | 59.28% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat ATTENTION (score 60/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.251e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 2.666.
- BTC 24h 0.21% · 1h -0.06% · 4h 0.27%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 742336$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.607 · OI 96792.476 (pas de dark pool free temps réel).
- Top traders L/S 2.831.
- Fear & Greed 30 (Fear).
- Market cap crypto ≈ 2.63 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.28%).
- Liquidations 24h proxy ≈ 1.19 M$.
- ETF net inflow : BTC 26.06 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.67 · murC 90000 (+16.2%) · murP 74000 (-4.4%).
- Volumes cachés proxy : taker buy 0.509 · vol perp/spot 7.56×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
