# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-24T22:28Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `62/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80472.5 | prix |
| OI | 95673.41 | C13 |
| Funding | 8.1e-05 | C14 |
| Funding moy. ~30j | 3.224e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.136 | crowd |
| BTC 1h/4h/24h | 0.11 / -0.04 / -1.02 % | B7 |
| Dominance BTC | 59.51% | A3 |
| Alts ↓ 24h | 70.0% | B9 |

## Lecture
- Climat ATTENTION (score 62/100).
- Funding maintenant 8.1e-05. Moyenne ~30j 3.224e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.136.
- BTC 24h -1.02% · 1h 0.11% · 4h -0.04%.
- Panier alts : 70.0% en baisse (14/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.02 · OI 95673.41 (pas de dark pool free temps réel).
- Top traders L/S 2.276.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.71 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.51%).
- Liquidations 24h proxy ≈ 4.55 M$.
- ETF net inflow : BTC 64.17 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.57 · murC 95000 (+18.2%) · murP 75000 (-6.7%).
- Volumes cachés proxy : taker buy 0.536 · vol perp/spot 16.05×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
