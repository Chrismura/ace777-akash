# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-30T10:46Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `45/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77557.29 | prix |
| OI | 95388.79 | C13 |
| Funding | 8.4e-05 | C14 |
| Funding moy. ~30j | 4.13e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 2.32 | crowd |
| BTC 1h/4h/24h | -0.13 / -1.35 / -3.36 % | B7 |
| Dominance BTC | 59.77% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat ATTENTION (score 45/100).
- Funding maintenant 8.4e-05. Moyenne ~30j 4.13e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 2.32.
- BTC 24h -3.36% · 1h -0.13% · 4h -1.35%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 4754306$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.785 · OI 95388.79 (pas de dark pool free temps réel).
- Top traders L/S 2.478.
- Fear & Greed 30 (Fear).
- Market cap crypto ≈ 2.61 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.77%).
- Liquidations 24h proxy ≈ 2.91 M$.
- ETF net inflow : BTC 21.15 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.711 · murC 90000 (+16.2%) · murP 60000 (-22.6%).
- Volumes cachés proxy : taker buy 0.526 · vol perp/spot 10.53×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
