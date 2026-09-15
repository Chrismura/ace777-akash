# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-15T18:43Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `52/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 75835.62 | prix |
| OI | 107296.167 | C13 |
| Funding | 8.4e-05 | C14 |
| Funding moy. ~30j | 6.757e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.75 | crowd |
| BTC 1h/4h/24h | -1.3 / 0.03 / -4.3 % | B7 |
| Dominance BTC | 58.44% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat ATTENTION (score 52/100).
- Funding maintenant 8.4e-05. Moyenne ~30j 6.757e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.75.
- BTC 24h -4.3% · 1h -1.3% · 4h 0.03%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1057262$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.119 · OI 107296.167 (pas de dark pool free temps réel).
- Top traders L/S 1.845.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.64 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.44%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC 102.31 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.525 · murC 85000 (+12.1%) · murP 70000 (-7.7%).
- Volumes cachés proxy : taker buy 0.508 · vol perp/spot 13.62×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
