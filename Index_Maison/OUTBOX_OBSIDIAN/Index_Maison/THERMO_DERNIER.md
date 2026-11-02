# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-11-02T10:08Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `66/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77945.1 | prix |
| OI | 95609.011 | C13 |
| Funding | 8.6e-05 | C14 |
| Funding moy. ~30j | 4.617e-05 (n=90) | Cortana |
| Funding mois préc. | 4.436e-05 (n=93) | Cortana |
| L/S 1h | 2.115 | crowd |
| BTC 1h/4h/24h | -0.12 / -0.24 / -0.21 % | B7 |
| Dominance BTC | 59.96% | A3 |
| Alts ↓ 24h | 45.0% | B9 |

## Lecture
- Climat ATTENTION (score 66/100).
- Funding maintenant 8.6e-05. Moyenne ~30j 4.617e-05 (90 pts). Mois précédent 4.436e-05 (93 pts).
- Long/Short 2.115.
- BTC 24h -0.21% · 1h -0.12% · 4h -0.24%.
- Panier alts : 45.0% en baisse (9/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.008 · OI 95609.011 (pas de dark pool free temps réel).
- Top traders L/S 2.257.
- Fear & Greed 37 (Fear).
- Market cap crypto ≈ 2.60 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.96%).
- Liquidations 24h proxy ≈ 1.63 M$.
- ETF net inflow : BTC 63.34 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.665 · murC 90000 (+15.6%) · murP 60000 (-22.9%).
- Volumes cachés proxy : taker buy 0.528 · vol perp/spot 10.13×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
