# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-11-01T14:08Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `58/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78015.21 | prix |
| OI | 97127.481 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.366e-05 (n=90) | Cortana |
| Funding mois préc. | 4.436e-05 (n=93) | Cortana |
| L/S 1h | 2.318 | crowd |
| BTC 1h/4h/24h | 0.02 / 0.02 / 0.65 % | B7 |
| Dominance BTC | 59.29% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat ATTENTION (score 58/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.366e-05 (90 pts). Mois précédent 4.436e-05 (93 pts).
- Long/Short 2.318.
- BTC 24h 0.65% · 1h 0.02% · 4h 0.02%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 546858$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.985 · OI 97127.481 (pas de dark pool free temps réel).
- Top traders L/S 2.418.
- Fear & Greed 34 (Fear).
- Market cap crypto ≈ 2.64 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.29%).
- Liquidations 24h proxy ≈ 2.18 M$.
- ETF net inflow : BTC 58.87 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.66 · murC 90000 (+15.5%) · murP 60000 (-23.0%).
- Volumes cachés proxy : taker buy 0.537 · vol perp/spot 7.25×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
