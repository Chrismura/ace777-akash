# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-28T09:17Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `80/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82802.3 | prix |
| OI | 95647.244 | C13 |
| Funding | -1.7e-05 | C14 |
| Funding moy. ~30j | 5.364e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.303 | crowd |
| BTC 1h/4h/24h | -0.12 / -0.37 / -2.14 % | B7 |
| Dominance BTC | 58.7% | A3 |
| Alts ↓ 24h | 85.0% | B9 |

## Lecture
- Climat CALME (score 80/100).
- Funding maintenant -1.7e-05. Moyenne ~30j 5.364e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.303.
- BTC 24h -2.14% · 1h -0.12% · 4h -0.37%.
- Panier alts : 85.0% en baisse (17/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 660337$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.844 · OI 95647.244 (pas de dark pool free temps réel).
- Top traders L/S 1.409.
- Fear & Greed 74 (Greed).
- Market cap crypto ≈ 2.82 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.7%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 286.98 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.487 · murC 95000 (+14.7%) · murP 75000 (-9.5%).
- Volumes cachés proxy : taker buy 0.492 · vol perp/spot 10.67×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
