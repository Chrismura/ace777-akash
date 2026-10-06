# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-06T01:39Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `91/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 85769.8 | prix |
| OI | 94522.098 | C13 |
| Funding | -1.8e-05 | C14 |
| Funding moy. ~30j | 4.657e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.08 | crowd |
| BTC 1h/4h/24h | -0.12 / -0.16 / -1.06 % | B7 |
| Dominance BTC | 58.72% | A3 |
| Alts ↓ 24h | 65.0% | B9 |

## Lecture
- Climat CALME (score 91/100).
- Funding maintenant -1.8e-05. Moyenne ~30j 4.657e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.08.
- BTC 24h -1.06% · 1h -0.12% · 4h -0.16%.
- Panier alts : 65.0% en baisse (13/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.952 · OI 94522.098 (pas de dark pool free temps réel).
- Top traders L/S 1.177.
- Fear & Greed 73 (Greed).
- Market cap crypto ≈ 2.94 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.72%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 23.99 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.52 · murC 95000 (+10.7%) · murP 80000 (-6.8%).
- Volumes cachés proxy : taker buy 0.502 · vol perp/spot 12.16×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
