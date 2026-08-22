# Hulk DIGEST — 2026-08-22T00:23:48Z

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
| PYTHUSDT | IDLE | 1.76 | 6.39 | 1.39 | 0.1 | 6348332.26 | 2.04 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.03 | 8.23 | 1.63 | 0.14 | 143836672.97 | 2.07 | skipped_fast |
| HBARUSDT | IDLE | 2.81 | 6.36 | 1.86 | 0.07 | 930995.66 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 11.25 | 2.76 | 0.11 | 518835.57 | 16.45 | skipped_fast |
| CCUSDT | IDLE | 1.98 | 7.42 | 1.99 | 0.12 | 646502.42 | 6.28 | skipped_fast |
| WUSDT | IDLE | 2.72 | 6.91 | 0.76 | 0.08 | 384680.89 | 14.25 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 3.56 | 0.58 | 0.05 | 545191.16 | 3.06 | skipped_fast |
| BIOUSDT | IDLE | 2.27 | 5.04 | 0.68 | 0.02 | 185753.94 | 3.1 | skipped_fast |
| EDELUSDT | IDLE | 2.61 | 5.5 | 1.85 | -0.01 | 79866.23 | 22.15 | skipped_fast |
| RIZEUSDT | IDLE | 2.23 | 9.82 | 2.94 | 0.14 | 59815.53 | 43.62 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.51 | 0.06 | 188767.01 | 41.17 | skipped_fast |
| QNTUSDT | IDLE | 2.57 | 5.42 | 1.49 | 0.06 | 170952.51 | 4.55 | skipped_fast |
| KITEUSDT | IDLE | 1.07 | 3.12 | 0.46 | 0.09 | 61302.95 | 11.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.03 | 9727.87 | 59.19 | skipped_fast |
| REDUSDT | IDLE | 0.54 | 4.91 | 0.67 | 0.21 | 157748.31 | 55.14 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 54774.34 | 16.43 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.79 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
