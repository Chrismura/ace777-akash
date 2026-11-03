# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-11-03T14:39Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `57/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77333.4 | prix |
| OI | 99407.292 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.867e-05 (n=90) | Cortana |
| Funding mois préc. | 4.436e-05 (n=93) | Cortana |
| L/S 1h | 2.583 | crowd |
| BTC 1h/4h/24h | -0.03 / 0.31 / -0.73 % | B7 |
| Dominance BTC | 59.19% | A3 |
| Alts ↓ 24h | 70.0% | B9 |

## Lecture
- Climat ATTENTION (score 57/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.867e-05 (90 pts). Mois précédent 4.436e-05 (93 pts).
- Long/Short 2.583.
- BTC 24h -0.73% · 1h -0.03% · 4h 0.31%.
- Panier alts : 70.0% en baisse (14/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 1067028$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.964 · OI 99407.292 (pas de dark pool free temps réel).
- Top traders L/S 2.671.
- Fear & Greed 26 (Fear).
- Market cap crypto ≈ 2.62 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.19%).
- Liquidations 24h proxy ≈ 1.93 M$.
- ETF net inflow : BTC -655.69 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.683 · murC 90000 (+16.5%) · murP 72000 (-6.8%).
- Volumes cachés proxy : taker buy 0.577 · vol perp/spot 11.06×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- OFI réel (C26) : NEUTRE +0.0156 · Δ -15.94bps (n=120) — pas d’absorption.
- Mur mesuré (C27) : seuil 11.027% (98.41$) · k=5.0 σ20j=2.2054% · pireDD20j -6.16%.
- Kelly S2 (C28) : m=10.51 · expo 720.67$ · maxS2 3.71$ · aveugles 3.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **Mesures maison (02/11) :** C26 OFI réel L2 · C27 Mur k×σ · C28 Kelly S2
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
