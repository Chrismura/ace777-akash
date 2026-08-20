# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-20T01:37Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `61/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 69505.0 | prix |
| OI | 107402.277 | C13 |
| Funding | 8.4e-05 | C14 |
| Funding moy. ~30j | 5.49e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.072 | crowd |
| BTC 1h/4h/24h | 0.17 / -0.26 / 7.87 % | B7 |
| Dominance BTC | 56.6% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat ATTENTION (score 61/100).
- Funding maintenant 8.4e-05. Moyenne ~30j 5.49e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.072.
- BTC 24h 7.87% · 1h 0.17% · 4h -0.26%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 3616397$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.144 · OI 107402.277 (pas de dark pool free temps réel).
- Top traders L/S 1.124.
- Fear & Greed 62 (Greed).
- Market cap crypto ≈ 2.46 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.6%).
- Liquidations 24h proxy ≈ 0.06 B$.
- ETF net inflow : BTC -43.31 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.561 · murC 70000 (+0.7%) · murP 60000 (-13.7%).
- Volumes cachés proxy : taker buy 0.493 · vol perp/spot 12.81×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=458 · heat=100.0 · PnL sess=238.567 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
