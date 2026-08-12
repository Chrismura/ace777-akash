# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-12T11:36Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `76/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64139.7 | prix |
| OI | 107909.823 | C13 |
| Funding | 8.1e-05 | C14 |
| Funding moy. ~30j | 5.514e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.667 | crowd |
| BTC 1h/4h/24h | 0.04 / 0.53 / -0.28 % | B7 |
| Dominance BTC | 56.34% | A3 |
| Alts ↓ 24h | 0.0% | B9 |

## Lecture
- Climat CALME (score 76/100).
- Funding maintenant 8.1e-05. Moyenne ~30j 5.514e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.667.
- BTC 24h -0.28% · 1h 0.04% · 4h 0.53%.
- Panier alts : 0.0% en baisse (0/5).
- Whales proxy : 1 gros print(s) ≥500k$ (max 722145$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.083 · OI 107909.823 (pas de dark pool free temps réel).
- Top traders L/S 1.739.
- Fear & Greed 27 (Fear).
- Market cap crypto ≈ 2.28 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.34%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC 37.59 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.565 · murC 70000 (+9.2%) · murP 60000 (-6.4%).
- Volumes cachés proxy : taker buy 0.498 · vol perp/spot 12.05×.
- ACE soft: LIVE=NUAGE_PROD_4H_LIVE_COLOR.log · SKIP=944 · heat=100.0 · PnL sess=178.5128 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
