# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-18T17:52Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `63/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80858.3 | prix |
| OI | 109938.489 | C13 |
| Funding | 6.1e-05 | C14 |
| Funding moy. ~30j | 6.827e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 0.951 | crowd |
| BTC 1h/4h/24h | 0.06 / 1.01 / 5.56 % | B7 |
| Dominance BTC | 58.47% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat ATTENTION (score 63/100).
- Funding maintenant 6.1e-05. Moyenne ~30j 6.827e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 0.951.
- BTC 24h 5.56% · 1h 0.06% · 4h 1.01%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 603377$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.948 · OI 109938.489 (pas de dark pool free temps réel).
- Top traders L/S 1.023.
- Fear & Greed 56 (Greed).
- Market cap crypto ≈ 2.77 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.47%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -101.61 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.558 · murC 85000 (+5.1%) · murP 70000 (-13.5%).
- Volumes cachés proxy : taker buy 0.496 · vol perp/spot 13.31×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
