# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-09T21:09Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `88/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78233.35 | prix |
| OI | 104919.941 | C13 |
| Funding | 6.7e-05 | C14 |
| Funding moy. ~30j | 6.74e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.178 | crowd |
| BTC 1h/4h/24h | -0.07 / -0.65 / -0.32 % | B7 |
| Dominance BTC | 58.46% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat CALME (score 88/100).
- Funding maintenant 6.7e-05. Moyenne ~30j 6.74e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.178.
- BTC 24h -0.32% · 1h -0.07% · 4h -0.65%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.03 · OI 104919.941 (pas de dark pool free temps réel).
- Top traders L/S 1.233.
- Fear & Greed 66 (Greed).
- Market cap crypto ≈ 2.69 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.46%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 148.05 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.534 · murC 81000 (+3.5%) · murP 70000 (-10.5%).
- Volumes cachés proxy : taker buy 0.484 · vol perp/spot 15.81×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
