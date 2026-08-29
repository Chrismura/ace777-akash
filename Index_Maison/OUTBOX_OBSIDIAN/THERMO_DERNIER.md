# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-29T06:03Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `71/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77540.2 | prix |
| OI | 106427.991 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 6.523e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.174 | crowd |
| BTC 1h/4h/24h | -0.09 / -0.13 / -2.81 % | B7 |
| Dominance BTC | 58.95% | A3 |
| Alts ↓ 24h | 65.0% | B9 |

## Lecture
- Climat CALME (score 71/100).
- Funding maintenant 0.0001. Moyenne ~30j 6.523e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.174.
- BTC 24h -2.81% · 1h -0.09% · 4h -0.13%.
- Panier alts : 65.0% en baisse (13/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 826962$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.217 · OI 106427.991 (pas de dark pool free temps réel).
- Top traders L/S 1.23.
- Fear & Greed 68 (Greed).
- Market cap crypto ≈ 2.64 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.95%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 212.5 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.581 · murC 82000 (+5.7%) · murP 70000 (-9.8%).
- Volumes cachés proxy : taker buy 0.495 · vol perp/spot 14.64×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
