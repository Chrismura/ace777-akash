# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-01T19:26Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `78/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77357.48 | prix |
| OI | 109171.859 | C13 |
| Funding | 5.4e-05 | C14 |
| Funding moy. ~30j | 6.762e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.248 | crowd |
| BTC 1h/4h/24h | 0.3 / -0.67 / -2.1 % | B7 |
| Dominance BTC | 59.08% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 78/100).
- Funding maintenant 5.4e-05. Moyenne ~30j 6.762e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.248.
- BTC 24h -2.1% · 1h 0.3% · 4h -0.67%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.802 · OI 109171.859 (pas de dark pool free temps réel).
- Top traders L/S 1.359.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.63 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.08%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 188.88 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.562 · murC 82000 (+6.0%) · murP 70000 (-9.5%).
- Volumes cachés proxy : taker buy 0.521 · vol perp/spot 16.79×.
- ACE soft: LIVE=ACE_DUO_CLEAN_V4_15M_LIVE_COLOR.log · SKIP=228 · heat=11.9 · PnL sess=-3.9801 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
