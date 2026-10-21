# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-21T05:31Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `77/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82873.74 | prix |
| OI | 95051.08 | C13 |
| Funding | 6.8e-05 | C14 |
| Funding moy. ~30j | 3.228e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.463 | crowd |
| BTC 1h/4h/24h | 0.12 / -0.11 / 1.15 % | B7 |
| Dominance BTC | 59.52% | A3 |
| Alts ↓ 24h | 15.0% | B9 |

## Lecture
- Climat CALME (score 77/100).
- Funding maintenant 6.8e-05. Moyenne ~30j 3.228e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.463.
- BTC 24h 1.15% · 1h 0.12% · 4h -0.11%.
- Panier alts : 15.0% en baisse (3/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.121 · OI 95051.08 (pas de dark pool free temps réel).
- Top traders L/S 1.593.
- Fear & Greed 63 (Greed).
- Market cap crypto ≈ 2.79 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.52%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -79.62 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.6 · murC 95000 (+14.7%) · murP 75000 (-9.4%).
- Volumes cachés proxy : taker buy 0.54 · vol perp/spot 14.77×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
