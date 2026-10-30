# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-30T13:52Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `hot` · **Score :** `36/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 76639.9 | prix |
| OI | 96678.101 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.13e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 2.494 | crowd |
| BTC 1h/4h/24h | -1.04 / -1.32 / -4.47 % | B7 |
| Dominance BTC | 59.2% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat CHAUD (score 36/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.13e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 2.494.
- BTC 24h -4.47% · 1h -1.04% · 4h -1.32%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.157 · OI 96678.101 (pas de dark pool free temps réel).
- Top traders L/S 2.65.
- Fear & Greed 30 (Fear).
- Market cap crypto ≈ 2.60 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.2%).
- Liquidations 24h proxy ≈ 2.91 M$.
- ETF net inflow : BTC 20.9 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.719 · murC 90000 (+17.6%) · murP 60000 (-21.6%).
- Volumes cachés proxy : taker buy 0.526 · vol perp/spot 9.85×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
