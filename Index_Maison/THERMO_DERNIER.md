# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-20T14:12Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `68/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83190.14 | prix |
| OI | 95726.647 | C13 |
| Funding | 4.5e-05 | C14 |
| Funding moy. ~30j | 3.198e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 1.845 | crowd |
| BTC 1h/4h/24h | 1.22 / 1.95 / 1.59 % | B7 |
| Dominance BTC | 59.56% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat ATTENTION (score 68/100).
- Funding maintenant 4.5e-05. Moyenne ~30j 3.198e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 1.845.
- BTC 24h 1.59% · 1h 1.22% · 4h 1.95%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 949263$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.124 · OI 95726.647 (pas de dark pool free temps réel).
- Top traders L/S 1.936.
- Fear & Greed 55 (Greed).
- Market cap crypto ≈ 2.78 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.56%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 587.22 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.565 · murC 95000 (+14.4%) · murP 75000 (-9.7%).
- Volumes cachés proxy : taker buy 0.459 · vol perp/spot 16.23×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
