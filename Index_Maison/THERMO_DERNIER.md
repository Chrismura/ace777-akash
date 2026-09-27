# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-27T02:59Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `86/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84404.38 | prix |
| OI | 94290.632 | C13 |
| Funding | 5.3e-05 | C14 |
| Funding moy. ~30j | 5.742e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.278 | crowd |
| BTC 1h/4h/24h | -0.06 / 0.18 / 0.48 % | B7 |
| Dominance BTC | 58.31% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat CALME (score 86/100).
- Funding maintenant 5.3e-05. Moyenne ~30j 5.742e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.278.
- BTC 24h 0.48% · 1h -0.06% · 4h 0.18%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 522888$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.799 · OI 94290.632 (pas de dark pool free temps réel).
- Top traders L/S 1.387.
- Fear & Greed 70 (Greed).
- Market cap crypto ≈ 2.90 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.31%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 292.53 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.466 · murC 95000 (+12.5%) · murP 75000 (-11.2%).
- Volumes cachés proxy : taker buy 0.544 · vol perp/spot 8.43×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
