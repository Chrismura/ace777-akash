# Hulk DIGEST — 2026-08-21T15:24:44Z

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
| PYTHUSDT | IDLE | 0.62 | 2.49 | 0.8 | 0.1 | 3045987.62 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 1.48 | 6.25 | 0.8 | 0.14 | 148208945.33 | 0.71 | skipped_fast |
| CCUSDT | IDLE | 1.74 | 3.5 | 0.06 | 0.04 | 558079.99 | 6.61 | skipped_fast |
| ZBCNUSDT | IDLE | 1.88 | 9.04 | 3.12 | 0.18 | 477114.36 | 44.51 | skipped_fast |
| HBARUSDT | IDLE | 1.81 | 4.2 | 0.78 | 0.07 | 718750.39 | 1.28 | skipped_fast |
| WUSDT | IDLE | 2.22 | 4.71 | 0.69 | 0.07 | 334389.62 | 12.56 | skipped_fast |
| CHIPUSDT | IDLE | 0.9 | 3.8 | 3.06 | 0.05 | 519626.7 | 6.15 | skipped_fast |
| REDUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.85 | 8.14 | 0.36 | 0.1 | 97757.49 | 20.98 | skipped_fast |
| QAITUSDT | IDLE | 3.63 | 6.82 | 2.94 | -0.03 | 4152.3 | 67.05 | skipped_fast |
| RIZEUSDT | IDLE | 2.25 | 10.56 | 7.76 | -0.01 | 45747.29 | 47.09 | skipped_fast |
| BIOUSDT | IDLE | 1.62 | 3.45 | 1.5 | 0.06 | 188989.95 | 6.19 | skipped_fast |
| TELUSDT | IDLE | 2.65 | 7.92 | 3.87 | 0.06 | 232809.01 | 37.13 | skipped_fast |
| KITEUSDT | IDLE | 1.65 | 5.52 | 1.69 | 0.11 | 65001.77 | 11.05 | skipped_fast |
| EDELUSDT | IDLE | 1.41 | 2.79 | 0.22 | 0.01 | 79330.57 | 10.86 | skipped_fast |
| RWAINCUSDT | IDLE | 1.73 | 3.19 | 1.76 | 0.02 | 8239.85 | 21.61 | skipped_fast |
| QNTUSDT | IDLE | 1.33 | 2.63 | 0.2 | 0.04 | 54431.18 | 6.18 | skipped_fast |
| FLUIDUSDT | IDLE | 1.55 | 4.05 | 0.0 | 0.12 | 4405.51 | 21.43 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 1.0 | 0.41 | 0.04 | 55215.28 | 33.11 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
