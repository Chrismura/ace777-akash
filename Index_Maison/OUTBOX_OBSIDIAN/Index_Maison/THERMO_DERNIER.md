# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-29T09:06Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `75/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77650.34 | prix |
| OI | 106741.294 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 6.553e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.162 | crowd |
| BTC 1h/4h/24h | 0.05 / 0.05 / -2.12 % | B7 |
| Dominance BTC | 59.51% | A3 |
| Alts ↓ 24h | 70.0% | B9 |

## Lecture
- Climat CALME (score 75/100).
- Funding maintenant 0.0001. Moyenne ~30j 6.553e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.162.
- BTC 24h -2.12% · 1h 0.05% · 4h 0.05%.
- Panier alts : 70.0% en baisse (14/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 505765$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.933 · OI 106741.294 (pas de dark pool free temps réel).
- Top traders L/S 1.22.
- Fear & Greed 68 (Greed).
- Market cap crypto ≈ 2.61 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.51%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 212.8 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.573 · murC 82000 (+5.7%) · murP 70000 (-9.8%).
- Volumes cachés proxy : taker buy 0.495 · vol perp/spot 14.44×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
