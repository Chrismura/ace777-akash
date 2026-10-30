# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-30T11:49Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `hot` · **Score :** `42/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77417.65 | prix |
| OI | 95421.602 | C13 |
| Funding | 9.6e-05 | C14 |
| Funding moy. ~30j | 4.13e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 2.469 | crowd |
| BTC 1h/4h/24h | -0.5 / -0.95 / -3.45 % | B7 |
| Dominance BTC | 59.77% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat CHAUD (score 42/100).
- Funding maintenant 9.6e-05. Moyenne ~30j 4.13e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 2.469.
- BTC 24h -3.45% · 1h -0.5% · 4h -0.95%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.887 · OI 95421.602 (pas de dark pool free temps réel).
- Top traders L/S 2.617.
- Fear & Greed 30 (Fear).
- Market cap crypto ≈ 2.60 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.77%).
- Liquidations 24h proxy ≈ 1.97 M$.
- ETF net inflow : BTC 21.11 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.709 · murC 90000 (+16.4%) · murP 60000 (-22.4%).
- Volumes cachés proxy : taker buy 0.526 · vol perp/spot 10.29×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
