# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-03T00:45Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `90/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84584.32 | prix |
| OI | 98059.681 | C13 |
| Funding | 4.5e-05 | C14 |
| Funding moy. ~30j | 4.904e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.188 | crowd |
| BTC 1h/4h/24h | 0.12 / 0.19 / -0.23 % | B7 |
| Dominance BTC | 58.7% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 90/100).
- Funding maintenant 4.5e-05. Moyenne ~30j 4.904e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.188.
- BTC 24h -0.23% · 1h 0.12% · 4h 0.19%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : 5 gros print(s) ≥500k$ (max 1068177$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.898 · OI 98059.681 (pas de dark pool free temps réel).
- Top traders L/S 1.26.
- Fear & Greed 67 (Greed).
- Market cap crypto ≈ 2.89 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.7%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 8.16 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.517 · murC 95000 (+12.3%) · murP 80000 (-5.4%).
- Volumes cachés proxy : taker buy 0.477 · vol perp/spot 10.99×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
