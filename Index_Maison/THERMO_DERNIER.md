# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-09T13:29Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `90/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 65035.34 | prix |
| OI | 106456.217 | C13 |
| Funding | 5.7e-05 | C14 |
| Funding moy. ~30j | 5.413e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.183 | crowd |
| BTC 1h/4h/24h | 0.16 / 0.28 / 0.07 % | B7 |
| Dominance BTC | 56.64% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 90/100).
- Funding maintenant 5.7e-05. Moyenne ~30j 5.413e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.183.
- BTC 24h 0.07% · 1h 0.16% · 4h 0.28%.
- Panier alts : 40.0% en baisse (2/5).
- Whales proxy : 1 gros print(s) ≥500k$ (max 650700$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.701 · OI 106456.217 (pas de dark pool free temps réel).
- Top traders L/S 1.278.
- Fear & Greed 31 (Fear).
- Market cap crypto ≈ 2.30 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.64%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 84.5 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.597 · murC 70000 (+7.6%) · murP 60000 (-7.7%).
- Volumes cachés proxy : taker buy 0.503 · vol perp/spot 18.12×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
