# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-03T23:56Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `93/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84703.7 | prix |
| OI | 97290.301 | C13 |
| Funding | -1.3e-05 | C14 |
| Funding moy. ~30j | 4.794e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.217 | crowd |
| BTC 1h/4h/24h | -0.03 / -0.11 / 0.26 % | B7 |
| Dominance BTC | 58.61% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat CALME (score 93/100).
- Funding maintenant -1.3e-05. Moyenne ~30j 4.794e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.217.
- BTC 24h 0.26% · 1h -0.03% · 4h -0.11%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.265 · OI 97290.301 (pas de dark pool free temps réel).
- Top traders L/S 1.247.
- Fear & Greed 67 (Greed).
- Market cap crypto ≈ 2.90 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.61%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 8.17 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.51 · murC 95000 (+12.1%) · murP 75000 (-11.5%).
- Volumes cachés proxy : taker buy 0.491 · vol perp/spot 7.94×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
