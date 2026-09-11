# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-11T14:14Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `69/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79088.45 | prix |
| OI | 104472.893 | C13 |
| Funding | 6.8e-05 | C14 |
| Funding moy. ~30j | 6.702e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.486 | crowd |
| BTC 1h/4h/24h | -0.19 / 2.73 / 2.56 % | B7 |
| Dominance BTC | 58.3% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat ATTENTION (score 69/100).
- Funding maintenant 6.8e-05. Moyenne ~30j 6.702e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.486.
- BTC 24h 2.56% · 1h -0.19% · 4h 2.73%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.155 · OI 104472.893 (pas de dark pool free temps réel).
- Top traders L/S 1.501.
- Fear & Greed 56 (Greed).
- Market cap crypto ≈ 2.76 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.3%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 77.14 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.531 · murC 90000 (+13.9%) · murP 70000 (-11.4%).
- Volumes cachés proxy : taker buy 0.447 · vol perp/spot 13.85×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
