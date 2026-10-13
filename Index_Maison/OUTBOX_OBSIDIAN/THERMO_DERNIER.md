# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-13T23:13Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `85/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83226.17 | prix |
| OI | 92842.053 | C13 |
| Funding | -5e-06 | C14 |
| Funding moy. ~30j | 3.718e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.286 | crowd |
| BTC 1h/4h/24h | -0.31 / -0.04 / 1.52 % | B7 |
| Dominance BTC | 59.28% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat CALME (score 85/100).
- Funding maintenant -5e-06. Moyenne ~30j 3.718e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.286.
- BTC 24h 1.52% · 1h -0.31% · 4h -0.04%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : 5 gros print(s) ≥500k$ (max 891749$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.064 · OI 92842.053 (pas de dark pool free temps réel).
- Top traders L/S 1.344.
- Fear & Greed 57 (Greed).
- Market cap crypto ≈ 2.81 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.28%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -102.57 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.587 · murC 95000 (+14.2%) · murP 78000 (-6.2%).
- Volumes cachés proxy : taker buy 0.467 · vol perp/spot 12.57×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
