# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-14T03:26Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `71/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63476.3 | prix |
| OI | 109752.499 | C13 |
| Funding | 9.2e-05 | C14 |
| Funding moy. ~30j | 5.508e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.867 | crowd |
| BTC 1h/4h/24h | 0.06 / 0.03 / -0.17 % | B7 |
| Dominance BTC | 56.25% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 71/100).
- Funding maintenant 9.2e-05. Moyenne ~30j 5.508e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.867.
- BTC 24h -0.17% · 1h 0.06% · 4h 0.03%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 646956$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.607 · OI 109752.499 (pas de dark pool free temps réel).
- Top traders L/S 1.925.
- Fear & Greed 29 (Fear).
- Market cap crypto ≈ 2.27 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.25%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC -82.52 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.551 · murC 70000 (+10.4%) · murP 60000 (-5.4%).
- Volumes cachés proxy : taker buy 0.544 · vol perp/spot 11.38×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1125 · heat=100.0 · PnL sess=115.7714 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
