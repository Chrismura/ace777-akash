# Hulk DIGEST — 2026-08-19T04:46:37Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.35 | 0.66 | 0.3 | 0.01 | 10066603.52 | 1.0 | n/a |
| CHIPUSDT | IDLE | 1.65 | 5.77 | 4.64 | -0.07 | 185472.57 | 7.78 | no_map |
| PYTHUSDT | IDLE | 1.72 | 3.25 | 1.27 | 0.03 | 178004.65 | 2.57 | tvl≈86,400,925 |
| REDUSDT | IDLE | 1.22 | 8.56 | 6.8 | -0.03 | 166447.81 | 17.12 | tvl≈1,666,606 |
| CCUSDT | IDLE | 1.44 | 2.56 | 2.09 | -0.02 | 218116.48 | 8.91 | no_map |
| ZBCNUSDT | IDLE | 0.83 | 1.58 | 0.53 | 0.0 | 164582.17 | 14.02 | n/a |
| BIOUSDT | IDLE | 1.01 | 1.96 | 0.4 | 0.02 | 62863.51 | 4.02 | n/a |
| WUSDT | IDLE | 0.65 | 1.13 | 1.12 | -0.01 | 125249.14 | 12.46 | tvl≈1,354,943,773 |
| EDELUSDT | IDLE | 0.77 | 2.29 | 1.19 | -0.02 | 73527.54 | 13.34 | no_map |
| KITEUSDT | IDLE | 0.72 | 1.3 | 0.9 | -0.03 | 65225.23 | 17.57 | no_map |
| RWAINCUSDT | IDLE | 0.73 | 1.49 | 0.76 | 0.0 | 10468.92 | 53.49 | no_map |
| QAITUSDT | IDLE | 0.48 | 3.72 | 3.58 | -0.18 | 12350.27 | 67.05 | no_map |
| TELUSDT | IDLE | 0.99 | 1.88 | 0.61 | 0.05 | 85909.24 | 27.47 | no_map |
| HBARUSDT | IDLE | 0.57 | 1.12 | 0.07 | 0.03 | 111161.98 | 1.48 | empty_tvl |
| QNTUSDT | IDLE | 0.72 | 1.4 | 0.28 | 0.0 | 37890.07 | 3.55 | n/a |
| RIZEUSDT | IDLE | 1.53 | 3.92 | 2.94 | -0.05 | 27619.58 | 263.73 | no_map |
| RWAUSDT | IDLE | 0.25 | 0.44 | 0.43 | -0.01 | 51236.67 | 8.73 | no_map |
| FLUIDUSDT | IDLE | 0.48 | 0.84 | 0.83 | -0.01 | 177.92 | 22.21 | tvl≈2,328,145,559 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
