# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-20T00:37Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `60/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 69522.6 | prix |
| OI | 107527.117 | C13 |
| Funding | 9.1e-05 | C14 |
| Funding moy. ~30j | 5.49e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.077 | crowd |
| BTC 1h/4h/24h | 0.31 / 0.73 / 7.59 % | B7 |
| Dominance BTC | 56.67% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat ATTENTION (score 60/100).
- Funding maintenant 9.1e-05. Moyenne ~30j 5.49e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.077.
- BTC 24h 7.59% · 1h 0.31% · 4h 0.73%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 3823500$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.129 · OI 107527.117 (pas de dark pool free temps réel).
- Top traders L/S 1.127.
- Fear & Greed 62 (Greed).
- Market cap crypto ≈ 2.47 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.67%).
- Liquidations 24h proxy ≈ 0.06 B$.
- ETF net inflow : BTC -43.32 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.559 · murC 70000 (+0.7%) · murP 60000 (-13.7%).
- Volumes cachés proxy : taker buy 0.493 · vol perp/spot 12.97×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=458 · heat=100.0 · PnL sess=238.567 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
