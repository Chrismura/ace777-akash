# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-25T22:00Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `89/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78536.8 | prix |
| OI | 106724.524 | C13 |
| Funding | 8.7e-05 | C14 |
| Funding moy. ~30j | 6.374e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.017 | crowd |
| BTC 1h/4h/24h | 0.01 / -0.69 / -0.53 % | B7 |
| Dominance BTC | 59.25% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat CALME (score 89/100).
- Funding maintenant 8.7e-05. Moyenne ~30j 6.374e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.017.
- BTC 24h -0.53% · 1h 0.01% · 4h -0.69%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.658 · OI 106724.524 (pas de dark pool free temps réel).
- Top traders L/S 1.096.
- Fear & Greed 74 (Greed).
- Market cap crypto ≈ 2.66 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.25%).
- Liquidations 24h proxy ≈ 0.04 B$.
- ETF net inflow : BTC 280.06 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.626 · murC 82000 (+4.3%) · murP 60000 (-23.7%).
- Volumes cachés proxy : taker buy 0.542 · vol perp/spot 13.19×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
