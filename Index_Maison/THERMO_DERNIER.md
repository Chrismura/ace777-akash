# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-17T17:09Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `71/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64054.26 | prix |
| OI | 107515.818 | C13 |
| Funding | 7.2e-05 | C14 |
| Funding moy. ~30j | 5.442e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.684 | crowd |
| BTC 1h/4h/24h | -0.04 / 0.64 / 1.28 % | B7 |
| Dominance BTC | 56.42% | A3 |
| Alts ↓ 24h | 5.0% | B9 |

## Lecture
- Climat CALME (score 71/100).
- Funding maintenant 7.2e-05. Moyenne ~30j 5.442e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.684.
- BTC 24h 1.28% · 1h -0.04% · 4h 0.64%.
- Panier alts : 5.0% en baisse (1/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 627366$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.744 · OI 107515.818 (pas de dark pool free temps réel).
- Top traders L/S 1.734.
- Fear & Greed 31 (Fear).
- Market cap crypto ≈ 2.28 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.42%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC -56.48 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.554 · murC 70000 (+9.3%) · murP 60000 (-6.3%).
- Volumes cachés proxy : taker buy 0.555 · vol perp/spot 17.6×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=964 · heat=100.0 · PnL sess=178.1499 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
