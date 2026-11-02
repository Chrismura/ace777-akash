# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-11-02T16:22Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `60/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77324.4 | prix |
| OI | 97469.443 | C13 |
| Funding | 9.3e-05 | C14 |
| Funding moy. ~30j | 4.668e-05 (n=90) | Cortana |
| Funding mois préc. | 4.469e-05 (n=93) | Cortana |
| L/S 1h | 2.226 | crowd |
| BTC 1h/4h/24h | -0.22 / -0.6 / -0.84 % | B7 |
| Dominance BTC | 59.26% | A3 |
| Alts ↓ 24h | 70.0% | B9 |

## Lecture
- Climat ATTENTION (score 60/100).
- Funding maintenant 9.3e-05. Moyenne ~30j 4.668e-05 (90 pts). Mois précédent 4.469e-05 (93 pts).
- Long/Short 2.226.
- BTC 24h -0.84% · 1h -0.22% · 4h -0.6%.
- Panier alts : 70.0% en baisse (14/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 831041$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.863 · OI 97469.443 (pas de dark pool free temps réel).
- Top traders L/S 2.39.
- Fear & Greed 37 (Fear).
- Market cap crypto ≈ 2.61 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.26%).
- Liquidations 24h proxy ≈ 2.20 M$.
- ETF net inflow : BTC 62.84 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.686 · murC 90000 (+16.5%) · murP 72000 (-6.8%).
- Volumes cachés proxy : taker buy 0.577 · vol perp/spot 10.82×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
