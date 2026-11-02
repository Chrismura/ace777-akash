# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-11-02T17:25Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `57/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77285.66 | prix |
| OI | 97881.416 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.668e-05 (n=90) | Cortana |
| Funding mois préc. | 4.469e-05 (n=93) | Cortana |
| L/S 1h | 2.265 | crowd |
| BTC 1h/4h/24h | -0.27 / -0.83 / -1.03 % | B7 |
| Dominance BTC | 59.3% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat ATTENTION (score 57/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.668e-05 (90 pts). Mois précédent 4.469e-05 (93 pts).
- Long/Short 2.265.
- BTC 24h -1.03% · 1h -0.27% · 4h -0.83%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 538525$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.027 · OI 97881.416 (pas de dark pool free temps réel).
- Top traders L/S 2.432.
- Fear & Greed 37 (Fear).
- Market cap crypto ≈ 2.61 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.3%).
- Liquidations 24h proxy ≈ 1.76 M$.
- ETF net inflow : BTC 62.81 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.687 · murC 90000 (+16.6%) · murP 72000 (-6.7%).
- Volumes cachés proxy : taker buy 0.577 · vol perp/spot 10.88×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
