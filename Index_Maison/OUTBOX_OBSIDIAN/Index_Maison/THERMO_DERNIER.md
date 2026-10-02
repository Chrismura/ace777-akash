# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-02T15:42Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `86/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 85313.6 | prix |
| OI | 97150.933 | C13 |
| Funding | 1.6e-05 | C14 |
| Funding moy. ~30j | 4.963e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 0.874 | crowd |
| BTC 1h/4h/24h | -0.39 / -1.23 / 1.69 % | B7 |
| Dominance BTC | 58.76% | A3 |
| Alts ↓ 24h | 50.0% | B9 |

## Lecture
- Climat CALME (score 86/100).
- Funding maintenant 1.6e-05. Moyenne ~30j 4.963e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 0.874.
- BTC 24h 1.69% · 1h -0.39% · 4h -1.23%.
- Panier alts : 50.0% en baisse (10/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.661 · OI 97150.933 (pas de dark pool free temps réel).
- Top traders L/S 0.941.
- Fear & Greed 72 (Greed).
- Market cap crypto ≈ 2.92 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.76%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 6.77 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.521 · murC 95000 (+11.3%) · murP 75000 (-12.1%).
- Volumes cachés proxy : taker buy 0.526 · vol perp/spot 10.61×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
