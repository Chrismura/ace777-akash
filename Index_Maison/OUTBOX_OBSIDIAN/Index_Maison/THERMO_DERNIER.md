# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-01T14:19Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `91/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78184.9 | prix |
| OI | 108596.341 | C13 |
| Funding | 4.4e-05 | C14 |
| Funding moy. ~30j | 6.805e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.152 | crowd |
| BTC 1h/4h/24h | 0.18 / 0.25 / 0.28 % | B7 |
| Dominance BTC | 59.14% | A3 |
| Alts ↓ 24h | 50.0% | B9 |

## Lecture
- Climat CALME (score 91/100).
- Funding maintenant 4.4e-05. Moyenne ~30j 6.805e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.152.
- BTC 24h 0.28% · 1h 0.18% · 4h 0.25%.
- Panier alts : 50.0% en baisse (10/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 781238$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.995 · OI 108596.341 (pas de dark pool free temps réel).
- Top traders L/S 1.242.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.65 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.14%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 190.9 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.562 · murC 82000 (+4.9%) · murP 70000 (-10.5%).
- Volumes cachés proxy : taker buy 0.502 · vol perp/spot 13.4×.
- ACE soft: LIVE=ACE_DUO_CLEAN_V1_15M_LIVE_COLOR.log · SKIP=129 · heat=8.9 · PnL sess=-2.9614 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
