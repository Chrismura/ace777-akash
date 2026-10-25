# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-25T10:37Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `67/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80287.61 | prix |
| OI | 93268.971 | C13 |
| Funding | 7.2e-05 | C14 |
| Funding moy. ~30j | 3.354e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 2.07 | crowd |
| BTC 1h/4h/24h | -0.01 / -0.21 / -0.47 % | B7 |
| Dominance BTC | 60.13% | A3 |
| Alts ↓ 24h | 50.0% | B9 |

## Lecture
- Climat ATTENTION (score 67/100).
- Funding maintenant 7.2e-05. Moyenne ~30j 3.354e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 2.07.
- BTC 24h -0.47% · 1h -0.01% · 4h -0.21%.
- Panier alts : 50.0% en baisse (10/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 765247$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.711 · OI 93268.971 (pas de dark pool free temps réel).
- Top traders L/S 2.22.
- Fear & Greed 54 (Neutral).
- Market cap crypto ≈ 2.68 T$.
- Alt season proxy : Bitcoin season (BTC.D 60.13%).
- Liquidations 24h proxy ≈ 1.64 M$.
- ETF net inflow : BTC 64.03 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.592 · murC 95000 (+18.4%) · murP 75000 (-6.5%).
- Volumes cachés proxy : taker buy 0.536 · vol perp/spot 16.12×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
