# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-05T19:35Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `95/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 85692.0 | prix |
| OI | 94722.55 | C13 |
| Funding | 7e-06 | C14 |
| Funding moy. ~30j | 4.724e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.146 | crowd |
| BTC 1h/4h/24h | 0.09 / 0.55 / 0.22 % | B7 |
| Dominance BTC | 58.71% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 95/100).
- Funding maintenant 7e-06. Moyenne ~30j 4.724e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.146.
- BTC 24h 0.22% · 1h 0.09% · 4h 0.55%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.33 · OI 94722.55 (pas de dark pool free temps réel).
- Top traders L/S 1.232.
- Fear & Greed 70 (Greed).
- Market cap crypto ≈ 2.93 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.71%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 281.96 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.521 · murC 95000 (+10.8%) · murP 80000 (-6.7%).
- Volumes cachés proxy : taker buy 0.502 · vol perp/spot 13.11×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
