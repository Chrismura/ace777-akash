# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-11-02T13:20Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `64/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77597.5 | prix |
| OI | 96129.584 | C13 |
| Funding | 9.9e-05 | C14 |
| Funding moy. ~30j | 4.617e-05 (n=90) | Cortana |
| Funding mois préc. | 4.436e-05 (n=93) | Cortana |
| L/S 1h | 2.105 | crowd |
| BTC 1h/4h/24h | -0.23 / -0.57 / -0.48 % | B7 |
| Dominance BTC | 59.88% | A3 |
| Alts ↓ 24h | 55.0% | B9 |

## Lecture
- Climat ATTENTION (score 64/100).
- Funding maintenant 9.9e-05. Moyenne ~30j 4.617e-05 (90 pts). Mois précédent 4.436e-05 (93 pts).
- Long/Short 2.105.
- BTC 24h -0.48% · 1h -0.23% · 4h -0.57%.
- Panier alts : 55.0% en baisse (11/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.066 · OI 96129.584 (pas de dark pool free temps réel).
- Top traders L/S 2.252.
- Fear & Greed 37 (Fear).
- Market cap crypto ≈ 2.59 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.88%).
- Liquidations 24h proxy ≈ 1.60 M$.
- ETF net inflow : BTC 63.06 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.684 · murC 90000 (+16.1%) · murP 60000 (-22.6%).
- Volumes cachés proxy : taker buy 0.528 · vol perp/spot 10.09×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
