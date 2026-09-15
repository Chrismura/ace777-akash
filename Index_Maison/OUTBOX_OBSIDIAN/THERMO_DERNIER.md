# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-15T09:33Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `75/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 76885.8 | prix |
| OI | 104760.636 | C13 |
| Funding | 7.3e-05 | C14 |
| Funding moy. ~30j | 6.704e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.528 | crowd |
| BTC 1h/4h/24h | -0.1 / -0.91 / -1.15 % | B7 |
| Dominance BTC | 58.31% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 75/100).
- Funding maintenant 7.3e-05. Moyenne ~30j 6.704e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.528.
- BTC 24h -1.15% · 1h -0.1% · 4h -0.91%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 760325$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.046 · OI 104760.636 (pas de dark pool free temps réel).
- Top traders L/S 1.621.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.64 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.31%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -59.59 M$ (bitbo-public (moy 7j), BTC only).
- Volumes cachés proxy : taker buy 0.511 · vol perp/spot 13.36×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
