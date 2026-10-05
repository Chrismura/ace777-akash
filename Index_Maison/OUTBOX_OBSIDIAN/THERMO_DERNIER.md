# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-05T10:31Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `90/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 85988.24 | prix |
| OI | 97218.493 | C13 |
| Funding | 5.6e-05 | C14 |
| Funding moy. ~30j | 4.763e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 0.984 | crowd |
| BTC 1h/4h/24h | 0.06 / -0.27 / 0.74 % | B7 |
| Dominance BTC | 59.23% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat CALME (score 90/100).
- Funding maintenant 5.6e-05. Moyenne ~30j 4.763e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 0.984.
- BTC 24h 0.74% · 1h 0.06% · 4h -0.27%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.827 · OI 97218.493 (pas de dark pool free temps réel).
- Top traders L/S 1.075.
- Fear & Greed 70 (Greed).
- Market cap crypto ≈ 2.92 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.23%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC 8.29 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.518 · murC 95000 (+10.5%) · murP 80000 (-7.0%).
- Volumes cachés proxy : taker buy 0.486 · vol perp/spot 12.36×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
