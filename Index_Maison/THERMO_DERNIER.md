# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-11T20:17Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `87/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77384.98 | prix |
| OI | 103220.01 | C13 |
| Funding | 1.2e-05 | C14 |
| Funding moy. ~30j | 6.669e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.513 | crowd |
| BTC 1h/4h/24h | 0.17 / -0.63 / 0.15 % | B7 |
| Dominance BTC | 58.2% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat CALME (score 87/100).
- Funding maintenant 1.2e-05. Moyenne ~30j 6.669e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.513.
- BTC 24h 0.15% · 1h 0.17% · 4h -0.63%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 581160$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.087 · OI 103220.01 (pas de dark pool free temps réel).
- Top traders L/S 1.55.
- Fear & Greed 56 (Greed).
- Market cap crypto ≈ 2.67 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.2%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC 75.48 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.539 · murC 90000 (+16.3%) · murP 70000 (-9.6%).
- Volumes cachés proxy : taker buy 0.495 · vol perp/spot 14.4×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
