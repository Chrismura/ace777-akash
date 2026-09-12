# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-12T00:16Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `79/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77252.5 | prix |
| OI | 103477.517 | C13 |
| Funding | 6.2e-05 | C14 |
| Funding moy. ~30j | 6.663e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.547 | crowd |
| BTC 1h/4h/24h | 0.08 / -0.06 / 0.62 % | B7 |
| Dominance BTC | 58.28% | A3 |
| Alts ↓ 24h | 20.0% | B9 |

## Lecture
- Climat CALME (score 79/100).
- Funding maintenant 6.2e-05. Moyenne ~30j 6.663e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.547.
- BTC 24h 0.62% · 1h 0.08% · 4h -0.06%.
- Panier alts : 20.0% en baisse (4/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 1456125$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.052 · OI 103477.517 (pas de dark pool free temps réel).
- Top traders L/S 1.584.
- Fear & Greed 63 (Greed).
- Market cap crypto ≈ 2.66 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.28%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC 75.35 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.539 · murC 90000 (+16.5%) · murP 70000 (-9.4%).
- Volumes cachés proxy : taker buy 0.495 · vol perp/spot 14.3×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
