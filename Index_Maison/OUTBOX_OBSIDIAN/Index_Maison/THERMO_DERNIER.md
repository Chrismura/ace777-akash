# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-16T23:45Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `71/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81591.4 | prix |
| OI | 94133.545 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 3.369e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.728 | crowd |
| BTC 1h/4h/24h | -0.2 / 0.04 / -0.67 % | B7 |
| Dominance BTC | 59.35% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 71/100).
- Funding maintenant 0.0001. Moyenne ~30j 3.369e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.728.
- BTC 24h -0.67% · 1h -0.2% · 4h 0.04%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 604130$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.975 · OI 94133.545 (pas de dark pool free temps réel).
- Top traders L/S 1.869.
- Fear & Greed 63 (Greed).
- Market cap crypto ≈ 2.76 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.35%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -18.55 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.589 · murC 95000 (+16.5%) · murP 80000 (-1.9%).
- Volumes cachés proxy : taker buy 0.537 · vol perp/spot 12.09×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
