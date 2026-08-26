# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-26T06:23Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `81/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78891.6 | prix |
| OI | 106050.125 | C13 |
| Funding | 5.9e-05 | C14 |
| Funding moy. ~30j | 6.392e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.011 | crowd |
| BTC 1h/4h/24h | -0.25 / -0.27 / -2.36 % | B7 |
| Dominance BTC | 59.27% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 81/100).
- Funding maintenant 5.9e-05. Moyenne ~30j 6.392e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.011.
- BTC 24h -2.36% · 1h -0.25% · 4h -0.27%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 3847701$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.995 · OI 106050.125 (pas de dark pool free temps réel).
- Top traders L/S 1.055.
- Fear & Greed 65 (Greed).
- Market cap crypto ≈ 2.66 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.27%).
- Liquidations 24h proxy ≈ 0.03 B$.
- ETF net inflow : BTC 298.85 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.625 · murC 82000 (+3.9%) · murP 70000 (-11.3%).
- Volumes cachés proxy : taker buy 0.542 · vol perp/spot 13.02×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
