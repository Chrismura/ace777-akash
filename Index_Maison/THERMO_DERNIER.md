# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-22T22:02Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `50/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81513.16 | prix |
| OI | 95578.36 | C13 |
| Funding | 6e-05 | C14 |
| Funding moy. ~30j | 2.982e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 2.072 | crowd |
| BTC 1h/4h/24h | 0.08 / 0.21 / -3.74 % | B7 |
| Dominance BTC | 59.5% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat ATTENTION (score 50/100).
- Funding maintenant 6e-05. Moyenne ~30j 2.982e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 2.072.
- BTC 24h -3.74% · 1h 0.08% · 4h 0.21%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 869686$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.222 · OI 95578.36 (pas de dark pool free temps réel).
- Top traders L/S 2.222.
- Fear & Greed 68 (Greed).
- Market cap crypto ≈ 2.74 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.5%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 67.32 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.589 · murC 95000 (+16.7%) · murP 75000 (-7.9%).
- Volumes cachés proxy : taker buy 0.529 · vol perp/spot 14.79×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
