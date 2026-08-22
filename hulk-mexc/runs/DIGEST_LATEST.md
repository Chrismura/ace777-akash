# Hulk DIGEST — 2026-08-22T02:20:53Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.4 | 8.42 | 0.56 | 0.14 | 6945072.54 | 3.89 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.32 | 10.26 | 0.51 | 0.17 | 154302175.29 | 4.65 | skipped_fast |
| HBARUSDT | IDLE | 2.28 | 4.9 | 0.02 | 0.08 | 961945.05 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.8 | 0.09 | 544547.32 | 18.39 | skipped_fast |
| CCUSDT | IDLE | 1.69 | 6.26 | 0.0 | 0.15 | 656265.21 | 6.09 | skipped_fast |
| CHIPUSDT | IDLE | 2.23 | 5.07 | 0.51 | -0.01 | 515880.36 | 6.02 | skipped_fast |
| BIOUSDT | IDLE | 3.08 | 7.64 | 0.53 | 0.09 | 192668.6 | 23.86 | skipped_fast |
| WUSDT | IDLE | 1.81 | 4.91 | 0.03 | 0.1 | 401119.26 | 15.05 | skipped_fast |
| EDELUSDT | IDLE | 2.45 | 5.02 | 2.61 | -0.03 | 79693.92 | 55.65 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.9 | 0.11 | 61275.76 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.01 | 8.27 | 6.89 | 0.17 | 157048.39 | 9.8 | skipped_fast |
| QNTUSDT | IDLE | 2.25 | 4.89 | 0.43 | 0.08 | 171147.73 | 8.99 | skipped_fast |
| KITEUSDT | IDLE | 1.35 | 4.09 | 0.7 | 0.12 | 61625.76 | 11.72 | skipped_fast |
| QAITUSDT | IDLE | 1.86 | 3.57 | 0.94 | 0.0 | 3916.13 | 39.49 | skipped_fast |
| RWAINCUSDT | IDLE | 1.82 | 3.27 | 2.48 | 0.0 | 9379.52 | 43.38 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.11 | 0.97 | 0.04 | 179438.64 | 36.19 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 19.69 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.24 | 0.04 | 54808.32 | 8.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
