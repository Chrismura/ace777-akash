# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-28T13:30Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `72/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80709.78 | prix |
| OI | 96280.314 | C13 |
| Funding | 5.5e-05 | C14 |
| Funding moy. ~30j | 4.003e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.86 | crowd |
| BTC 1h/4h/24h | -0.09 / -1.08 / 0.72 % | B7 |
| Dominance BTC | 59.45% | A3 |
| Alts ↓ 24h | 10.0% | B9 |

## Lecture
- Climat CALME (score 72/100).
- Funding maintenant 5.5e-05. Moyenne ~30j 4.003e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.86.
- BTC 24h 0.72% · 1h -0.09% · 4h -1.08%.
- Panier alts : 10.0% en baisse (2/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 752795$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.803 · OI 96280.314 (pas de dark pool free temps réel).
- Top traders L/S 1.971.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.72 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.45%).
- Liquidations 24h proxy ≈ 3.40 M$.
- ETF net inflow : BTC 131.95 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.584 · murC 95000 (+17.9%) · murP 75000 (-6.9%).
- Volumes cachés proxy : taker buy 0.513 · vol perp/spot 13.6×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
