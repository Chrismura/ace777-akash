# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · 2026-09-18T02:17Z UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `ok` · **Score :** `80/100`

## Snapshot `BTCUSDT`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | 76756.4 | prix |
| OI | 108448.827 | C13 |
| Funding | 6.5e-05 | C14 |
| Funding moy. ~30j | 6.816e-05 (n=90) | Cortana |
| Funding mois préc. | 6.695e-05 (n=93) | Cortana |
| L/S 1h | 1.444 | crowd |
| BTC 1h/4h/24h | 0.07 / 0.48 / 0.8 % | B7 |
| Dominance BTC | 58.06% | A3 |
| Alts ↓ 24h | 15.0% | B9 |

## Lecture
- Climat CALME (score 80/100).
- Funding maintenant 6.5e-05. Moyenne ~30j 6.816e-05 (90 pts). Mois précédent 6.695e-05 (93 pts).
- Long/Short 1.444.
- BTC 24h 0.8% · 1h 0.07% · 4h 0.48%.
- Panier alts : 15.0% en baisse (3/20).
- Whales proxy : 1 gros print(s) ≥500k$ (max 2166448$) — source aggTrades Binance.
- Dark/OTC proxy : taker buy/sell 0.924 · OI 108448.827 (pas de dark pool free temps réel).
- Top traders L/S 1.526.
- Fear & Greed 56 (Greed).
- Market cap crypto ≈ 2.64 T$.
- Alt season proxy : Bitcoin season (BTC.D 58.06%).
- Liquidations 24h proxy ≈ 0.00 B$.
- ETF net inflow : BTC -105.43 M$ (bitbo-public (moy 7j), BTC only).
- GEX proxy (Deribit) : P/C 0.566 · murC 90000 (+17.3%) · murP 70000 (-8.8%).
- Volumes cachés proxy : taker buy 0.514 · vol perp/spot 12.0×.
- ACE soft: LIVE=MASTER_BASE_V8_6_FORTRESS_8H20_LIVE_COLOR.log · SKIP=935 · heat=2.7 · PnL sess=0.9024 · RED=0.
- C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
