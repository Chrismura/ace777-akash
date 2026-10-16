# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-16T01:01Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `81/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82318.2 | prix |
| OI | 94261.639 | C13 |
| Funding | 4.5e-05 | C14 |
| Funding moy. ~30j | 3.335e-05 (n=90) | Cortana |
| Funding mois préc. | 5.025e-05 (n=90) | Cortana |
| L/S 1h | 1.511 | crowd |
| BTC 1h/4h/24h | 0.02 / -0.08 / 0.6 % | B7 |
| Dominance BTC | 59.34% | A3 |
| Alts ↓ 24h | 15.0% | B9 |

## Lecture
- Climat CALME (score 81/100).
- Funding maintenant 4.5e-05. Moyenne ~30j 3.335e-05 (90 pts). Mois précédent 5.025e-05 (90 pts).
- Long/Short 1.511.
- BTC 24h 0.6% · 1h 0.02% · 4h -0.08%.
- Panier alts : 15.0% en baisse (3/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.876 · OI 94261.639 (pas de dark pool free temps réel).
- Top traders L/S 1.589.
- Fear & Greed 63 (Greed).
- Market cap crypto ≈ 2.78 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.34%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -49.06 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.613 · murC 95000 (+15.5%) · murP 78000 (-5.2%).
- Volumes cachés proxy : taker buy 0.555 · vol perp/spot 13.24×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
