# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-30T01:01Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `85/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 78131.42 | prix |
| OI | 107764.531 | C13 |
| Funding | 8.2e-05 | C14 |
| Funding moy. ~30j | 6.545e-05 (n=90) | Cortana |
| Funding mois préc. | 6.067e-05 (n=93) | Cortana |
| L/S 1h | 1.181 | crowd |
| BTC 1h/4h/24h | -0.02 / -0.01 / 0.57 % | B7 |
| Dominance BTC | 59.48% | A3 |
| Alts ↓ 24h | 25.0% | B9 |

## Lecture
- Climat CALME (score 85/100).
- Funding maintenant 8.2e-05. Moyenne ~30j 6.545e-05 (90 pts). Mois précédent 6.067e-05 (93 pts).
- Long/Short 1.181.
- BTC 24h 0.57% · 1h -0.02% · 4h -0.01%.
- Panier alts : 25.0% en baisse (5/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 1043894$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.995 · OI 107764.531 (pas de dark pool free temps réel).
- Top traders L/S 1.221.
- Fear & Greed 69 (Greed).
- Market cap crypto ≈ 2.63 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.48%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 201.88 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.569 · murC 82000 (+4.9%) · murP 70000 (-10.4%).
- Volumes cachés proxy : taker buy 0.478 · vol perp/spot 11.18×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1330 · heat=100.0 · PnL sess=318.5769 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
