# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-11-03T01:32Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `52/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77201.6 | prix |
| OI | 99403.733 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.794e-05 (n=90) | Cortana |
| Funding mois préc. | 4.378e-05 (n=93) | Cortana |
| L/S 1h | 2.622 | crowd |
| BTC 1h/4h/24h | 0.13 / 0.48 / -1.55 % | B7 |
| Dominance BTC | 59.32% | A3 |
| Alts ↓ 24h | 85.0% | B9 |

## Lecture
- Climat ATTENTION (score 52/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.794e-05 (90 pts). Mois précédent 4.378e-05 (93 pts).
- Long/Short 2.622.
- BTC 24h -1.55% · 1h 0.13% · 4h 0.48%.
- Panier alts : 85.0% en baisse (17/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1647887$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.053 · OI 99403.733 (pas de dark pool free temps réel).
- Top traders L/S 2.833.
- Fear & Greed 26 (Fear).
- Market cap crypto ≈ 2.61 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.32%).
- Liquidations 24h proxy ≈ 1.89 M$.
- ETF net inflow : BTC 47.51 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.696 · murC 90000 (+16.7%) · murP 60000 (-22.2%).
- Volumes cachés proxy : taker buy 0.577 · vol perp/spot 10.39×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- OFI réel (C26) : NEUTRE +0.0036 · Δ -4.61bps (n=120) — pas d’absorption.
- Mur mesuré (C27) : seuil 11.222% (100.3$) · k=5.0 σ20j=2.2445% · pireDD20j -6.16%.
- Kelly S2 (C28) : m=8.135 · expo 699.68$ · maxS2 4.84$ · aveugles 3.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **Mesures maison (02/11) :** C26 OFI réel L2 · C27 Mur k×σ · C28 Kelly S2
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
