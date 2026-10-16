# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-16T22:02Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `69/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81715.4 | prix |
| OI | 94555.683 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 3.369e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.726 | crowd |
| BTC 1h/4h/24h | 0.09 / 0.75 / -0.96 % | B7 |
| Dominance BTC | 59.4% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat ATTENTION (score 69/100).
- Funding maintenant 0.0001. Moyenne ~30j 3.369e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.726.
- BTC 24h -0.96% · 1h 0.09% · 4h 0.75%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 1403572$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.163 · OI 94555.683 (pas de dark pool free temps réel).
- Top traders L/S 1.87.
- Fear & Greed 63 (Greed).
- Market cap crypto ≈ 2.76 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.4%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -18.58 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.589 · murC 95000 (+16.4%) · murP 80000 (-2.0%).
- Volumes cachés proxy : taker buy 0.537 · vol perp/spot 12.1×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
