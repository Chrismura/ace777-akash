# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-20T05:56Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `70/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81823.2 | prix |
| OI | 94890.302 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 3.23e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.687 | crowd |
| BTC 1h/4h/24h | -0.29 / 0.07 / -1.06 % | B7 |
| Dominance BTC | 59.58% | A3 |
| Alts ↓ 24h | 70.0% | B9 |

## Lecture
- Climat CALME (score 70/100).
- Funding maintenant 0.0001. Moyenne ~30j 3.23e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.687.
- BTC 24h -1.06% · 1h -0.29% · 4h 0.07%.
- Panier alts : 70.0% en baisse (14/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 736500$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.714 · OI 94890.302 (pas de dark pool free temps réel).
- Top traders L/S 1.783.
- Fear & Greed 55 (Greed).
- Market cap crypto ≈ 2.76 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.58%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -10.55 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.58 · murC 95000 (+16.2%) · murP 75000 (-8.3%).
- Volumes cachés proxy : taker buy 0.459 · vol perp/spot 13.81×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
