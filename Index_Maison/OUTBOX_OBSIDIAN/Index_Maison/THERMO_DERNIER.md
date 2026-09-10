# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-10T05:12Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `76/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78392.67 | prix |
| OI | 105298.547 | C13 |
| Funding | 9.5e-05 | C14 |
| Funding moy. ~30j | 6.754e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.469 | crowd |
| BTC 1h/4h/24h | 0.02 / 0.42 / -0.9 % | B7 |
| Dominance BTC | 58.56% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 76/100).
- Funding maintenant 9.5e-05. Moyenne ~30j 6.754e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.469.
- BTC 24h -0.9% · 1h 0.02% · 4h 0.42%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : 4 gros print(s) ≥500k$ (max 1135021$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.868 · OI 105298.547 (pas de dark pool free temps réel).
- Top traders L/S 1.532.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.68 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.56%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 93.85 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.54 · murC 81000 (+3.3%) · murP 70000 (-10.7%).
- Volumes cachés proxy : taker buy 0.484 · vol perp/spot 15.95×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
