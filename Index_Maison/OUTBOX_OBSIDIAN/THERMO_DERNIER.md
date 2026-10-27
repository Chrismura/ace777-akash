# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-27T17:23Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `64/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80692.69 | prix |
| OI | 96866.443 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 3.849e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.141 | crowd |
| BTC 1h/4h/24h | 0.08 / 0.84 / 0.36 % | B7 |
| Dominance BTC | 59.4% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat ATTENTION (score 64/100).
- Funding maintenant 0.0001. Moyenne ~30j 3.849e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.141.
- BTC 24h 0.36% · 1h 0.08% · 4h 0.84%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 1692655$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.83 · OI 96866.443 (pas de dark pool free temps réel).
- Top traders L/S 2.255.
- Fear & Greed 48 (Neutral).
- Market cap crypto ≈ 2.72 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.4%).
- Liquidations 24h proxy ≈ 2.06 M$.
- ETF net inflow : BTC 71.02 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.592 · murC 95000 (+17.8%) · murP 75000 (-7.0%).
- Volumes cachés proxy : taker buy 0.513 · vol perp/spot 17.73×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
