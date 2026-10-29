# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-29T13:22Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `61/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80183.59 | prix |
| OI | 97944.053 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.029e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 2.17 | crowd |
| BTC 1h/4h/24h | 0.2 / 0.01 / -0.63 % | B7 |
| Dominance BTC | 59.35% | A3 |
| Alts ↓ 24h | 70.0% | B9 |

## Lecture
- Climat ATTENTION (score 61/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.029e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 2.17.
- BTC 24h -0.63% · 1h 0.2% · 4h 0.01%.
- Panier alts : 70.0% en baisse (14/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.008 · OI 97944.053 (pas de dark pool free temps réel).
- Top traders L/S 2.313.
- Fear & Greed 51 (Neutral).
- Market cap crypto ≈ 2.71 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.35%).
- Liquidations 24h proxy ≈ 1.62 M$.
- ETF net inflow : BTC -0.94 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.593 · murC 95000 (+18.6%) · murP 75000 (-6.4%).
- Volumes cachés proxy : taker buy 0.492 · vol perp/spot 15.97×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
