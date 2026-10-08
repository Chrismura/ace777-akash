# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-08T16:15Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `62/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 80950.0 | prix |
| OI | 94462.925 | C13 |
| Funding | 3.3e-05 | C14 |
| Funding moy. ~30j | 4.254e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.819 | crowd |
| BTC 1h/4h/24h | -0.05 / -1.61 / -3.04 % | B7 |
| Dominance BTC | 59.13% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat ATTENTION (score 62/100).
- Funding maintenant 3.3e-05. Moyenne ~30j 4.254e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.819.
- BTC 24h -3.04% · 1h -0.05% · 4h -1.61%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.876 · OI 94462.925 (pas de dark pool free temps réel).
- Top traders L/S 1.931.
- Fear & Greed 64 (Greed).
- Market cap crypto ≈ 2.74 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.13%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -326.79 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.586 · murC 95000 (+17.4%) · murP 80000 (-1.1%).
- Volumes cachés proxy : taker buy 0.504 · vol perp/spot 11.88×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
