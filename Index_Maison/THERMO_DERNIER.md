# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-09T11:22Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `91/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64948.96 | prix |
| OI | 106318.641 | C13 |
| Funding | 4.3e-05 | C14 |
| Funding moy. ~30j | 5.413e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.202 | crowd |
| BTC 1h/4h/24h | 0.03 / 0.24 / -0.01 % | B7 |
| Dominance BTC | 56.65% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 91/100).
- Funding maintenant 4.3e-05. Moyenne ~30j 5.413e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.202.
- BTC 24h -0.01% · 1h 0.03% · 4h 0.24%.
- Panier alts : 40.0% en baisse (2/5).
- Whales proxy : 2 gros print(s) ≥500k$ (max 742421$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.233 · OI 106318.641 (pas de dark pool free temps réel).
- Top traders L/S 1.295.
- Fear & Greed 31 (Fear).
- Market cap crypto ≈ 2.30 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.65%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 84.39 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.596 · murC 70000 (+7.8%) · murP 60000 (-7.6%).
- Volumes cachés proxy : taker buy 0.503 · vol perp/spot 18.6×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
