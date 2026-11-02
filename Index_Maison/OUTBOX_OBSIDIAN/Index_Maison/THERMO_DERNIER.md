# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-11-02T05:19Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `67/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78240.95 | prix |
| OI | 95298.937 | C13 |
| Funding | 6.7e-05 | C14 |
| Funding moy. ~30j | 4.523e-05 (n=90) | Cortana |
| Funding mois préc. | 4.378e-05 (n=93) | Cortana |
| L/S 1h | 2.084 | crowd |
| BTC 1h/4h/24h | -0.17 / -0.16 / 0.58 % | B7 |
| Dominance BTC | 60.05% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat ATTENTION (score 67/100).
- Funding maintenant 6.7e-05. Moyenne ~30j 4.523e-05 (90 pts). Mois précédent 4.378e-05 (93 pts).
- Long/Short 2.084.
- BTC 24h 0.58% · 1h -0.17% · 4h -0.16%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.772 · OI 95298.937 (pas de dark pool free temps réel).
- Top traders L/S 2.211.
- Fear & Greed 37 (Fear).
- Market cap crypto ≈ 2.62 T$.
- Alt season proxy : Bitcoin season (BTC.D 60.05%).
- Liquidations 24h proxy ≈ 1.92 M$.
- ETF net inflow : BTC 63.59 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.663 · murC 90000 (+15.1%) · murP 74000 (-5.3%).
- Volumes cachés proxy : taker buy 0.528 · vol perp/spot 8.25×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
