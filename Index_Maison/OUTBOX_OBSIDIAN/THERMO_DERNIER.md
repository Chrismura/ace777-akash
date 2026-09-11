# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-11T07:17Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `73/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77296.23 | prix |
| OI | 106858.742 | C13 |
| Funding | 7.6e-05 | C14 |
| Funding moy. ~30j | 6.729e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.637 | crowd |
| BTC 1h/4h/24h | 0.04 / 0.56 / -1.1 % | B7 |
| Dominance BTC | 58.5% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat CALME (score 73/100).
- Funding maintenant 7.6e-05. Moyenne ~30j 6.729e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.637.
- BTC 24h -1.1% · 1h 0.04% · 4h 0.56%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.228 · OI 106858.742 (pas de dark pool free temps réel).
- Top traders L/S 1.654.
- Fear & Greed 56 (Greed).
- Market cap crypto ≈ 2.65 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.5%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 75.39 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.538 · murC 90000 (+16.4%) · murP 70000 (-9.5%).
- Volumes cachés proxy : taker buy 0.447 · vol perp/spot 14.22×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
