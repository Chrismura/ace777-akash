# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-14T03:31Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `74/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77741.92 | prix |
| OI | 106526.972 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 6.622e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.601 | crowd |
| BTC 1h/4h/24h | 0.2 / 1.22 / 0.69 % | B7 |
| Dominance BTC | 58.92% | A3 |
| Alts ↓ 24h | 70.0% | B9 |

## Lecture
- Climat CALME (score 74/100).
- Funding maintenant 0.0001. Moyenne ~30j 6.622e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.601.
- BTC 24h 0.69% · 1h 0.2% · 4h 1.22%.
- Panier alts : 70.0% en baisse (14/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 533081$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.215 · OI 106526.972 (pas de dark pool free temps réel).
- Top traders L/S 1.646.
- Fear & Greed 57 (Greed).
- Market cap crypto ≈ 2.65 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.92%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -8.68 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.557 · murC 90000 (+15.8%) · murP 70000 (-9.9%).
- Volumes cachés proxy : taker buy 0.513 · vol perp/spot 14.7×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
