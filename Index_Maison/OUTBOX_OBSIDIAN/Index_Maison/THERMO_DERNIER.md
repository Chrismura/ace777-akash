# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-01T05:16Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `82/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78836.21 | prix |
| OI | 108182.717 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 6.793e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.019 | crowd |
| BTC 1h/4h/24h | 0.17 / 0.58 / 1.43 % | B7 |
| Dominance BTC | 59.21% | A3 |
| Alts ↓ 24h | 5.0% | B9 |

## Lecture
- Climat CALME (score 82/100).
- Funding maintenant 0.0001. Moyenne ~30j 6.793e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.019.
- BTC 24h 1.43% · 1h 0.17% · 4h 0.58%.
- Panier alts : 5.0% en baisse (1/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 550539$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.961 · OI 108182.717 (pas de dark pool free temps réel).
- Top traders L/S 1.095.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.67 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.21%).
- Liquidations 24h proxy ≈ 0.03 B$.
- ETF net inflow : BTC 120.96 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.571 · murC 82000 (+4.0%) · murP 70000 (-11.2%).
- Volumes cachés proxy : taker buy 0.502 · vol perp/spot 12.54×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
