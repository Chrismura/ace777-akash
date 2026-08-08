# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-08T14:36Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `92/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 65145.7 | prix |
| OI | 107028.4 | C13 |
| Funding | 5.6e-05 | C14 |
| Funding moy. ~30j | 5.461e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.128 | crowd |
| BTC 1h/4h/24h | 0.25 / 0.25 / 0.05 % | B7 |
| Dominance BTC | 56.7% | A3 |
| Alts ↓ 24h | 0.0% | B9 |

## Lecture
- Climat CALME (score 92/100).
- Funding maintenant 5.6e-05. Moyenne ~30j 5.461e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.128.
- BTC 24h 0.05% · 1h 0.25% · 4h 0.25%.
- Panier alts : 0.0% en baisse (0/5).
- Whales proxy : 1 gros print(s) ≥500k$ (max 512366$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.196 · OI 107028.4 (pas de dark pool free temps réel).
- Top traders L/S 1.21.
- Fear & Greed 30 (Fear).
- Market cap crypto ≈ 2.30 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.7%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 57.54 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.598 · murC 70000 (+7.5%) · murP 60000 (-7.9%).
- Volumes cachés proxy : taker buy 0.522 · vol perp/spot 15.46×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
