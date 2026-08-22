# Hulk DIGEST — 2026-08-22T01:56:57Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.89 | 10.86 | 1.29 | 0.14 | 6859774.65 | 3.92 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.41 | 10.52 | 1.45 | 0.15 | 153675437.72 | 5.38 | skipped_fast |
| HBARUSDT | IDLE | 3.03 | 6.36 | 1.05 | 0.07 | 948659.63 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.81 | 0.09 | 550531.74 | 18.4 | skipped_fast |
| CCUSDT | IDLE | 1.81 | 7.36 | 0.8 | 0.16 | 662331.93 | 8.78 | skipped_fast |
| WUSDT | IDLE | 2.68 | 6.65 | 0.32 | 0.08 | 398428.23 | 13.18 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 3.56 | 1.19 | 0.02 | 510519.7 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.62 | 5.86 | 0.58 | 0.05 | 185118.45 | 3.06 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79521.1 | 22.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.97 | 0.11 | 61049.58 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.43 | 0.15 | 157005.3 | 12.19 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 5.17 | 0.39 | 0.12 | 61296.06 | 13.46 | skipped_fast |
| QNTUSDT | IDLE | 2.43 | 5.18 | 1.12 | 0.07 | 171362.1 | 6.04 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| TELUSDT | IDLE | 2.58 | 6.19 | 1.02 | 0.05 | 180882.1 | 51.76 | skipped_fast |
| RWAINCUSDT | IDLE | 1.77 | 3.27 | 1.79 | 0.03 | 9181.85 | 101.69 | skipped_fast |
| FLUIDUSDT | IDLE | 1.46 | 3.74 | 2.03 | 0.08 | 4799.07 | 19.84 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54646.97 | 16.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
