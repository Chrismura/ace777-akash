# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-01T17:18Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `84/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77474.48 | prix |
| OI | 109117.849 | C13 |
| Funding | 4.5e-05 | C14 |
| Funding moy. ~30j | 6.762e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.22 | crowd |
| BTC 1h/4h/24h | -0.09 / -0.7 / -1.31 % | B7 |
| Dominance BTC | 59.07% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 84/100).
- Funding maintenant 4.5e-05. Moyenne ~30j 6.762e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.22.
- BTC 24h -1.31% · 1h -0.09% · 4h -0.7%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.719 · OI 109117.849 (pas de dark pool free temps réel).
- Top traders L/S 1.317.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.63 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.07%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 189.16 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.563 · murC 82000 (+5.8%) · murP 70000 (-9.7%).
- Volumes cachés proxy : taker buy 0.521 · vol perp/spot 15.24×.
- ACE soft: LIVE=ACE_DUO_CLEAN_V4_15M_LIVE_COLOR.log · SKIP=228 · heat=11.9 · PnL sess=-3.9801 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
