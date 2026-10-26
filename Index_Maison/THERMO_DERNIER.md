# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-26T20:30Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `59/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79850.9 | prix |
| OI | 95053.768 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 3.61e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.219 | crowd |
| BTC 1h/4h/24h | -0.18 / -0.43 / -0.83 % | B7 |
| Dominance BTC | 59.42% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat ATTENTION (score 59/100).
- Funding maintenant 0.0001. Moyenne ~30j 3.61e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.219.
- BTC 24h -0.83% · 1h -0.18% · 4h -0.43%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 879857$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.887 · OI 95053.768 (pas de dark pool free temps réel).
- Top traders L/S 2.336.
- Fear & Greed 50 (Neutral).
- Market cap crypto ≈ 2.69 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.42%).
- Liquidations 24h proxy ≈ 2.39 M$.
- ETF net inflow : BTC 30.26 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.596 · murC 95000 (+19.2%) · murP 75000 (-5.9%).
- Volumes cachés proxy : taker buy 0.5 · vol perp/spot 16.31×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
