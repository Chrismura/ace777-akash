# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-01T09:22Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `85/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77907.67 | prix |
| OI | 108938.913 | C13 |
| Funding | 8.7e-05 | C14 |
| Funding moy. ~30j | 6.805e-05 (n=90) | Cortana |
| Funding mois préc. | 6.769e-05 (n=93) | Cortana |
| L/S 1h | 1.082 | crowd |
| BTC 1h/4h/24h | 0.06 / -1.58 / -0.98 % | B7 |
| Dominance BTC | 59.59% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 85/100).
- Funding maintenant 8.7e-05. Moyenne ~30j 6.805e-05 (90 pts). Mois précédent 6.769e-05 (93 pts).
- Long/Short 1.082.
- BTC 24h -0.98% · 1h 0.06% · 4h -1.58%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 651896$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.784 · OI 108938.913 (pas de dark pool free temps réel).
- Top traders L/S 1.168.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.62 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.59%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 119.53 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.563 · murC 82000 (+5.2%) · murP 70000 (-10.2%).
- Volumes cachés proxy : taker buy 0.502 · vol perp/spot 12.77×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
