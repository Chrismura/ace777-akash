# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-18T23:07Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `75/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81719.7 | prix |
| OI | 93269.362 | C13 |
| Funding | 3.3e-05 | C14 |
| Funding moy. ~30j | 3.28e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.855 | crowd |
| BTC 1h/4h/24h | -0.03 / 1.08 / 0.5 % | B7 |
| Dominance BTC | 60.09% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 75/100).
- Funding maintenant 3.3e-05. Moyenne ~30j 3.28e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.855.
- BTC 24h 0.5% · 1h -0.03% · 4h 1.08%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 699966$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.241 · OI 93269.362 (pas de dark pool free temps réel).
- Top traders L/S 1.936.
- Fear & Greed 53 (Neutral).
- Market cap crypto ≈ 2.73 T$.
- Alt season proxy : Bitcoin season (BTC.D 60.09%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -46.39 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.591 · murC 95000 (+16.3%) · murP 80000 (-2.0%).
- Volumes cachés proxy : taker buy 0.455 · vol perp/spot 16.04×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
