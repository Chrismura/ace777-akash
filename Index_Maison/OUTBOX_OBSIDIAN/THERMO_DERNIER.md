# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-10-12T21:47Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `76/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82451.2 | prix |
| OI | 93388.098 | C13 |
| Funding | 7.7e-05 | C14 |
| Funding moy. ~30j | 3.696e-05 (n=90) | Cortana |
| Funding mois préc. | 5e-05 (n=90) | Cortana |
| L/S 1h | 1.478 | crowd |
| BTC 1h/4h/24h | -0.76 / -0.04 / -1.15 % | B7 |
| Dominance BTC | 59.2% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat CALME (score 76/100).
- Funding maintenant 7.7e-05. Moyenne ~30j 3.696e-05 (90 pts). Mois précédent 5e-05 (90 pts).
- Long/Short 1.478.
- BTC 24h -1.15% · 1h -0.76% · 4h -0.04%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 646069$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.768 · OI 93388.098 (pas de dark pool free temps réel).
- Top traders L/S 1.587.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.81 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.2%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -219.03 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.581 · murC 95000 (+15.3%) · murP 80000 (-2.9%).
- Volumes cachés proxy : taker buy 0.504 · vol perp/spot 11.27×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
