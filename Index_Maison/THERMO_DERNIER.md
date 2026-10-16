# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-16T21:05Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `71/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81610.97 | prix |
| OI | 94662.578 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 3.369e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.737 | crowd |
| BTC 1h/4h/24h | -0.11 / 0.52 / -0.62 % | B7 |
| Dominance BTC | 59.43% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat CALME (score 71/100).
- Funding maintenant 0.0001. Moyenne ~30j 3.369e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.737.
- BTC 24h -0.62% · 1h -0.11% · 4h 0.52%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 662558$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.163 · OI 94662.578 (pas de dark pool free temps réel).
- Top traders L/S 1.88.
- Fear & Greed 63 (Greed).
- Market cap crypto ≈ 2.75 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.43%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -18.56 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.589 · murC 95000 (+16.5%) · murP 80000 (-1.9%).
- Volumes cachés proxy : taker buy 0.537 · vol perp/spot 12.33×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
