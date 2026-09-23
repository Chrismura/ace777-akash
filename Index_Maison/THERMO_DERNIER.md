# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-23T03:15Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `88/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 86478.6 | prix |
| OI | 106751.912 | C13 |
| Funding | 3.6e-05 | C14 |
| Funding moy. ~30j | 6.554e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 0.896 | crowd |
| BTC 1h/4h/24h | -0.03 / 0.37 / 1.13 % | B7 |
| Dominance BTC | 58.7% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat CALME (score 88/100).
- Funding maintenant 3.6e-05. Moyenne ~30j 6.554e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 0.896.
- BTC 24h 1.13% · 1h -0.03% · 4h 0.37%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.011 · OI 106751.912 (pas de dark pool free temps réel).
- Top traders L/S 0.988.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.95 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.7%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 35.67 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.558 · murC 95000 (+9.8%) · murP 70000 (-19.1%).
- Volumes cachés proxy : taker buy 0.555 · vol perp/spot 12.13×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
