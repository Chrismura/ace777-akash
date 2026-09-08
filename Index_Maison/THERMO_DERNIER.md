# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-08T09:37Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `80/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78629.71 | prix |
| OI | 108940.192 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 6.737e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.272 | crowd |
| BTC 1h/4h/24h | 0.29 / 0.09 / -0.91 % | B7 |
| Dominance BTC | 58.89% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 80/100).
- Funding maintenant 0.0001. Moyenne ~30j 6.737e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.272.
- BTC 24h -0.91% · 1h 0.29% · 4h 0.09%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 593312$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.077 · OI 108940.192 (pas de dark pool free temps réel).
- Top traders L/S 1.362.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.67 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.89%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 82.03 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.517 · murC 81000 (+3.0%) · murP 70000 (-11.0%).
- Volumes cachés proxy : taker buy 0.473 · vol perp/spot 12.67×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_6H00_LIVE_COLOR.log · SKIP=888 · heat=2.9 · PnL sess=-0.9802 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
