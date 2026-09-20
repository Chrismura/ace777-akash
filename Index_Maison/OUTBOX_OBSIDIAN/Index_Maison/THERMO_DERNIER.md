# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-20T05:59Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `85/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80493.18 | prix |
| OI | 109065.971 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 6.856e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 0.917 | crowd |
| BTC 1h/4h/24h | 0.09 / -0.72 / -0.62 % | B7 |
| Dominance BTC | 58.96% | A3 |
| Alts ↓ 24h | 50.0% | B9 |

## Lecture
- Climat CALME (score 85/100).
- Funding maintenant 0.0001. Moyenne ~30j 6.856e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 0.917.
- BTC 24h -0.62% · 1h 0.09% · 4h -0.72%.
- Panier alts : 50.0% en baisse (10/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 3478338$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.929 · OI 109065.971 (pas de dark pool free temps réel).
- Top traders L/S 1.069.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.74 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.96%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -118.16 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.563 · murC 85000 (+5.6%) · murP 70000 (-13.0%).
- Volumes cachés proxy : taker buy 0.532 · vol perp/spot 11.68×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
