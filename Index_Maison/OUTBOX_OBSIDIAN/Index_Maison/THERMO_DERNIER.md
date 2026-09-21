# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-21T14:02Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `59/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 85468.5 | prix |
| OI | 111537.717 | C13 |
| Funding | 9.8e-05 | C14 |
| Funding moy. ~30j | 6.81e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 0.904 | crowd |
| BTC 1h/4h/24h | 0.03 / 1.25 / 5.99 % | B7 |
| Dominance BTC | 58.81% | A3 |
| Alts ↓ 24h | 15.0% | B9 |

## Lecture
- Climat ATTENTION (score 59/100).
- Funding maintenant 9.8e-05. Moyenne ~30j 6.81e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 0.904.
- BTC 24h 5.99% · 1h 0.03% · 4h 1.25%.
- Panier alts : 15.0% en baisse (3/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 967978$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.014 · OI 111537.717 (pas de dark pool free temps réel).
- Top traders L/S 0.976.
- Fear & Greed 70 (Greed).
- Market cap crypto ≈ 2.90 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.81%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -68.77 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.527 · murC 90000 (+5.3%) · murP 70000 (-18.1%).
- Volumes cachés proxy : taker buy 0.478 · vol perp/spot 12.46×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
