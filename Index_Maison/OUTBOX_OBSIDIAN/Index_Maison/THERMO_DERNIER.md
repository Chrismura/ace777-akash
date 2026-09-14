# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-14T06:36Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `78/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77443.58 | prix |
| OI | 106652.741 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 6.622e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.535 | crowd |
| BTC 1h/4h/24h | -0.18 / -0.18 / 0.24 % | B7 |
| Dominance BTC | 58.85% | A3 |
| Alts ↓ 24h | 60.0% | B9 |

## Lecture
- Climat CALME (score 78/100).
- Funding maintenant 0.0001. Moyenne ~30j 6.622e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.535.
- BTC 24h 0.24% · 1h -0.18% · 4h -0.18%.
- Panier alts : 60.0% en baisse (12/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1339781$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.903 · OI 106652.741 (pas de dark pool free temps réel).
- Top traders L/S 1.582.
- Fear & Greed 57 (Greed).
- Market cap crypto ≈ 2.64 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.85%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -8.65 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.556 · murC 90000 (+16.2%) · murP 70000 (-9.6%).
- Volumes cachés proxy : taker buy 0.513 · vol perp/spot 13.87×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
