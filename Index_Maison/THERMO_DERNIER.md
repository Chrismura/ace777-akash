# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-27T23:12Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `93/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84151.17 | prix |
| OI | 94342.332 | C13 |
| Funding | 2.9e-05 | C14 |
| Funding moy. ~30j | 5.593e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.163 | crowd |
| BTC 1h/4h/24h | -0.01 / -0.65 / -0.18 % | B7 |
| Dominance BTC | 58.76% | A3 |
| Alts ↓ 24h | 65.0% | B9 |

## Lecture
- Climat CALME (score 93/100).
- Funding maintenant 2.9e-05. Moyenne ~30j 5.593e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.163.
- BTC 24h -0.18% · 1h -0.01% · 4h -0.65%.
- Panier alts : 65.0% en baisse (13/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.987 · OI 94342.332 (pas de dark pool free temps réel).
- Top traders L/S 1.248.
- Fear & Greed 70 (Greed).
- Market cap crypto ≈ 2.87 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.76%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 291.65 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.46 · murC 95000 (+12.9%) · murP 75000 (-10.9%).
- Volumes cachés proxy : taker buy 0.492 · vol perp/spot 14.05×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
