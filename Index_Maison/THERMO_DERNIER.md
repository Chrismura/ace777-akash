# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-18T23:51Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `62/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80924.0 | prix |
| OI | 107920.677 | C13 |
| Funding | 6.3e-05 | C14 |
| Funding moy. ~30j | 6.827e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 0.913 | crowd |
| BTC 1h/4h/24h | -0.21 / -0.29 / 5.91 % | B7 |
| Dominance BTC | 58.35% | A3 |
| Alts ↓ 24h | 15.0% | B9 |

## Lecture
- Climat ATTENTION (score 62/100).
- Funding maintenant 6.3e-05. Moyenne ~30j 6.827e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 0.913.
- BTC 24h 5.91% · 1h -0.21% · 4h -0.29%.
- Panier alts : 15.0% en baisse (3/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.011 · OI 107920.677 (pas de dark pool free temps réel).
- Top traders L/S 0.992.
- Fear & Greed 56 (Greed).
- Market cap crypto ≈ 2.78 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.35%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -101.69 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.557 · murC 85000 (+5.0%) · murP 70000 (-13.5%).
- Volumes cachés proxy : taker buy 0.496 · vol perp/spot 13.09×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
