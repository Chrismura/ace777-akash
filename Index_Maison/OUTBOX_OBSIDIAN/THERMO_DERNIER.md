# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-21T04:59Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `83/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81361.7 | prix |
| OI | 108187.625 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 6.81e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 0.934 | crowd |
| BTC 1h/4h/24h | -0.05 / -0.26 / 1.18 % | B7 |
| Dominance BTC | 58.15% | A3 |
| Alts ↓ 24h | 35.0% | B9 |

## Lecture
- Climat CALME (score 83/100).
- Funding maintenant 0.0001. Moyenne ~30j 6.81e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 0.934.
- BTC 24h 1.18% · 1h -0.05% · 4h -0.26%.
- Panier alts : 35.0% en baisse (7/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 778514$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.128 · OI 108187.625 (pas de dark pool free temps réel).
- Top traders L/S 1.061.
- Fear & Greed 70 (Greed).
- Market cap crypto ≈ 2.80 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.15%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -65.46 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.562 · murC 85000 (+4.5%) · murP 70000 (-14.0%).
- Volumes cachés proxy : taker buy 0.478 · vol perp/spot 14.67×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
