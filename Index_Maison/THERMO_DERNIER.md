# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-30T11:09Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `84/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78171.0 | prix |
| OI | 108580.91 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 6.551e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.129 | crowd |
| BTC 1h/4h/24h | 0.07 / 0.11 / 0.72 % | B7 |
| Dominance BTC | 59.47% | A3 |
| Alts ↓ 24h | 5.0% | B9 |

## Lecture
- Climat CALME (score 84/100).
- Funding maintenant 0.0001. Moyenne ~30j 6.551e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.129.
- BTC 24h 0.72% · 1h 0.07% · 4h 0.11%.
- Panier alts : 5.0% en baisse (1/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.014 · OI 108580.91 (pas de dark pool free temps réel).
- Top traders L/S 1.192.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.63 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.47%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 201.99 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.57 · murC 82000 (+4.9%) · murP 70000 (-10.5%).
- Volumes cachés proxy : taker buy 0.478 · vol perp/spot 12.12×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
