# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-17T05:34Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `64/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63459.26 | prix |
| OI | 110313.651 | C13 |
| Funding | 9e-05 | C14 |
| Funding moy. ~30j | 5.375e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 2.076 | crowd |
| BTC 1h/4h/24h | -0.09 / 0.59 / 0.66 % | B7 |
| Dominance BTC | 56.22% | A3 |
| Alts ↓ 24h | 15.0% | B9 |

## Lecture
- Climat ATTENTION (score 64/100).
- Funding maintenant 9e-05. Moyenne ~30j 5.375e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 2.076.
- BTC 24h 0.66% · 1h -0.09% · 4h 0.59%.
- Panier alts : 15.0% en baisse (3/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 517776$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.223 · OI 110313.651 (pas de dark pool free temps réel).
- Top traders L/S 2.103.
- Fear & Greed 31 (Fear).
- Market cap crypto ≈ 2.26 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.22%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -55.95 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.558 · murC 70000 (+10.4%) · murP 60000 (-5.4%).
- Volumes cachés proxy : taker buy 0.488 · vol perp/spot 16.35×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1211 · heat=100.0 · PnL sess=181.9014 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
