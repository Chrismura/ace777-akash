# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-18T09:57Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `75/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 64159.32 | prix |
| OI | 105774.365 | C13 |
| Funding | 6.6e-05 | C14 |
| Funding moy. ~30j | 5.474e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.516 | crowd |
| BTC 1h/4h/24h | -0.17 / -0.08 / 1.36 % | B7 |
| Dominance BTC | 56.51% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 75/100).
- Funding maintenant 6.6e-05. Moyenne ~30j 5.474e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.516.
- BTC 24h 1.36% · 1h -0.17% · 4h -0.08%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 813726$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.218 · OI 105774.365 (pas de dark pool free temps réel).
- Top traders L/S 1.644.
- Fear & Greed 41 (Fear).
- Market cap crypto ≈ 2.28 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.51%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC -86.27 M$ (bitbo-public (moy 7j), BTC only).
- Volumes cachés proxy : taker buy 0.555 · vol perp/spot 15.05×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=642 · heat=100.0 · PnL sess=214.0387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
