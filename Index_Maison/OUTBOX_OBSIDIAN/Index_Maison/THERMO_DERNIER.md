# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-21T14:53Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `60/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77379.97 | prix |
| OI | 107040.87 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 5.601e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.042 | crowd |
| BTC 1h/4h/24h | 0.19 / -0.53 / 7.91 % | B7 |
| Dominance BTC | 59.33% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat ATTENTION (score 60/100).
- Funding maintenant 0.0001. Moyenne ~30j 5.601e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.042.
- BTC 24h 7.91% · 1h 0.19% · 4h -0.53%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.036 · OI 107040.87 (pas de dark pool free temps réel).
- Top traders L/S 1.089.
- Fear & Greed 72 (Greed).
- Market cap crypto ≈ 2.62 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.33%).
- Liquidations 24h proxy ≈ 0.05 B$.
- ETF net inflow : BTC 993.61 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.585 · murC 78000 (+0.9%) · murP 60000 (-22.4%).
- Volumes cachés proxy : taker buy 0.516 · vol perp/spot 13.35×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=607 · heat=100.0 · PnL sess=272.6308 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
