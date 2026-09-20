# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-20T00:57Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `88/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81254.7 | prix |
| OI | 107494.346 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 6.856e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 0.942 | crowd |
| BTC 1h/4h/24h | 0.04 / 0.15 / -0.22 % | B7 |
| Dominance BTC | 58.87% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 88/100).
- Funding maintenant 0.0001. Moyenne ~30j 6.856e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 0.942.
- BTC 24h -0.22% · 1h 0.04% · 4h 0.15%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 915080$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.102 · OI 107494.346 (pas de dark pool free temps réel).
- Top traders L/S 1.094.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.77 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.87%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -119.28 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.563 · murC 85000 (+4.6%) · murP 70000 (-13.9%).
- Volumes cachés proxy : taker buy 0.532 · vol perp/spot 9.8×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
