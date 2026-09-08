# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-08T06:35Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `78/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78360.0 | prix |
| OI | 108149.241 | C13 |
| Funding | 8.6e-05 | C14 |
| Funding moy. ~30j | 6.72e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.212 | crowd |
| BTC 1h/4h/24h | -0.26 / -0.69 / -1.64 % | B7 |
| Dominance BTC | 58.98% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 78/100).
- Funding maintenant 8.6e-05. Moyenne ~30j 6.72e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.212.
- BTC 24h -1.64% · 1h -0.26% · 4h -0.69%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.044 · OI 108149.241 (pas de dark pool free temps réel).
- Top traders L/S 1.285.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.66 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.98%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 81.75 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.525 · murC 90000 (+14.8%) · murP 70000 (-10.7%).
- Volumes cachés proxy : taker buy 0.473 · vol perp/spot 13.68×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_6H00_LIVE_COLOR.log · SKIP=888 · heat=2.9 · PnL sess=-0.9802 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
