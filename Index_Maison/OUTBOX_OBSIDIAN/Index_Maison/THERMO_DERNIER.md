# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-22T16:12Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `57/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81560.6 | prix |
| OI | 95500.214 | C13 |
| Funding | 1.9e-05 | C14 |
| Funding moy. ~30j | 2.982e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.987 | crowd |
| BTC 1h/4h/24h | -0.16 / -0.16 / -3.47 % | B7 |
| Dominance BTC | 59.47% | A3 |
| Alts ↓ 24h | 85.0% | B9 |

## Lecture
- Climat ATTENTION (score 57/100).
- Funding maintenant 1.9e-05. Moyenne ~30j 2.982e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.987.
- BTC 24h -3.47% · 1h -0.16% · 4h -0.16%.
- Panier alts : 85.0% en baisse (17/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 663430$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.925 · OI 95500.214 (pas de dark pool free temps réel).
- Top traders L/S 2.133.
- Fear & Greed 68 (Greed).
- Market cap crypto ≈ 2.76 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.47%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 67.36 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.588 · murC 95000 (+16.6%) · murP 75000 (-7.9%).
- Volumes cachés proxy : taker buy 0.529 · vol perp/spot 14.12×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
