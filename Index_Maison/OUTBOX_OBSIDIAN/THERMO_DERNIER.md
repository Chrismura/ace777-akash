# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-19T10:32Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `82/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64349.72 | prix |
| OI | 104946.496 | C13 |
| Funding | 4.2e-05 | C14 |
| Funding moy. ~30j | 5.404e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.581 | crowd |
| BTC 1h/4h/24h | -0.07 / 0.05 / 0.29 % | B7 |
| Dominance BTC | 56.48% | A3 |
| Alts ↓ 24h | 65.0% | B9 |

## Lecture
- Climat CALME (score 82/100).
- Funding maintenant 4.2e-05. Moyenne ~30j 5.404e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.581.
- BTC 24h 0.29% · 1h -0.07% · 4h 0.05%.
- Panier alts : 65.0% en baisse (13/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 1287040$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.958 · OI 104946.496 (pas de dark pool free temps réel).
- Top traders L/S 1.688.
- Fear & Greed 46 (Fear).
- Market cap crypto ≈ 2.29 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.48%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -37.53 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.56 · murC 70000 (+8.8%) · murP 60000 (-6.7%).
- Volumes cachés proxy : taker buy 0.502 · vol perp/spot 14.53×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1133 · heat=100.0 · PnL sess=290.8596 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
