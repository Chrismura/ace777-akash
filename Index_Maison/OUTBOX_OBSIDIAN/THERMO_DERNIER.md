# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-19T14:58Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `75/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82220.0 | prix |
| OI | 94883.443 | C13 |
| Funding | 7.4e-05 | C14 |
| Funding moy. ~30j | 3.261e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.447 | crowd |
| BTC 1h/4h/24h | 0.17 / -0.19 / 1.42 % | B7 |
| Dominance BTC | 59.66% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat CALME (score 75/100).
- Funding maintenant 7.4e-05. Moyenne ~30j 3.261e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.447.
- BTC 24h 1.42% · 1h 0.17% · 4h -0.19%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.886 · OI 94883.443 (pas de dark pool free temps réel).
- Top traders L/S 1.563.
- Fear & Greed 59 (Greed).
- Market cap crypto ≈ 2.77 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.66%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -20.27 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.578 · murC 95000 (+15.6%) · murP 75000 (-8.7%).
- Volumes cachés proxy : taker buy 0.455 · vol perp/spot 12.72×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
