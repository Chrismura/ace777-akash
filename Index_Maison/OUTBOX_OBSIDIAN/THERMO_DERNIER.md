# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-24T18:37Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `94/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84275.7 | prix |
| OI | 95188.736 | C13 |
| Funding | -4e-06 | C14 |
| Funding moy. ~30j | 6.134e-05 (n=90) | Cortana |
| Funding mois préc. | 6.772e-05 (n=93) | Cortana |
| L/S 1h | 1.223 | crowd |
| BTC 1h/4h/24h | 0.24 / 0.78 / 0.18 % | B7 |
| Dominance BTC | 58.57% | A3 |
| Alts ↓ 24h | 30.0% | B9 |

## Lecture
- Climat CALME (score 94/100).
- Funding maintenant -4e-06. Moyenne ~30j 6.134e-05 (90 pts). Mois précédent 6.772e-05 (93 pts).
- Long/Short 1.223.
- BTC 24h 0.18% · 1h 0.24% · 4h 0.78%.
- Panier alts : 30.0% en baisse (6/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 521696$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.807 · OI 95188.736 (pas de dark pool free temps réel).
- Top traders L/S 1.318.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.89 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.57%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 292.09 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.646 · murC 95000 (+12.7%) · murP 70000 (-17.0%).
- Volumes cachés proxy : taker buy 0.464 · vol perp/spot 11.01×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
