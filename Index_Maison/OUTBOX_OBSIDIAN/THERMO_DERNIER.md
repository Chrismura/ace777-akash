# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-18T07:22Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `77/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77707.2 | prix |
| OI | 108315.421 | C13 |
| Funding | 7.2e-05 | C14 |
| Funding moy. ~30j | 6.816e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.358 | crowd |
| BTC 1h/4h/24h | 0.19 / 0.46 / 1.59 % | B7 |
| Dominance BTC | 58.05% | A3 |
| Alts ↓ 24h | 10.0% | B9 |

## Lecture
- Climat CALME (score 77/100).
- Funding maintenant 7.2e-05. Moyenne ~30j 6.816e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.358.
- BTC 24h 1.59% · 1h 0.19% · 4h 0.46%.
- Panier alts : 10.0% en baisse (2/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 660601$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.66 · OI 108315.421 (pas de dark pool free temps réel).
- Top traders L/S 1.425.
- Fear & Greed 56 (Greed).
- Market cap crypto ≈ 2.68 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.05%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -106.74 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.565 · murC 90000 (+15.9%) · murP 70000 (-9.9%).
- Volumes cachés proxy : taker buy 0.514 · vol perp/spot 12.38×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
