# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-26T22:30Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `59/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79913.99 | prix |
| OI | 95349.945 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 3.61e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.248 | crowd |
| BTC 1h/4h/24h | -0.2 / -0.06 / -0.69 % | B7 |
| Dominance BTC | 59.46% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat ATTENTION (score 59/100).
- Funding maintenant 0.0001. Moyenne ~30j 3.61e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.248.
- BTC 24h -0.69% · 1h -0.2% · 4h -0.06%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 504172$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.669 · OI 95349.945 (pas de dark pool free temps réel).
- Top traders L/S 2.361.
- Fear & Greed 50 (Neutral).
- Market cap crypto ≈ 2.69 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.46%).
- Liquidations 24h proxy ≈ 2.44 M$.
- ETF net inflow : BTC 30.29 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.596 · murC 95000 (+19.0%) · murP 75000 (-6.0%).
- Volumes cachés proxy : taker buy 0.5 · vol perp/spot 15.98×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
