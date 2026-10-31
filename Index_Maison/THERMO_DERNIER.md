# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-31T21:56Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `55/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77579.8 | prix |
| OI | 97034.288 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.284e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.578 | crowd |
| BTC 1h/4h/24h | 0.08 / -0.11 / 1.12 % | B7 |
| Dominance BTC | 59.22% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat ATTENTION (score 55/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.284e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.578.
- BTC 24h 1.12% · 1h 0.08% · 4h -0.11%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.267 · OI 97034.288 (pas de dark pool free temps réel).
- Top traders L/S 2.74.
- Fear & Greed 30 (Fear).
- Market cap crypto ≈ 2.63 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.22%).
- Liquidations 24h proxy ≈ 2.29 M$.
- ETF net inflow : BTC 26.07 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.677 · murC 90000 (+16.1%) · murP 74000 (-4.5%).
- Volumes cachés proxy : taker buy 0.537 · vol perp/spot 7.04×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
