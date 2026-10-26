# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-26T07:45Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `62/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80084.9 | prix |
| OI | 94010.84 | C13 |
| Funding | 7.6e-05 | C14 |
| Funding moy. ~30j | 3.46e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 2.234 | crowd |
| BTC 1h/4h/24h | -0.01 / 0.65 / -0.73 % | B7 |
| Dominance BTC | 60.08% | A3 |
| Alts ↓ 24h | 50.0% | B9 |

## Lecture
- Climat ATTENTION (score 62/100).
- Funding maintenant 7.6e-05. Moyenne ~30j 3.46e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 2.234.
- BTC 24h -0.73% · 1h -0.01% · 4h 0.65%.
- Panier alts : 50.0% en baisse (10/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 1058046$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.774 · OI 94010.84 (pas de dark pool free temps réel).
- Top traders L/S 2.357.
- Fear & Greed 50 (Neutral).
- Market cap crypto ≈ 2.68 T$.
- Alt season proxy : Bitcoin season (BTC.D 60.08%).
- Liquidations 24h proxy ≈ 2.41 M$.
- ETF net inflow : BTC 30.35 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.595 · murC 95000 (+18.8%) · murP 75000 (-6.2%).
- Volumes cachés proxy : taker buy 0.481 · vol perp/spot 17.33×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
