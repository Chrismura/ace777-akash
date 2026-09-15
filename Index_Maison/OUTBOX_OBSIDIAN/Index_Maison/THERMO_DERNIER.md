# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-15T07:40Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `80/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77046.2 | prix |
| OI | 104439.824 | C13 |
| Funding | 7.1e-05 | C14 |
| Funding moy. ~30j | 6.655e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.402 | crowd |
| BTC 1h/4h/24h | -0.27 / -0.79 / -0.88 % | B7 |
| Dominance BTC | 58.37% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 80/100).
- Funding maintenant 7.1e-05. Moyenne ~30j 6.655e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.402.
- BTC 24h -0.88% · 1h -0.27% · 4h -0.79%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.907 · OI 104439.824 (pas de dark pool free temps réel).
- Top traders L/S 1.494.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.65 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.37%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -59.71 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.549 · murC 85000 (+10.3%) · murP 70000 (-9.2%).
- Volumes cachés proxy : taker buy 0.511 · vol perp/spot 13.53×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
