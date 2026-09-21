# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-21T21:02Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `64/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 86813.2 | prix |
| OI | 109000.152 | C13 |
| Funding | 4.7e-05 | C14 |
| Funding moy. ~30j | 6.76e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 0.911 | crowd |
| BTC 1h/4h/24h | -0.19 / 1.1 / 7.2 % | B7 |
| Dominance BTC | 59.01% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat ATTENTION (score 64/100).
- Funding maintenant 4.7e-05. Moyenne ~30j 6.76e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 0.911.
- BTC 24h 7.2% · 1h -0.19% · 4h 1.1%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.436 · OI 109000.152 (pas de dark pool free temps réel).
- Top traders L/S 0.971.
- Fear & Greed 70 (Greed).
- Market cap crypto ≈ 2.95 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.01%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -69.85 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.506 · murC 95000 (+9.4%) · murP 70000 (-19.4%).
- Volumes cachés proxy : taker buy 0.54 · vol perp/spot 11.93×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
