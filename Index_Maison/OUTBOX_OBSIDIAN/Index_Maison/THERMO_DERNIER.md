# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-29T11:42Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `83/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84175.09 | prix |
| OI | 93241.127 | C13 |
| Funding | 5.5e-05 | C14 |
| Funding moy. ~30j | 5.24e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.22 | crowd |
| BTC 1h/4h/24h | 0.22 / 0.27 / 1.36 % | B7 |
| Dominance BTC | 58.75% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 83/100).
- Funding maintenant 5.5e-05. Moyenne ~30j 5.24e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.22.
- BTC 24h 1.36% · 1h 0.22% · 4h 0.27%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 547755$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.718 · OI 93241.127 (pas de dark pool free temps réel).
- Top traders L/S 1.292.
- Fear & Greed 73 (Greed).
- Market cap crypto ≈ 2.88 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.75%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 314.46 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.497 · murC 95000 (+12.9%) · murP 75000 (-10.9%).
- Volumes cachés proxy : taker buy 0.514 · vol perp/spot 14.27×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
