# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-30T02:55Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `52/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77317.1 | prix |
| OI | 96037.201 | C13 |
| Funding | 3e-06 | C14 |
| Funding moy. ~30j | 4.08e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 2.605 | crowd |
| BTC 1h/4h/24h | 0.7 / -2.08 / -3.22 % | B7 |
| Dominance BTC | 59.27% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat ATTENTION (score 52/100).
- Funding maintenant 3e-06. Moyenne ~30j 4.08e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 2.605.
- BTC 24h -3.22% · 1h 0.7% · 4h -2.08%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 800077$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.837 · OI 96037.201 (pas de dark pool free temps réel).
- Top traders L/S 2.786.
- Fear & Greed 30 (Fear).
- Market cap crypto ≈ 2.61 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.27%).
- Liquidations 24h proxy ≈ 3.81 M$.
- ETF net inflow : BTC 21.09 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.623 · murC 95000 (+23.1%) · murP 70000 (-9.3%).
- Volumes cachés proxy : taker buy 0.526 · vol perp/spot 12.55×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
