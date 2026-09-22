# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-22T02:01Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `59/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 85550.0 | prix |
| OI | 109060.362 | C13 |
| Funding | 8.5e-05 | C14 |
| Funding moy. ~30j | 6.734e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 0.868 | crowd |
| BTC 1h/4h/24h | -0.04 / -1.01 / 5.69 % | B7 |
| Dominance BTC | 58.79% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat ATTENTION (score 59/100).
- Funding maintenant 8.5e-05. Moyenne ~30j 6.734e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 0.868.
- BTC 24h 5.69% · 1h -0.04% · 4h -1.01%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 856438$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.526 · OI 109060.362 (pas de dark pool free temps réel).
- Top traders L/S 0.948.
- Fear & Greed 78 (Extreme Greed).
- Market cap crypto ≈ 2.92 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.79%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -21.9 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.516 · murC 95000 (+11.0%) · murP 70000 (-18.2%).
- Volumes cachés proxy : taker buy 0.54 · vol perp/spot 11.75×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
