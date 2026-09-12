# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-12T23:33Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `81/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77220.86 | prix |
| OI | 103267.722 | C13 |
| Funding | 4.3e-05 | C14 |
| Funding moy. ~30j | 6.602e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.649 | crowd |
| BTC 1h/4h/24h | 0.03 / 0.18 / 0.06 % | B7 |
| Dominance BTC | 58.23% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat CALME (score 81/100).
- Funding maintenant 4.3e-05. Moyenne ~30j 6.602e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.649.
- BTC 24h 0.06% · 1h 0.03% · 4h 0.18%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.044 · OI 103267.722 (pas de dark pool free temps réel).
- Top traders L/S 1.722.
- Fear & Greed 63 (Greed).
- Market cap crypto ≈ 2.66 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.23%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 75.32 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.556 · murC 90000 (+16.5%) · murP 70000 (-9.4%).
- Volumes cachés proxy : taker buy 0.484 · vol perp/spot 10.93×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
