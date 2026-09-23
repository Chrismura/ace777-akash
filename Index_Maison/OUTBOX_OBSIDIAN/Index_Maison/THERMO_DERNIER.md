# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-23T14:17Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `87/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84449.81 | prix |
| OI | 104732.888 | C13 |
| Funding | 1.4e-05 | C14 |
| Funding moy. ~30j | 6.447e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 0.975 | crowd |
| BTC 1h/4h/24h | -1.46 / -1.61 / -2.08 % | B7 |
| Dominance BTC | 58.77% | A3 |
| Alts ↓ 24h | 70.0% | B9 |

## Lecture
- Climat CALME (score 87/100).
- Funding maintenant 1.4e-05. Moyenne ~30j 6.447e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 0.975.
- BTC 24h -2.08% · 1h -1.46% · 4h -1.61%.
- Panier alts : 70.0% en baisse (14/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.099 · OI 104732.888 (pas de dark pool free temps réel).
- Top traders L/S 1.078.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.90 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.77%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 1413.73 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.583 · murC 95000 (+12.4%) · murP 70000 (-17.2%).
- Volumes cachés proxy : taker buy 0.555 · vol perp/spot 13.47×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
