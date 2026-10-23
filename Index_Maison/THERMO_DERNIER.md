# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-23T08:44Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `66/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81830.0 | prix |
| OI | 94984.968 | C13 |
| Funding | 7e-05 | C14 |
| Funding moy. ~30j | 3.105e-05 (n=90) | Cortana |
| Funding mois préc. | 4.965e-05 (n=90) | Cortana |
| L/S 1h | 2.198 | crowd |
| BTC 1h/4h/24h | 0.35 / 0.33 / -0.13 % | B7 |
| Dominance BTC | 59.42% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat ATTENTION (score 66/100).
- Funding maintenant 7e-05. Moyenne ~30j 3.105e-05 (90 pts). Mois précédent 4.965e-05 (90 pts).
- Long/Short 2.198.
- BTC 24h -0.13% · 1h 0.35% · 4h 0.33%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.075 · OI 94984.968 (pas de dark pool free temps réel).
- Top traders L/S 2.248.
- Fear & Greed 50 (Neutral).
- Market cap crypto ≈ 2.76 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.42%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 65.26 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.567 · murC 95000 (+16.2%) · murP 75000 (-8.3%).
- Volumes cachés proxy : taker buy 0.529 · vol perp/spot 16.48×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
