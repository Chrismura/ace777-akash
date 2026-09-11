# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-11T02:16Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `72/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 76888.39 | prix |
| OI | 106942.57 | C13 |
| Funding | 6.4e-05 | C14 |
| Funding moy. ~30j | 6.729e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.636 | crowd |
| BTC 1h/4h/24h | -0.06 / 0.14 / -1.45 % | B7 |
| Dominance BTC | 58.48% | A3 |
| Alts ↓ 24h | 85.0% | B9 |

## Lecture
- Climat CALME (score 72/100).
- Funding maintenant 6.4e-05. Moyenne ~30j 6.729e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.636.
- BTC 24h -1.45% · 1h -0.06% · 4h 0.14%.
- Panier alts : 85.0% en baisse (17/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 750775$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.916 · OI 106942.57 (pas de dark pool free temps réel).
- Top traders L/S 1.73.
- Fear & Greed 56 (Greed).
- Market cap crypto ≈ 2.63 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.48%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 75.0 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.536 · murC 90000 (+17.0%) · murP 70000 (-9.0%).
- Volumes cachés proxy : taker buy 0.447 · vol perp/spot 14.03×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
