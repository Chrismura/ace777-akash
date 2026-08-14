# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-14T21:32Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `67/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 62861.62 | prix |
| OI | 111999.871 | C13 |
| Funding | 4.1e-05 | C14 |
| Funding moy. ~30j | 5.421e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 2.099 | crowd |
| BTC 1h/4h/24h | -0.03 / -0.21 / -0.91 % | B7 |
| Dominance BTC | 56.12% | A3 |
| Alts ↓ 24h | 50.0% | B9 |

## Lecture
- Climat ATTENTION (score 67/100).
- Funding maintenant 4.1e-05. Moyenne ~30j 5.421e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 2.099.
- BTC 24h -0.91% · 1h -0.03% · 4h -0.21%.
- Panier alts : 50.0% en baisse (10/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.9 · OI 111999.871 (pas de dark pool free temps réel).
- Top traders L/S 2.19.
- Fear & Greed 29 (Fear).
- Market cap crypto ≈ 2.25 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.12%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -199.72 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.533 · murC 70000 (+11.4%) · murP 60000 (-4.5%).
- Volumes cachés proxy : taker buy 0.538 · vol perp/spot 10.77×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1128 · heat=100.0 · PnL sess=169.6072 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
