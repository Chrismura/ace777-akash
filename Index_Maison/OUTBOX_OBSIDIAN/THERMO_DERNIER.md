# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-11-03T13:12Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `warn` · **Score :** `58/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 77302.86 | prix |
| OI | 100082.429 | C13 |
| Funding | 0.0001 | C14 |
| Funding moy. ~30j | 4.867e-05 (n=90) | Cortana |
| Funding mois préc. | 4.436e-05 (n=93) | Cortana |
| L/S 1h | 2.647 | crowd |
| BTC 1h/4h/24h | -0.13 / 0.33 / -0.48 % | B7 |
| Dominance BTC | 59.21% | A3 |
| Alts ↓ 24h | 80.0% | B9 |

## Lecture
- Climat ATTENTION (score 58/100).
- Funding maintenant 0.0001. Moyenne ~30j 4.867e-05 (90 pts). Mois précédent 4.436e-05 (93 pts).
- Long/Short 2.647.
- BTC 24h -0.48% · 1h -0.13% · 4h 0.33%.
- Panier alts : 80.0% en baisse (16/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 1.135 · OI 100082.429 (pas de dark pool free temps réel).
- Top traders L/S 2.745.
- Fear & Greed 26 (Fear).
- Market cap crypto ≈ 2.62 T$.
- Alt season proxy : Bitcoin season (BTC.D 59.21%).
- Liquidations 24h proxy ≈ 2.60 M$.
- ETF net inflow : BTC -655.43 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.684 · murC 90000 (+16.6%) · murP 72000 (-6.7%).
- Volumes cachés proxy : taker buy 0.577 · vol perp/spot 11.22×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- OFI réel (C26) : SANS_MESURE (fichier absent/stale).
- Mur mesuré (C27) : seuil 11.027% (98.41$) · k=5.0 σ20j=2.2054% · pireDD20j -6.16%.
- Kelly S2 (C28) : m=10.51 · expo 720.67$ · maxS2 3.71$ · aveugles 3.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **Mesures maison (02/11) :** C26 OFI réel L2 · C27 Mur k×σ · C28 Kelly S2
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
