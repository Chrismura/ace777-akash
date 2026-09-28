# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-28T07:17Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `83/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83093.55 | prix |
| OI | 95554.046 | C13 |
| Funding | -2.3e-05 | C14 |
| Funding moy. ~30j | 5.504e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.28 | crowd |
| BTC 1h/4h/24h | -0.04 / -0.26 / -1.67 % | B7 |
| Dominance BTC | 58.72% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat CALME (score 83/100).
- Funding maintenant -2.3e-05. Moyenne ~30j 5.504e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.28.
- BTC 24h -1.67% · 1h -0.04% · 4h -0.26%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.259 · OI 95554.046 (pas de dark pool free temps réel).
- Top traders L/S 1.381.
- Fear & Greed 74 (Greed).
- Market cap crypto ≈ 2.84 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.72%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 287.99 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.478 · murC 95000 (+14.3%) · murP 75000 (-9.7%).
- Volumes cachés proxy : taker buy 0.492 · vol perp/spot 12.61×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
