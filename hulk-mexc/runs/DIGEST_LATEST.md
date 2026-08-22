# Hulk DIGEST — 2026-08-22T02:02:56Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.42 | 8.42 | 1.1 | 0.14 | 6881593.93 | 5.86 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.34 | 10.03 | 1.75 | 0.15 | 154128360.27 | 4.71 | skipped_fast |
| HBARUSDT | IDLE | 2.34 | 4.9 | 0.83 | 0.07 | 950674.37 | 2.5 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.98 | 0.09 | 548029.43 | 13.08 | skipped_fast |
| CCUSDT | IDLE | 1.67 | 6.1 | 0.0 | 0.15 | 659992.35 | 9.58 | skipped_fast |
| CHIPUSDT | IDLE | 1.6 | 3.69 | 0.03 | 0.02 | 516331.97 | 6.08 | skipped_fast |
| WUSDT | IDLE | 1.71 | 4.41 | 0.09 | 0.09 | 400122.85 | 14.13 | skipped_fast |
| BIOUSDT | IDLE | 2.68 | 5.36 | 0.03 | 0.07 | 184993.92 | 17.99 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.97 | 0.11 | 61045.45 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.09 | 0.16 | 156862.36 | 8.09 | skipped_fast |
| EDELUSDT | IDLE | 2.37 | 5.02 | 1.41 | -0.02 | 79571.14 | 66.08 | skipped_fast |
| QNTUSDT | IDLE | 2.28 | 4.89 | 0.88 | 0.07 | 171342.15 | 7.53 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 4.09 | 0.09 | 0.13 | 61300.0 | 10.74 | skipped_fast |
| QAITUSDT | IDLE | 1.78 | 3.57 | 0.0 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.11 | 1.07 | 0.04 | 178953.75 | 41.37 | skipped_fast |
| RWAINCUSDT | IDLE | 1.75 | 3.27 | 1.58 | 0.03 | 9241.73 | 64.41 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 20.57 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.04 | 54561.42 | 8.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
