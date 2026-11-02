# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-11-02T11:20Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `66/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77846.6 | prix |
| OI | 95691.483 | C13 |
| Funding | 8.8e-05 | C14 |
| Funding moy. ~30j | 4.617e-05 (n=90) | Cortana |
| Funding mois préc. | 4.436e-05 (n=93) | Cortana |
| L/S 1h | 2.111 | crowd |
| BTC 1h/4h/24h | -0.13 / -0.3 / -0.16 % | B7 |
| Dominance BTC | 59.95% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat ATTENTION (score 66/100).
- Funding maintenant 8.8e-05. Moyenne ~30j 4.617e-05 (90 pts). Mois précédent 4.436e-05 (93 pts).
- Long/Short 2.111.
- BTC 24h -0.16% · 1h -0.13% · 4h -0.3%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 1564951$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.055 · OI 95691.483 (pas de dark pool free temps réel).
- Top traders L/S 2.26.
- Fear & Greed 37 (Fear).
- Market cap crypto ≈ 2.60 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.95%).
- Liquidations 24h proxy ≈ 1.54 M$.
- ETF net inflow : BTC 63.26 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.668 · murC 90000 (+15.7%) · murP 60000 (-22.8%).
- Volumes cachés proxy : taker buy 0.528 · vol perp/spot 9.95×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
