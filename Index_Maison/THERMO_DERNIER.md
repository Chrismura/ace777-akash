# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-14T00:05Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `83/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83178.25 | prix |
| OI | 92536.881 | C13 |
| Funding | -9e-06 | C14 |
| Funding moy. ~30j | 3.627e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.29 | crowd |
| BTC 1h/4h/24h | 0.06 / -0.23 / 1.79 % | B7 |
| Dominance BTC | 59.24% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 83/100).
- Funding maintenant -9e-06. Moyenne ~30j 3.627e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.29.
- BTC 24h 1.79% · 1h 0.06% · 4h -0.23%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 740189$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.546 · OI 92536.881 (pas de dark pool free temps réel).
- Top traders L/S 1.349.
- Fear & Greed 62 (Greed).
- Market cap crypto ≈ 2.81 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.24%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -96.54 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.587 · murC 95000 (+14.2%) · murP 78000 (-6.2%).
- Volumes cachés proxy : taker buy 0.467 · vol perp/spot 12.58×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
