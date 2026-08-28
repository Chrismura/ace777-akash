# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-28T14:24Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `87/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78680.5 | prix |
| OI | 107084.376 | C13 |
| Funding | 5.3e-05 | C14 |
| Funding moy. ~30j | 6.481e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.027 | crowd |
| BTC 1h/4h/24h | -0.74 / -1.05 / -1.37 % | B7 |
| Dominance BTC | 59.11% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 87/100).
- Funding maintenant 5.3e-05. Moyenne ~30j 6.481e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.027.
- BTC 24h -1.37% · 1h -0.74% · 4h -1.05%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 2375560$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.908 · OI 107084.376 (pas de dark pool free temps réel).
- Top traders L/S 1.12.
- Fear & Greed 73 (Greed).
- Market cap crypto ≈ 2.66 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.11%).
- Liquidations 24h proxy ≈ 0.03 B$.
- ETF net inflow : BTC 515.73 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.536 · murC 82000 (+4.1%) · murP 70000 (-11.2%).
- Volumes cachés proxy : taker buy 0.496 · vol perp/spot 12.88×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
