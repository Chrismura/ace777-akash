# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-10T21:30Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `72/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64090.59 | prix |
| OI | 106571.817 | C13 |
| Funding | 6.8e-05 | C14 |
| Funding moy. ~30j | 5.445e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.589 | crowd |
| BTC 1h/4h/24h | -0.06 / 0.24 / -1.57 % | B7 |
| Dominance BTC | 56.52% | A3 |
| Alts ↓ 24h | 100.0% | B9 |

## Lecture
- Climat CALME (score 72/100).
- Funding maintenant 6.8e-05. Moyenne ~30j 5.445e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.589.
- BTC 24h -1.57% · 1h -0.06% · 4h 0.24%.
- Panier alts : 100.0% en baisse (5/5).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.588 · OI 106571.817 (pas de dark pool free temps réel).
- Top traders L/S 1.714.
- Fear & Greed 30 (Fear).
- Market cap crypto ≈ 2.27 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.52%).
- Liquidations 24h proxy ≈ 0.04 B$.
- ETF net inflow : BTC 68.18 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.587 · murC 70000 (+9.3%) · murP 60000 (-6.3%).
- Volumes cachés proxy : taker buy 0.489 · vol perp/spot 19.1×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
