# Hulk DIGEST — 2026-10-11T16:23:34Z

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
| XRPUSDT | IDLE | 1.38 | 2.67 | 0.6 | 0.01 | 12617430.04 | 2.12 | n/a |
| ETHUSDT | IDLE | 0.78 | 1.53 | 0.18 | 0.01 | 190498213.01 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.61 | 1.18 | 0.21 | 0.01 | 137396990.58 | 0.0 | no_map |
| WUSDT | IDLE | 1.88 | 3.67 | 0.63 | 0.01 | 870281.83 | 6.75 | tvl≈1,674,589,277 |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 31.62 | 14.61 | 0.08 | 53548.7 | 21.6 | tvl≈2,422,137,643 |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 11.9 | 7.2 | -0.0 | 29283.36 | 4.88 | no_map |
| PYTHUSDT | IDLE | 1.27 | 2.51 | 0.19 | -0.01 | 731585.46 | 3.85 | tvl≈172,259,825 |
| CCUSDT | IDLE | 2.97 | 5.91 | 0.16 | 0.06 | 320653.37 | 0.79 | no_map |
| QNTUSDT | IDLE | 1.09 | 2.06 | 0.86 | 0.01 | 908135.32 | 2.87 | n/a |
| CHIPUSDT | IDLE | 1.1 | 9.0 | 1.84 | 0.29 | 418992.86 | 15.88 | no_map |
| EDELUSDT | IDLE | 1.43 | 2.64 | 1.5 | 0.0 | 404455.21 | 23.26 | no_map |
| TELUSDT | IDLE | 3.77 | 7.16 | 2.54 | -0.01 | 140403.37 | 28.34 | no_map |
| BIOUSDT | IDLE | 1.98 | 3.88 | 0.56 | 0.04 | 74083.42 | 3.32 | n/a |
| ZBCNUSDT | IDLE | 1.62 | 3.23 | 0.02 | 0.01 | 163031.38 | 10.34 | n/a |
| REDUSDT | IDLE | 1.98 | 3.91 | 0.31 | 0.02 | 58128.53 | 13.72 | tvl≈3,713,830 |
| HBARUSDT | IDLE | 1.66 | 3.23 | 0.56 | 0.01 | 248379.57 | 11.77 | empty_tvl |
| RIZEUSDT | IDLE | 1.6 | 4.42 | 0.65 | -0.06 | 29613.96 | 61.33 | no_map |
| KITEUSDT | IDLE | 1.07 | 2.11 | 0.17 | -0.01 | 70220.18 | 10.16 | no_map |
| RWAUSDT | IDLE | 1.34 | 2.62 | 0.46 | 0.01 | 51184.22 | 7.77 | no_map |
| MNSRYUSDT | IDLE | 0.37 | 0.73 | 0.1 | -0.01 | 30081.89 | 25.98 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
