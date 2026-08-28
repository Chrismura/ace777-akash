# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-28T00:14Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `83/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80192.5 | prix |
| OI | 108779.278 | C13 |
| Funding | 6.2e-05 | C14 |
| Funding moy. ~30j | 6.481e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 0.92 | crowd |
| BTC 1h/4h/24h | -0.04 / 0.14 / 1.78 % | B7 |
| Dominance BTC | 59.22% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 83/100).
- Funding maintenant 6.2e-05. Moyenne ~30j 6.481e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 0.92.
- BTC 24h 1.78% · 1h -0.04% · 4h 0.14%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 688443$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.037 · OI 108779.278 (pas de dark pool free temps réel).
- Top traders L/S 0.998.
- Fear & Greed 73 (Greed).
- Market cap crypto ≈ 2.71 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.22%).
- Liquidations 24h proxy ≈ 0.04 B$.
- ETF net inflow : BTC 144.76 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.636 · murC 82000 (+2.1%) · murP 70000 (-12.8%).
- Volumes cachés proxy : taker buy 0.496 · vol perp/spot 13.56×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
