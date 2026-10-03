# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-03T15:46Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `89/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84803.8 | prix |
| OI | 97611.597 | C13 |
| Funding | 3.7e-05 | C14 |
| Funding moy. ~30j | 4.843e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.221 | crowd |
| BTC 1h/4h/24h | -0.02 / 0.2 / -0.57 % | B7 |
| Dominance BTC | 58.7% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 89/100).
- Funding maintenant 3.7e-05. Moyenne ~30j 4.843e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.221.
- BTC 24h -0.57% · 1h -0.02% · 4h 0.2%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 624357$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.802 · OI 97611.597 (pas de dark pool free temps réel).
- Top traders L/S 1.246.
- Fear & Greed 67 (Greed).
- Market cap crypto ≈ 2.90 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.7%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 8.18 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.512 · murC 95000 (+12.0%) · murP 75000 (-11.6%).
- Volumes cachés proxy : taker buy 0.477 · vol perp/spot 10.87×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
