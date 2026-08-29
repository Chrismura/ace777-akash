# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-29T12:05Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `73/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77575.9 | prix |
| OI | 106970.876 | C13 |
| Funding | 9.9e-05 | C14 |
| Funding moy. ~30j | 6.553e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.171 | crowd |
| BTC 1h/4h/24h | 0.02 / -0.04 / -2.51 % | B7 |
| Dominance BTC | 59.48% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 73/100).
- Funding maintenant 9.9e-05. Moyenne ~30j 6.553e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.171.
- BTC 24h -2.51% · 1h 0.02% · 4h -0.04%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 621081$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.12 · OI 106970.876 (pas de dark pool free temps réel).
- Top traders L/S 1.226.
- Fear & Greed 68 (Greed).
- Market cap crypto ≈ 2.61 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.48%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 212.6 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.574 · murC 82000 (+5.7%) · murP 70000 (-9.8%).
- Volumes cachés proxy : taker buy 0.495 · vol perp/spot 14.39×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
