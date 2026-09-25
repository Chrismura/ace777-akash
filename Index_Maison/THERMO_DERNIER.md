# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-25T20:24Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `87/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84016.57 | prix |
| OI | 95335.412 | C13 |
| Funding | 5.1e-05 | C14 |
| Funding moy. ~30j | 5.938e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.303 | crowd |
| BTC 1h/4h/24h | 0.06 / 0.36 / -0.2 % | B7 |
| Dominance BTC | 58.23% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat CALME (score 87/100).
- Funding maintenant 5.1e-05. Moyenne ~30j 5.938e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.303.
- BTC 24h -0.2% · 1h 0.06% · 4h 0.36%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 1089726$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.23 · OI 95335.412 (pas de dark pool free temps réel).
- Top traders L/S 1.407.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.89 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.23%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 291.19 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.469 · murC 95000 (+13.0%) · murP 78000 (-7.2%).
- Volumes cachés proxy : taker buy 0.484 · vol perp/spot 15.46×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
