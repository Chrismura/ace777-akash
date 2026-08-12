# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-12T15:49Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `80/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63485.6 | prix |
| OI | 109953.649 | C13 |
| Funding | 6.4e-05 | C14 |
| Funding moy. ~30j | 5.514e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.605 | crowd |
| BTC 1h/4h/24h | 0.22 / -1.12 / -0.08 % | B7 |
| Dominance BTC | 56.21% | A3 |
| Alts ↓ 24h | 0.0% | B9 |

## Lecture
- Climat CALME (score 80/100).
- Funding maintenant 6.4e-05. Moyenne ~30j 5.514e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.605.
- BTC 24h -0.08% · 1h 0.22% · 4h -1.12%.
- Panier alts : 0.0% en baisse (0/5).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1300156$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.923 · OI 109953.649 (pas de dark pool free temps réel).
- Top traders L/S 1.679.
- Fear & Greed 27 (Fear).
- Market cap crypto ≈ 2.27 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.21%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC 37.21 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.552 · murC 70000 (+10.3%) · murP 60000 (-5.4%).
- Volumes cachés proxy : taker buy 0.498 · vol perp/spot 12.23×.
- ACE soft: LIVE=NUAGE_PROD_4H_LIVE_COLOR.log · SKIP=886 · heat=100.0 · PnL sess=167.9867 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
