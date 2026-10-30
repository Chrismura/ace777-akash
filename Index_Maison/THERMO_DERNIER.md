# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-30T14:53Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `hot` · **Score :** `35/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77170.35 | prix |
| OI | 97100.989 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.13e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 2.617 | crowd |
| BTC 1h/4h/24h | 0.05 / -0.81 / -4.75 % | B7 |
| Dominance BTC | 59.13% | A3 |
| Alts ↓ 24h | 85.0% | B9 |

## Lecture
- Climat CHAUD (score 35/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.13e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 2.617.
- BTC 24h -4.75% · 1h 0.05% · 4h -0.81%.
- Panier alts : 85.0% en baisse (17/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.022 · OI 97100.989 (pas de dark pool free temps réel).
- Top traders L/S 2.808.
- Fear & Greed 30 (Fear).
- Market cap crypto ≈ 2.62 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.13%).
- Liquidations 24h proxy ≈ 2.86 M$.
- ETF net inflow : BTC 21.63 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.725 · murC 90000 (+16.8%) · murP 60000 (-22.1%).
- Volumes cachés proxy : taker buy 0.526 · vol perp/spot 9.26×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
