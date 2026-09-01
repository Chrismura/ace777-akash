# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-01T13:23Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `91/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77738.7 | prix |
| OI | 109154.924 | C13 |
| Funding | 4.4e-05 | C14 |
| Funding moy. ~30j | 6.805e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.143 | crowd |
| BTC 1h/4h/24h | -0.28 / -0.17 / -0.3 % | B7 |
| Dominance BTC | 59.11% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 91/100).
- Funding maintenant 4.4e-05. Moyenne ~30j 6.805e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.143.
- BTC 24h -0.3% · 1h -0.28% · 4h -0.17%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 639012$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.879 · OI 109154.924 (pas de dark pool free temps réel).
- Top traders L/S 1.226.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.64 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.11%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 189.81 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.563 · murC 82000 (+5.5%) · murP 70000 (-10.0%).
- Volumes cachés proxy : taker buy 0.502 · vol perp/spot 13.04×.
- ACE soft: LIVE=ACE_DUO_PREFLIGHT_10M_LIVE_COLOR.log · SKIP=110 · heat=0.4 · PnL sess=-0.1177 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
