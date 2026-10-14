# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-14T22:26Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `66/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 81547.6 | prix |
| OI | 93148.211 | C13 |
| Funding | -4.9e-05 | C14 |
| Funding moy. ~30j | 3.488e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.761 | crowd |
| BTC 1h/4h/24h | -0.23 / -0.16 / -2.24 % | B7 |
| Dominance BTC | 59.31% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat ATTENTION (score 66/100).
- Funding maintenant -4.9e-05. Moyenne ~30j 3.488e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.761.
- BTC 24h -2.24% · 1h -0.23% · 4h -0.16%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.98 · OI 93148.211 (pas de dark pool free temps réel).
- Top traders L/S 1.853.
- Fear & Greed 62 (Greed).
- Market cap crypto ≈ 2.76 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.31%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 148.98 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.612 · murC 95000 (+16.6%) · murP 78000 (-4.3%).
- Volumes cachés proxy : taker buy 0.507 · vol perp/spot 13.71×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
