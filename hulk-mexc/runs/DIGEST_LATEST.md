# Hulk DIGEST — 2026-09-23T17:22:44Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 12.25 | 7.36 | -0.06 | 1399236.22 | 4.8 | tvl≈140,236,528 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.55 | 6.67 | 5.28 | -0.05 | 122041053.56 | 2.0 | n/a |
| ETHUSDT | IDLE | 1.97 | 3.56 | 2.48 | -0.03 | 513047456.53 | 1.24 | no_map |
| BTCUSDT | IDLE | 1.6 | 2.87 | 2.23 | -0.03 | 884995302.56 | 0.0 | no_map |
| HBARUSDT | IDLE | 2.31 | 7.25 | 5.27 | -0.06 | 1553270.37 | 1.11 | empty_tvl |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.53 | 9.16 | 6.44 | -0.05 | 387663.06 | 6.13 | tvl≈1,711,676,146 |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.07 | 6.94 | 5.11 | -0.05 | 494171.84 | 7.44 | no_map |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.52 | 11.06 | 7.85 | -0.1 | 210446.95 | 10.59 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.58 | 10.94 | 7.39 | -0.07 | 221283.51 | 25.7 | no_map |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.93 | 10.05 | 6.07 | -0.04 | 99355.69 | 10.53 | n/a |
| REDUSDT | IDLE | 3.65 | 6.68 | 4.8 | -0.03 | 59128.95 | 14.94 | tvl≈2,847,874 |
| KITEUSDT | IDLE | 2.62 | 4.9 | 2.67 | -0.02 | 164608.92 | 7.49 | no_map |
| ZBCNUSDT | IDLE | 2.22 | 5.11 | 4.42 | -0.01 | 257055.25 | 29.57 | n/a |
| QNTUSDT | IDLE | 2.95 | 6.98 | 3.59 | -0.02 | 196449.18 | 5.6 | n/a |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.44 | 7.2 | 5.0 | -0.04 | 4179.09 | 21.43 | tvl≈2,612,092,424 |
| RIZEUSDT | IDLE | 1.27 | 16.61 | 14.24 | 0.35 | 69777.89 | 110.7 | no_map |
| TELUSDT | IDLE | 2.44 | 6.33 | 5.95 | -0.02 | 154651.56 | 52.96 | no_map |
| RWAINCUSDT | IDLE | 0.83 | 1.69 | 1.23 | 0.01 | 21468.67 | 5.43 | no_map |
| RWAUSDT | IDLE | 1.73 | 3.05 | 2.75 | -0.02 | 55656.81 | 22.28 | no_map |
| MNSRYUSDT | IDLE | 1.07 | 1.93 | 1.35 | -0.01 | 40855.63 | 63.77 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
