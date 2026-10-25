# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-25T16:01Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `62/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80576.1 | prix |
| OI | 93555.316 | C13 |
| Funding | 8e-05 | C14 |
| Funding moy. ~30j | 3.449e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.13 | crowd |
| BTC 1h/4h/24h | -0.03 / 0.19 / 1.01 % | B7 |
| Dominance BTC | 60.08% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat ATTENTION (score 62/100).
- Funding maintenant 8e-05. Moyenne ~30j 3.449e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.13.
- BTC 24h 1.01% · 1h -0.03% · 4h 0.19%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.569 · OI 93555.316 (pas de dark pool free temps réel).
- Top traders L/S 2.255.
- Fear & Greed 54 (Neutral).
- Market cap crypto ≈ 2.69 T$.
- Alt season proxy : Bitcoin season (BTC.D 60.08%).
- Liquidations 24h proxy ≈ 2.19 M$.
- ETF net inflow : BTC 64.26 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.594 · murC 95000 (+18.0%) · murP 75000 (-6.8%).
- Volumes cachés proxy : taker buy 0.536 · vol perp/spot 17.01×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
