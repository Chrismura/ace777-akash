# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-17T11:53Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `67/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63625.5 | prix |
| OI | 109079.97 | C13 |
| Funding | 6e-05 | C14 |
| Funding moy. ~30j | 5.377e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.982 | crowd |
| BTC 1h/4h/24h | -0.06 / 0.2 / 1.07 % | B7 |
| Dominance BTC | 56.26% | A3 |
| Alts ↓ 24h | 5.0% | B9 |

## Lecture
- Climat ATTENTION (score 67/100).
- Funding maintenant 6e-05. Moyenne ~30j 5.377e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.982.
- BTC 24h 1.07% · 1h -0.06% · 4h 0.2%.
- Panier alts : 5.0% en baisse (1/20).
- Whales proxy : 3 gros print(s) ≥500k$ (max 1509304$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.764 · OI 109079.97 (pas de dark pool free temps réel).
- Top traders L/S 2.019.
- Fear & Greed 31 (Fear).
- Market cap crypto ≈ 2.27 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.26%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC -56.1 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.554 · murC 70000 (+10.1%) · murP 60000 (-5.6%).
- Volumes cachés proxy : taker buy 0.488 · vol perp/spot 16.45×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1103 · heat=100.0 · PnL sess=178.5172 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
