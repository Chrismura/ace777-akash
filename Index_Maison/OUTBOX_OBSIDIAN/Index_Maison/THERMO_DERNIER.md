# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-31T11:57Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `58/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77612.9 | prix |
| OI | 96930.873 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.251e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 2.654 | crowd |
| BTC 1h/4h/24h | 0.3 / 0.37 / 0.5 % | B7 |
| Dominance BTC | 59.84% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat ATTENTION (score 58/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.251e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 2.654.
- BTC 24h 0.5% · 1h 0.3% · 4h 0.37%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 837799$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.804 · OI 96930.873 (pas de dark pool free temps réel).
- Top traders L/S 2.842.
- Fear & Greed 30 (Fear).
- Market cap crypto ≈ 2.60 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.84%).
- Liquidations 24h proxy ≈ 1.31 M$.
- ETF net inflow : BTC 26.09 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.67 · murC 90000 (+16.1%) · murP 74000 (-4.5%).
- Volumes cachés proxy : taker buy 0.509 · vol perp/spot 7.43×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
