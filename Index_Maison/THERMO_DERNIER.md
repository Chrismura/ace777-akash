# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-02T00:14Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `88/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84872.83 | prix |
| OI | 96956.941 | C13 |
| Funding | 2.4e-05 | C14 |
| Funding moy. ~30j | 4.941e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.039 | crowd |
| BTC 1h/4h/24h | 0.03 / 0.31 / 1.65 % | B7 |
| Dominance BTC | 58.58% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat CALME (score 88/100).
- Funding maintenant 2.4e-05. Moyenne ~30j 4.941e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.039.
- BTC 24h 1.65% · 1h 0.03% · 4h 0.31%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.334 · OI 96956.941 (pas de dark pool free temps réel).
- Top traders L/S 1.093.
- Fear & Greed 72 (Greed).
- Market cap crypto ≈ 2.90 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.58%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 9.33 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.553 · murC 95000 (+12.0%) · murP 80000 (-5.7%).
- Volumes cachés proxy : taker buy 0.526 · vol perp/spot 12.64×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
