# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-31T13:57Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `55/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77473.0 | prix |
| OI | 96879.062 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.251e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 2.638 | crowd |
| BTC 1h/4h/24h | -0.05 / 0.05 / 0.94 % | B7 |
| Dominance BTC | 59.27% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat ATTENTION (score 55/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.251e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 2.638.
- BTC 24h 0.94% · 1h -0.05% · 4h 0.05%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 534508$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.689 · OI 96879.062 (pas de dark pool free temps réel).
- Top traders L/S 2.801.
- Fear & Greed 30 (Fear).
- Market cap crypto ≈ 2.63 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.27%).
- Liquidations 24h proxy ≈ 0.89 M$.
- ETF net inflow : BTC 26.04 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.674 · murC 90000 (+16.3%) · murP 74000 (-4.4%).
- Volumes cachés proxy : taker buy 0.509 · vol perp/spot 7.66×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
