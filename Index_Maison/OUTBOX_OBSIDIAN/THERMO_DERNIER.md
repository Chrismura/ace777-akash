# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-15T15:10Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `81/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82186.0 | prix |
| OI | 94153.05 | C13 |
| Funding | 2e-06 | C14 |
| Funding moy. ~30j | 3.407e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.738 | crowd |
| BTC 1h/4h/24h | 0.42 / 1.53 / 0.53 % | B7 |
| Dominance BTC | 59.42% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat CALME (score 81/100).
- Funding maintenant 2e-06. Moyenne ~30j 3.407e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.738.
- BTC 24h 0.53% · 1h 0.42% · 4h 1.53%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 948906$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.47 · OI 94153.05 (pas de dark pool free temps réel).
- Top traders L/S 1.804.
- Fear & Greed 53 (Neutral).
- Market cap crypto ≈ 2.77 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.42%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -12.43 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.619 · murC 95000 (+15.7%) · murP 78000 (-5.0%).
- Volumes cachés proxy : taker buy 0.507 · vol perp/spot 13.26×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
