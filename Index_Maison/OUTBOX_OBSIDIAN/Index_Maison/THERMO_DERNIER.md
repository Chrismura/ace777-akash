# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-04T12:01Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `89/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 85267.7 | prix |
| OI | 98933.304 | C13 |
| Funding | 2.9e-05 | C14 |
| Funding moy. ~30j | 4.65e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.209 | crowd |
| BTC 1h/4h/24h | 0.0 / 0.24 / 0.74 % | B7 |
| Dominance BTC | 59.17% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat CALME (score 89/100).
- Funding maintenant 2.9e-05. Moyenne ~30j 4.65e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.209.
- BTC 24h 0.74% · 1h 0.0% · 4h 0.24%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.079 · OI 98933.304 (pas de dark pool free temps réel).
- Top traders L/S 1.222.
- Fear & Greed 65 (Greed).
- Market cap crypto ≈ 2.89 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.17%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 8.22 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.516 · murC 95000 (+11.3%) · murP 80000 (-6.2%).
- Volumes cachés proxy : taker buy 0.491 · vol perp/spot 11.93×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
