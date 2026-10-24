# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-24T13:23Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `62/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80717.23 | prix |
| OI | 94576.302 | C13 |
| Funding | 4.4e-05 | C14 |
| Funding moy. ~30j | 3.229e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 2.234 | crowd |
| BTC 1h/4h/24h | -0.04 / 0.16 / -1.3 % | B7 |
| Dominance BTC | 59.56% | A3 |
| Alts ↓ 24h | 65.0% | B9 |

## Lecture
- Climat ATTENTION (score 62/100).
- Funding maintenant 4.4e-05. Moyenne ~30j 3.229e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 2.234.
- BTC 24h -1.3% · 1h -0.04% · 4h 0.16%.
- Panier alts : 65.0% en baisse (13/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.311 · OI 94576.302 (pas de dark pool free temps réel).
- Top traders L/S 2.326.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.72 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.56%).
- Liquidations 24h proxy ≈ 1.62 M$.
- ETF net inflow : BTC 64.37 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.566 · murC 95000 (+17.8%) · murP 75000 (-7.0%).
- Volumes cachés proxy : taker buy 0.505 · vol perp/spot 16.81×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
