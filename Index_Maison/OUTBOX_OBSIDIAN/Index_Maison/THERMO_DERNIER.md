# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-09T01:21Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `67/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81593.9 | prix |
| OI | 93339.295 | C13 |
| Funding | 3.4e-05 | C14 |
| Funding moy. ~30j | 4.219e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.855 | crowd |
| BTC 1h/4h/24h | -0.22 / -0.09 / -2.0 % | B7 |
| Dominance BTC | 59.06% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat ATTENTION (score 67/100).
- Funding maintenant 3.4e-05. Moyenne ~30j 4.219e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.855.
- BTC 24h -2.0% · 1h -0.22% · 4h -0.09%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 1351315$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.32 · OI 93339.295 (pas de dark pool free temps réel).
- Top traders L/S 1.989.
- Fear & Greed 59 (Greed).
- Market cap crypto ≈ 2.78 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.06%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -19.78 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.599 · murC 95000 (+16.5%) · murP 80000 (-1.9%).
- Volumes cachés proxy : taker buy 0.504 · vol perp/spot 11.17×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
