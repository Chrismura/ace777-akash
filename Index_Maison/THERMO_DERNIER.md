# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-01T18:25Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `78/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77070.9 | prix |
| OI | 109518.419 | C13 |
| Funding | 5.2e-05 | C14 |
| Funding moy. ~30j | 6.762e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.229 | crowd |
| BTC 1h/4h/24h | -0.22 / -1.36 / -2.27 % | B7 |
| Dominance BTC | 59.05% | A3 |
| Alts ↓ 24h | 65.0% | B9 |

## Lecture
- Climat CALME (score 78/100).
- Funding maintenant 5.2e-05. Moyenne ~30j 6.762e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.229.
- BTC 24h -2.27% · 1h -0.22% · 4h -1.36%.
- Panier alts : 65.0% en baisse (13/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.895 · OI 109518.419 (pas de dark pool free temps réel).
- Top traders L/S 1.327.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.62 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.05%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 188.18 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.565 · murC 82000 (+6.4%) · murP 70000 (-9.2%).
- Volumes cachés proxy : taker buy 0.521 · vol perp/spot 15.99×.
- ACE soft: LIVE=ACE_DUO_CLEAN_V4_15M_LIVE_COLOR.log · SKIP=228 · heat=11.9 · PnL sess=-3.9801 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
