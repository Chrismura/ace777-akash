# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-11T05:16Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `69/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77090.27 | prix |
| OI | 106971.817 | C13 |
| Funding | 8.4e-05 | C14 |
| Funding moy. ~30j | 6.729e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.648 | crowd |
| BTC 1h/4h/24h | 0.02 / 0.19 / -1.7 % | B7 |
| Dominance BTC | 58.46% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat ATTENTION (score 69/100).
- Funding maintenant 8.4e-05. Moyenne ~30j 6.729e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.648.
- BTC 24h -1.7% · 1h 0.02% · 4h 0.19%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 717636$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.728 · OI 106971.817 (pas de dark pool free temps réel).
- Top traders L/S 1.669.
- Fear & Greed 56 (Greed).
- Market cap crypto ≈ 2.64 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.46%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 75.19 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.537 · murC 90000 (+16.7%) · murP 70000 (-9.2%).
- Volumes cachés proxy : taker buy 0.447 · vol perp/spot 14.07×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
