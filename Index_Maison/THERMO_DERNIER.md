# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-10T04:10Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `80/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78353.38 | prix |
| OI | 105425.037 | C13 |
| Funding | 8.1e-05 | C14 |
| Funding moy. ~30j | 6.754e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.459 | crowd |
| BTC 1h/4h/24h | 0.06 / 0.26 / -0.49 % | B7 |
| Dominance BTC | 58.54% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 80/100).
- Funding maintenant 8.1e-05. Moyenne ~30j 6.754e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.459.
- BTC 24h -0.49% · 1h 0.06% · 4h 0.26%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : 5 gros print(s) ≥500k$ (max 1523791$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.311 · OI 105425.037 (pas de dark pool free temps réel).
- Top traders L/S 1.525.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.68 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.54%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 93.8 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.54 · murC 81000 (+3.4%) · murP 70000 (-10.6%).
- Volumes cachés proxy : taker buy 0.484 · vol perp/spot 15.65×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
