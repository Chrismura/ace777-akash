# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-04T20:55Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `86/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 85767.56 | prix |
| OI | 98543.802 | C13 |
| Funding | 4.4e-05 | C14 |
| Funding moy. ~30j | 4.643e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.13 | crowd |
| BTC 1h/4h/24h | 0.46 / 0.53 / 1.25 % | B7 |
| Dominance BTC | 59.25% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat CALME (score 86/100).
- Funding maintenant 4.4e-05. Moyenne ~30j 4.643e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.13.
- BTC 24h 1.25% · 1h 0.46% · 4h 0.53%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 502258$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.311 · OI 98543.802 (pas de dark pool free temps réel).
- Top traders L/S 1.165.
- Fear & Greed 65 (Greed).
- Market cap crypto ≈ 2.91 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.25%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 8.27 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.517 · murC 95000 (+10.7%) · murP 80000 (-6.8%).
- Volumes cachés proxy : taker buy 0.486 · vol perp/spot 15.05×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
