# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-21T23:00Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `59/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78444.6 | prix |
| OI | 106373.639 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.696e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.059 | crowd |
| BTC 1h/4h/24h | -0.03 / 1.84 / 7.93 % | B7 |
| Dominance BTC | 58.98% | A3 |
| Alts ↓ 24h | 10.0% | B9 |

## Lecture
- Climat ATTENTION (score 59/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.696e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.059.
- BTC 24h 7.93% · 1h -0.03% · 4h 1.84%.
- Panier alts : 10.0% en baisse (2/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 709285$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.482 · OI 106373.639 (pas de dark pool free temps réel).
- Top traders L/S 1.098.
- Fear & Greed 72 (Greed).
- Market cap crypto ≈ 2.67 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.98%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 1007.28 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.615 · murC 80000 (+2.0%) · murP 60000 (-23.5%).
- Volumes cachés proxy : taker buy 0.534 · vol perp/spot 13.33×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1385 · heat=100.0 · PnL sess=309.7943 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
