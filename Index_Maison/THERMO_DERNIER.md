# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-12T17:56Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `74/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63456.1 | prix |
| OI | 110889.165 | C13 |
| Funding | 8.3e-05 | C14 |
| Funding moy. ~30j | 5.477e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.748 | crowd |
| BTC 1h/4h/24h | -0.01 / -0.55 / -0.24 % | B7 |
| Dominance BTC | 56.2% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 74/100).
- Funding maintenant 8.3e-05. Moyenne ~30j 5.477e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.748.
- BTC 24h -0.24% · 1h -0.01% · 4h -0.55%.
- Panier alts : 40.0% en baisse (2/5).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.031 · OI 110889.165 (pas de dark pool free temps réel).
- Top traders L/S 1.81.
- Fear & Greed 27 (Fear).
- Market cap crypto ≈ 2.26 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.2%).
- Liquidations 24h proxy ≈ 0.02 B$.
- ETF net inflow : BTC 37.19 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.552 · murC 70000 (+10.4%) · murP 60000 (-5.4%).
- Volumes cachés proxy : taker buy 0.494 · vol perp/spot 11.9×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1167 · heat=100.0 · PnL sess=115.558 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
