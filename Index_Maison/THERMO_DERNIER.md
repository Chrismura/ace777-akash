# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-09T09:16Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `89/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64792.9 | prix |
| OI | 106419.698 | C13 |
| Funding | 5.8e-05 | C14 |
| Funding moy. ~30j | 5.413e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.203 | crowd |
| BTC 1h/4h/24h | 0.0 / 0.02 / -0.29 % | B7 |
| Dominance BTC | 56.62% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 89/100).
- Funding maintenant 5.8e-05. Moyenne ~30j 5.413e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.203.
- BTC 24h -0.29% · 1h 0.0% · 4h 0.02%.
- Panier alts : 60.0% en baisse (3/5).
- Whales proxy : 1 gros print(s) ≥500k$ (max 568946$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.163 · OI 106419.698 (pas de dark pool free temps réel).
- Top traders L/S 1.297.
- Fear & Greed 31 (Fear).
- Market cap crypto ≈ 2.30 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.62%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 84.18 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.596 · murC 70000 (+8.1%) · murP 60000 (-7.4%).
- Volumes cachés proxy : taker buy 0.503 · vol perp/spot 18.07×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
