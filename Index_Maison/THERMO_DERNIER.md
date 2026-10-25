# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-25T05:54Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `68/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80532.49 | prix |
| OI | 93360.158 | C13 |
| Funding | 6e-05 | C14 |
| Funding moy. ~30j | 3.326e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 2.161 | crowd |
| BTC 1h/4h/24h | -0.45 / -0.43 / -0.24 % | B7 |
| Dominance BTC | 59.46% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat ATTENTION (score 68/100).
- Funding maintenant 6e-05. Moyenne ~30j 3.326e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 2.161.
- BTC 24h -0.24% · 1h -0.45% · 4h -0.43%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.077 · OI 93360.158 (pas de dark pool free temps réel).
- Top traders L/S 2.291.
- Fear & Greed 54 (Neutral).
- Market cap crypto ≈ 2.71 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.46%).
- Liquidations 24h proxy ≈ 1.77 M$.
- ETF net inflow : BTC 64.22 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.594 · murC 95000 (+18.1%) · murP 75000 (-6.8%).
- Volumes cachés proxy : taker buy 0.536 · vol perp/spot 15.35×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
