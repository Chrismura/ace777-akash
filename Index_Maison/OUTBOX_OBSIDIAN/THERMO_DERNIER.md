# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-19T04:54Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `67/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80983.81 | prix |
| OI | 108025.861 | C13 |
| Funding | 6.9e-05 | C14 |
| Funding moy. ~30j | 6.793e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 0.939 | crowd |
| BTC 1h/4h/24h | -0.15 / -0.81 / 4.61 % | B7 |
| Dominance BTC | 58.36% | A3 |
| Alts ↓ 24h | 10.0% | B9 |

## Lecture
- Climat ATTENTION (score 67/100).
- Funding maintenant 6.9e-05. Moyenne ~30j 6.793e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 0.939.
- BTC 24h 4.61% · 1h -0.15% · 4h -0.81%.
- Panier alts : 10.0% en baisse (2/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.771 · OI 108025.861 (pas de dark pool free temps réel).
- Top traders L/S 1.072.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.78 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.36%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -118.88 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.559 · murC 85000 (+5.0%) · murP 70000 (-13.6%).
- Volumes cachés proxy : taker buy 0.496 · vol perp/spot 13.11×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
