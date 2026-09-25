# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-25T05:41Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `89/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 84247.3 | prix |
| OI | 96581.88 | C13 |
| Funding | 6.2e-05 | C14 |
| Funding moy. ~30j | 6.05e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.235 | crowd |
| BTC 1h/4h/24h | 0.09 / -0.39 / 0.08 % | B7 |
| Dominance BTC | 58.58% | A3 |
| Alts ↓ 24h | 40.0% | B9 |

## Lecture
- Climat CALME (score 89/100).
- Funding maintenant 6.2e-05. Moyenne ~30j 6.05e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.235.
- BTC 24h 0.08% · 1h 0.09% · 4h -0.39%.
- Panier alts : 40.0% en baisse (8/20).
- Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.
- Dark/OTC proxy : taker buy/sell 0.91 · OI 96581.88 (pas de dark pool free temps réel).
- Top traders L/S 1.329.
- Fear & Greed 71 (Greed).
- Market cap crypto ≈ 2.88 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.58%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 291.99 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.642 · murC 95000 (+12.7%) · murP 70000 (-16.9%).
- Volumes cachés proxy : taker buy 0.464 · vol perp/spot 13.27×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
