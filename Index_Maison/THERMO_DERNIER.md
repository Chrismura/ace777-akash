# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-12T22:08Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `71/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 63449.0 | prix |
| OI | 110937.241 | C13 |
| Funding | 8.6e-05 | C14 |
| Funding moy. ~30j | 5.477e-05 (n=90) | Cortana |
| Funding mois préc. | 6.043e-05 (n=93) | Cortana |
| L/S 1h | 1.833 | crowd |
| BTC 1h/4h/24h | 0.01 / 0.14 / -0.4 % | B7 |
| Dominance BTC | 56.29% | A3 |
| Alts ↓ 24h | 100.0% | B9 |

## Lecture
- Climat CALME (score 71/100).
- Funding maintenant 8.6e-05. Moyenne ~30j 5.477e-05 (90 pts). Mois précédent 6.043e-05 (93 pts).
- Long/Short 1.833.
- BTC 24h -0.4% · 1h 0.01% · 4h 0.14%.
- Panier alts : 100.0% en baisse (5/5).
- Whales proxy : 2 gros print(s) ≥500k$ (max 1188760$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.795 · OI 110937.241 (pas de dark pool free temps réel).
- Top traders L/S 1.88.
- Fear & Greed 27 (Fear).
- Market cap crypto ≈ 2.26 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.29%).
- Liquidations 24h proxy ≈ 0.01 B$.
- ETF net inflow : BTC 37.19 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.556 · murC 70000 (+10.4%) · murP 60000 (-5.4%).
- Volumes cachés proxy : taker buy 0.494 · vol perp/spot 11.67×.
- ACE soft: LIVE=MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log · SKIP=1149 · heat=100.0 · PnL sess=116.2035 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
