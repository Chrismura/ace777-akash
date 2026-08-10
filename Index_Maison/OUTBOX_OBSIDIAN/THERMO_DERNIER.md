# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-10T10:39Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `88/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 65002.3 | prix |
| OI | 106958.679 | C13 |
| Funding | 8.7e-05 | C14 |
| Funding moy. ~30j | 5.435e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.145 | crowd |
| BTC 1h/4h/24h | 0.09 / -0.42 / 0.14 % | B7 |
| Dominance BTC | 56.67% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 88/100).
- Funding maintenant 8.7e-05. Moyenne ~30j 5.435e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.145.
- BTC 24h 0.14% · 1h 0.09% · 4h -0.42%.
- Panier alts : 60.0% en baisse (3/5).
- Whales proxy : 1 gros print(s) ≥500k$ (max 571263$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.839 · OI 106958.679 (pas de dark pool free temps réel).
- Top traders L/S 1.222.
- Fear & Greed 30 (Fear).
- Market cap crypto ≈ 2.30 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.67%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC 69.15 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.595 · murC 70000 (+7.7%) · murP 60000 (-7.7%).
- Volumes cachés proxy : taker buy 0.518 · vol perp/spot 17.58×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
