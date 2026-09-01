# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-01T11:15Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `87/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77964.0 | prix |
| OI | 108863.908 | C13 |
| Funding | 5.3e-05 | C14 |
| Funding moy. ~30j | 6.805e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.146 | crowd |
| BTC 1h/4h/24h | -0.03 / -0.81 / -0.81 % | B7 |
| Dominance BTC | 59.56% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat CALME (score 87/100).
- Funding maintenant 5.3e-05. Moyenne ~30j 6.805e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.146.
- BTC 24h -0.81% · 1h -0.03% · 4h -0.81%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.987 · OI 108863.908 (pas de dark pool free temps réel).
- Top traders L/S 1.227.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.62 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.56%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 119.62 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.563 · murC 82000 (+5.2%) · murP 70000 (-10.2%).
- Volumes cachés proxy : taker buy 0.502 · vol perp/spot 12.77×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
