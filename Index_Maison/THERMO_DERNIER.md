# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-28T15:25Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `87/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 79400.0 | prix |
| OI | 106464.117 | C13 |
| Funding | 5.1e-05 | C14 |
| Funding moy. ~30j | 6.481e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.04 | crowd |
| BTC 1h/4h/24h | -0.15 / -0.21 / -1.41 % | B7 |
| Dominance BTC | 59.14% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 87/100).
- Funding maintenant 5.1e-05. Moyenne ~30j 6.481e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.04.
- BTC 24h -1.41% · 1h -0.15% · 4h -0.21%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 652343$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.952 · OI 106464.117 (pas de dark pool free temps réel).
- Top traders L/S 1.141.
- Fear & Greed 73 (Greed).
- Market cap crypto ≈ 2.69 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.14%).
- Liquidations 24h proxy ≈ 0.04 B$.
- ETF net inflow : BTC 520.45 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.537 · murC 82000 (+3.2%) · murP 70000 (-11.9%).
- Volumes cachés proxy : taker buy 0.496 · vol perp/spot 13.57×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
