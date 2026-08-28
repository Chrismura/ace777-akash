# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-28T23:01Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `70/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77728.2 | prix |
| OI | 105899.327 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 6.506e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.182 | crowd |
| BTC 1h/4h/24h | -0.05 / 0.18 / -3.12 % | B7 |
| Dominance BTC | 58.98% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat CALME (score 70/100).
- Funding maintenant 0.0001. Moyenne ~30j 6.506e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.182.
- BTC 24h -3.12% · 1h -0.05% · 4h 0.18%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.143 · OI 105899.327 (pas de dark pool free temps réel).
- Top traders L/S 1.306.
- Fear & Greed 73 (Greed).
- Market cap crypto ≈ 2.64 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.98%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 509.49 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.578 · murC 82000 (+5.5%) · murP 70000 (-9.9%).
- Volumes cachés proxy : taker buy 0.495 · vol perp/spot 14.38×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
