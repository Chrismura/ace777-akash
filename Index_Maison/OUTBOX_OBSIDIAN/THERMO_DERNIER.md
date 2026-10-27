# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-27T03:36Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `60/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79888.46 | prix |
| OI | 96685.536 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 3.669e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 2.293 | crowd |
| BTC 1h/4h/24h | 0.12 / -0.29 / 0.35 % | B7 |
| Dominance BTC | 59.42% | A3 |
| Alts ↓ 24h | 15.0% | B9 |

## Lecture
- Climat ATTENTION (score 60/100).
- Funding maintenant 0.0001. Moyenne ~30j 3.669e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 2.293.
- BTC 24h 0.35% · 1h 0.12% · 4h -0.29%.
- Panier alts : 15.0% en baisse (3/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.751 · OI 96685.536 (pas de dark pool free temps réel).
- Top traders L/S 2.42.
- Fear & Greed 48 (Neutral).
- Market cap crypto ≈ 2.69 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.42%).
- Liquidations 24h proxy ≈ 2.32 M$.
- ETF net inflow : BTC -54.75 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.597 · murC 95000 (+19.1%) · murP 75000 (-6.0%).
- Volumes cachés proxy : taker buy 0.5 · vol perp/spot 16.03×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
