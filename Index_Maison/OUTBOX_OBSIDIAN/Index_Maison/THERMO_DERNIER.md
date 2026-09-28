# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-28T05:38Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `81/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 82879.84 | prix |
| OI | 95705.51 | C13 |
| Funding | -3.1e-05 | C14 |
| Funding moy. ~30j | 5.504e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.244 | crowd |
| BTC 1h/4h/24h | -0.67 / -0.91 / -1.94 % | B7 |
| Dominance BTC | 58.7% | A3 |
| Alts ↓ 24h | 75.0% | B9 |

## Lecture
- Climat CALME (score 81/100).
- Funding maintenant -3.1e-05. Moyenne ~30j 5.504e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.244.
- BTC 24h -1.94% · 1h -0.67% · 4h -0.91%.
- Panier alts : 75.0% en baisse (15/20).
- Whales proxy : 2 gros print(s) ≥500k$ (max 982345$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 1.214 · OI 95705.51 (pas de dark pool free temps réel).
- Top traders L/S 1.331.
- Fear & Greed 74 (Greed).
- Market cap crypto ≈ 2.84 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.7%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC 287.25 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.472 · murC 95000 (+14.6%) · murP 75000 (-9.5%).
- Volumes cachés proxy : taker buy 0.492 · vol perp/spot 12.92×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
