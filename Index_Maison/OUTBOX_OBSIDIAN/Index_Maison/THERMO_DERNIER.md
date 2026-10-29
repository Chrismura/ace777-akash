# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-29T10:19Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `57/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80083.61 | prix |
| OI | 96904.917 | C13 |
| Funding | 7e-05 | C14 |
| Funding moy. ~30j | 4.029e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 2.222 | crowd |
| BTC 1h/4h/24h | -0.11 / 0.19 / -1.69 % | B7 |
| Dominance BTC | 59.49% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat ATTENTION (score 57/100).
- Funding maintenant 7e-05. Moyenne ~30j 4.029e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 2.222.
- BTC 24h -1.69% · 1h -0.11% · 4h 0.19%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.624 · OI 96904.917 (pas de dark pool free temps réel).
- Top traders L/S 2.353.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.70 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.49%).
- Liquidations 24h proxy ≈ 1.77 M$.
- ETF net inflow : BTC -0.93 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.592 · murC 95000 (+18.7%) · murP 75000 (-6.3%).
- Volumes cachés proxy : taker buy 0.492 · vol perp/spot 15.57×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
