# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-29T01:41Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `74/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80571.2 | prix |
| OI | 95975.608 | C13 |
| Funding | 4.3e-05 | C14 |
| Funding moy. ~30j | 4.046e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.864 | crowd |
| BTC 1h/4h/24h | -0.62 / -0.94 / -0.46 % | B7 |
| Dominance BTC | 59.47% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat CALME (score 74/100).
- Funding maintenant 4.3e-05. Moyenne ~30j 4.046e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.864.
- BTC 24h -0.46% · 1h -0.62% · 4h -0.94%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1219102$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.721 · OI 95975.608 (pas de dark pool free temps réel).
- Top traders L/S 1.966.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.71 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.47%).
- Liquidations 24h proxy ≈ 2.47 M$.
- ETF net inflow : BTC -0.94 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.586 · murC 95000 (+18.0%) · murP 75000 (-6.8%).
- Volumes cachés proxy : taker buy 0.492 · vol perp/spot 13.83×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
