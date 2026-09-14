# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-14T21:32Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `82/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78910.03 | prix |
| OI | 104346.114 | C13 |
| Funding | 3.3e-05 | C14 |
| Funding moy. ~30j | 6.627e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.165 | crowd |
| BTC 1h/4h/24h | -0.22 / -0.03 / 2.0 % | B7 |
| Dominance BTC | 58.47% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 82/100).
- Funding maintenant 3.3e-05. Moyenne ~30j 6.627e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.165.
- BTC 24h 2.0% · 1h -0.22% · 4h -0.03%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1061978$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.191 · OI 104346.114 (pas de dark pool free temps réel).
- Top traders L/S 1.204.
- Fear & Greed 57 (Greed).
- Market cap crypto ≈ 2.70 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.47%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -366.41 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.546 · murC 85000 (+7.7%) · murP 70000 (-11.3%).
- Volumes cachés proxy : taker buy 0.511 · vol perp/spot 13.43×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
