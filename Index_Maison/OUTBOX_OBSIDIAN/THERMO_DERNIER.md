# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-08-08T15:39Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `91/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 65040.39 | prix |
| OI | 107207.836 | C13 |
| Funding | 5.6e-05 | C14 |
| Funding moy. ~30j | 5.461e-05 (n=90) | Cortana |
| Funding mois préc. | 6.081e-05 (n=93) | Cortana |
| L/S 1h | 1.14 | crowd |
| BTC 1h/4h/24h | -0.1 / 0.15 / 0.13 % | B7 |
| Dominance BTC | 56.67% | A3 |
| Alts ↓ 24h | 0.0% | B9 |

## Lecture
- Climat CALME (score 91/100).
- Funding maintenant 5.6e-05. Moyenne ~30j 5.461e-05 (90 pts). Mois précédent 6.081e-05 (93 pts).
- Long/Short 1.14.
- BTC 24h 0.13% · 1h -0.1% · 4h 0.15%.
- Panier alts : 0.0% en baisse (0/5).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.38 · OI 107207.836 (pas de dark pool free temps réel).
- Top traders L/S 1.217.
- Fear & Greed 30 (Fear).
- Market cap crypto ≈ 2.30 T$.
- Alt season proxy : Bitcoin season (BTC.D 56.67%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 57.45 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.599 · murC 70000 (+7.7%) · murP 60000 (-7.7%).
- Volumes cachés proxy : taker buy 0.522 · vol perp/spot 16.21×.
- ACE soft: LIVE=NUAGE_TEST_8H_CMP3_LIVE_COLOR.log · SKIP=1016 · heat=25.6 · PnL sess=-8.5387 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
