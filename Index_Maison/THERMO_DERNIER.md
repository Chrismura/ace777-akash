# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-07T16:04Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `69/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 83461.42 | prix |
| OI | 95641.017 | C13 |
| Funding | 1.2e-05 | C14 |
| Funding moy. ~30j | 4.481e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.669 | crowd |
| BTC 1h/4h/24h | 0.07 / 0.01 / -2.7 % | B7 |
| Dominance BTC | 58.79% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat ATTENTION (score 69/100).
- Funding maintenant 1.2e-05. Moyenne ~30j 4.481e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.669.
- BTC 24h -2.7% · 1h 0.07% · 4h 0.01%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 580381$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.107 · OI 95641.017 (pas de dark pool free temps réel).
- Top traders L/S 1.751.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.85 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.79%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -87.93 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.533 · murC 95000 (+13.8%) · murP 80000 (-4.2%).
- Volumes cachés proxy : taker buy 0.477 · vol perp/spot 13.46×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
